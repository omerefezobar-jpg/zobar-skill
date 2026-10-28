"""
Stage 2 Continual Learning & Context Compression Tests
Unit tests for ContextCompressor, ContinualMemoryEngine, and DPOLoRADatasetPipeline.
"""

import os
import unittest
import tempfile
import json
from scripts.context_compressor import ContextCompressor
from scripts.continual_memory_engine import ContinualMemoryEngine
from scripts.dpo_lora_dataset_pipeline import DPOLoRADatasetPipeline


class TestStage2ContinualLearning(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.memory_file = os.path.join(self.temp_dir.name, "test_kg.json")
        self.compressor = ContextCompressor(max_active_turns=2)
        self.memory = ContinualMemoryEngine(memory_file=self.memory_file)
        self.pipeline = DPOLoRADatasetPipeline(data_dir=self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_context_compressor_prunes_fillers_preserves_code(self):
        raw_text = (
            "Tabii ki, harika bir soru! Memnuniyetle açıklayayım. "
            "Python'da asenkron kod şu şekilde yazılır:\n"
            "```python\nasync def fast_run():\n    return 42\n```\n"
            "Gördüğünüz gibi son derece hızlıdır."
        )
        pruned = self.compressor.prune_low_entropy_tokens(raw_text)

        # Filler words must be stripped
        self.assertNotIn("Tabii ki", pruned)
        self.assertNotIn("Memnuniyetle açıklayayım", pruned)
        self.assertNotIn("Gördüğünüz gibi", pruned)

        # Code block must remain completely intact
        self.assertIn("```python\nasync def fast_run():\n    return 42\n```", pruned)

    def test_context_compressor_sliding_window_reduction(self):
        long_conversation = [
            {"role": "user", "content": "Ben sıfır sermaye ile bir mikro SaaS başlatmak istiyorum. Rust ve Tauri tercih ediyorum. Bu sistemde masaüstü istemcisi ultra hafif olmalı ve bellek ayak izi 30MB'ı geçmemeli. Ayrıca yerel önbellekleme ve SQLite kullanılmalı."},
            {"role": "assistant", "content": "Harika bir tercih! Rust ve Tauri bellek kullanımını 30MB seviyesinde tutar. SQLite WAL modunda çalıştırıldığında eşzamanlı okuma ve yazma işlemlerinde sıfır gecikme sağlar. Ayrıca işletim sisteminin native WebView2 motorunu kullandığı için Chromium gibi 1GB RAM tüketmez."},
            {"role": "user", "content": "Veritabanında Supabase ve pgvector kullanmak istiyorum. Ayrıca sistem çok hızlı olsun. Tüm SQL şemalarında Row Level Security ve HNSW indeksleme bulunmalı, dışarıya asla veri sızmamalı."},
            {"role": "assistant", "content": "Tabii ki! Supabase pgvector HNSW indeksi ile yüksek hız sunar. Row Level Security politikaları her organizasyonu izole eder ve multi-tenant veri güvenliğini garanti altına alır."},
            {"role": "user", "content": "Şimdi bana ilk API route kodunu ver."},
        ]

        res = self.compressor.compress_conversation(long_conversation)

        self.assertIn("state_summary", res)
        self.assertGreater(res["compression_ratio_percent"], 20.0)
        self.assertIn("Rust", res["state_summary"]["key_technologies"])
        self.assertIn("Tauri", res["state_summary"]["key_technologies"])
        self.assertIn("Supabase", res["state_summary"]["key_technologies"])
        self.assertEqual(len(res["active_messages"]), 2)

    def test_continual_memory_learns_and_recalls(self):
        # Including 'c++' which triggers re.error: multiple repeat on Python 3.10 if not properly escaped
        text = "Benim projelerimde kesinlikle Rust, c++ ve Supabase olmalı, mimari olarak ECS kullanıyorum ve her şey sub-millisecond hızlı olmalı."
        extracted = self.memory.learn_from_text(text)

        self.assertGreater(len(extracted), 0)
        self.assertIn("rust", self.memory.user_profile["preferred_languages"])
        self.assertIn("c++", self.memory.user_profile["preferred_languages"])
        self.assertIn("supabase", self.memory.user_profile["preferred_frameworks"])
        self.assertIn("ECS", self.memory.user_profile["core_architectures"])

        # Recall test
        query = "Biz hangi mimari kalıbı ve veritabanını kullanıyorduk?"
        recalled = self.memory.recall_relevant_memories(query)
        self.assertGreater(len(recalled), 0)

        # Prompt injection test
        injection = self.memory.build_memory_prompt_injection()
        self.assertIn("RUST", injection)
        self.assertIn("SUPABASE", injection)
        self.assertIn("ECS", injection)

    def test_dpo_lora_dataset_pipeline(self):
        record = self.pipeline.record_correction(
            prompt="Tauri v2 projesinde pencere ayarı nasıl yapılır?",
            chosen="tauri.conf.json dosyasında app.windows dizisinde ayarlanır.",
            rejected="React içindeki window.resizeTo() fonksiyonu çağrılır.",
            category="desktop_architecture"
        )

        self.assertIn("id", record)
        self.assertEqual(record["chosen"], "tauri.conf.json dosyasında app.windows dizisinde ayarlanır.")

        # Check DPO JSONL file existence and validity
        self.assertTrue(os.path.exists(self.pipeline.dpo_file))
        with open(self.pipeline.dpo_file, "r", encoding="utf-8") as f:
            lines = [json.loads(line) for line in f if line.strip()]
            self.assertEqual(len(lines), 1)
            self.assertEqual(lines[0]["prompt"], record["prompt"])
            self.assertEqual(lines[0]["chosen"], record["chosen"])
            self.assertEqual(lines[0]["rejected"], record["rejected"])

        # Check LoRA SFT JSONL file existence and validity
        self.assertTrue(os.path.exists(self.pipeline.lora_file))
        with open(self.pipeline.lora_file, "r", encoding="utf-8") as f:
            sft_lines = [json.loads(line) for line in f if line.strip()]
            self.assertEqual(len(sft_lines), 1)
            self.assertEqual(sft_lines[0]["output"], record["chosen"])

        # Check unsloth training script config export
        config = self.pipeline.export_unsloth_training_script_config()
        self.assertEqual(config["dataset_format"], "dpo")
        self.assertTrue(config["load_in_4bit"])


if __name__ == "__main__":
    unittest.main()
