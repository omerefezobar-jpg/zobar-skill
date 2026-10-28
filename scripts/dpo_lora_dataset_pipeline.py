"""
DPO & LoRA Continuous Learning Dataset Pipeline
Zobar Skill — Kullanıcı Geri Bildirimlerinden Sürekli Eğitim Veri Kümesi Oluşturucu

Görev:
1. Kullanıcı düzeltmelerini (Prompt, Chosen, Rejected) yakalar.
2. Direct Preference Optimization (DPO) standart JSONL formatına çevirir (Unsloth / TRL uyumlu).
3. Supervised Fine-Tuning (LoRA SFT Alpaca) veri formatına aktarır.
4. Modelin temel yeteneklerini bozmadan (Felaketli Unutma olmadan) gece eğitimi
   için hazır veri paketleri üretir.
"""

import os
import time
import json
from typing import Dict, Any, List, Optional


class DPOLoRADatasetPipeline:
    def __init__(self, data_dir: Optional[str] = None):
        if data_dir:
            self.data_dir = data_dir
        else:
            self.data_dir = os.path.join(os.path.dirname(__file__), "..", "references")
        os.makedirs(self.data_dir, exist_ok=True)

        self.dpo_file = os.path.join(self.data_dir, "dpo_training_dataset.jsonl")
        self.lora_file = os.path.join(self.data_dir, "lora_sft_dataset.jsonl")
        self.telemetry_file = os.path.join(self.data_dir, "continual_feedback_log.json")

        self.feedbacks: List[Dict[str, Any]] = []
        self.load()

    def load(self) -> None:
        if os.path.exists(self.telemetry_file):
            try:
                with open(self.telemetry_file, "r", encoding="utf-8") as f:
                    self.feedbacks = json.load(f)
            except Exception:
                self.feedbacks = []

    def save(self) -> None:
        try:
            with open(self.telemetry_file, "w", encoding="utf-8") as f:
                json.dump(self.feedbacks, f, indent=2, ensure_ascii=False)
        except Exception:
            pass

    def record_correction(
        self,
        prompt: str,
        chosen: str,
        rejected: str,
        category: str = "coding_preference",
        user_id: str = "default_user",
    ) -> Dict[str, Any]:
        """
        Records a DPO pairwise preference when user corrects or prefers an answer.
        """
        record = {
            "id": f"dpo_{int(time.time()*1000)}",
            "timestamp": time.time(),
            "category": category,
            "user_id": user_id,
            "prompt": prompt.strip(),
            "chosen": chosen.strip(),
            "rejected": rejected.strip(),
        }
        self.feedbacks.append(record)
        self.save()

        # Append to live DPO JSONL file
        with open(self.dpo_file, "a", encoding="utf-8") as f:
            dpo_entry = {
                "prompt": record["prompt"],
                "chosen": record["chosen"],
                "rejected": record["rejected"],
            }
            f.write(json.dumps(dpo_entry, ensure_ascii=False) + "\n")

        # Append to live LoRA SFT JSONL file (Alpaca format)
        with open(self.lora_file, "a", encoding="utf-8") as f:
            lora_entry = {
                "instruction": record["prompt"],
                "input": "",
                "output": record["chosen"],
            }
            f.write(json.dumps(lora_entry, ensure_ascii=False) + "\n")

        return record

    def get_stats(self) -> Dict[str, Any]:
        return {
            "total_feedback_records": len(self.feedbacks),
            "dpo_file_path": os.path.basename(self.dpo_file),
            "lora_file_path": os.path.basename(self.lora_file),
            "ready_for_nightly_lora": len(self.feedbacks) >= 1,
            "categories": list(set(f.get("category", "general") for f in self.feedbacks)),
        }

    def export_unsloth_training_script_config(self) -> Dict[str, Any]:
        """
        Generates standard configuration parameters for unsloth / HuggingFace PEFT training.
        """
        return {
            "model_name": "unsloth/Meta-Llama-3.1-8B-Instruct",
            "max_seq_length": 2048,
            "load_in_4bit": True,
            "lora_r": 16,
            "lora_alpha": 16,
            "lora_dropout": 0.05,
            "target_modules": ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
            "dataset_file": os.path.abspath(self.dpo_file),
            "dataset_format": "dpo",
            "epochs": 1,
            "learning_rate": 5e-5,
            "batch_size": 2,
            "gradient_accumulation_steps": 4,
        }


if __name__ == "__main__":
    pipeline = DPOLoRADatasetPipeline()
    sample = pipeline.record_correction(
        prompt="React projesinde global state için ne kullanmalıyım?",
        chosen="Zustand veya Nanostores kullanmalısın; Redux boilerplate'i olmadan hafif ve hızlı çalışır.",
        rejected="Redux Toolkit kurup karmaşık reducer ve dispatch aksiyonları tanımlamalısın.",
        category="frontend_architecture"
    )
    print("DPO Çifti Kaydedildi:")
    print(json.dumps(sample, indent=2, ensure_ascii=False))
    print("\nEğitim İstatistikleri:")
    print(json.dumps(pipeline.get_stats(), indent=2))
