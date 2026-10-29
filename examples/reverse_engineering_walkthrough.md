# Example 2: Reverse Engineering & Clean-Room Reproduction Walkthrough

This walkthrough demonstrates executing the 10-Phase Reverse Engineering Protocol, firmware snapshot fuzzing, clean-room functional specification export, and FSD generation.

---

## 1. Scenario: Proprietary Binary Protocol & Firmware Decompilation

A user requests:
> *"Reverse engineer a proprietary embedded motor controller binary firmware that communicates over CAN bus, extract its state machine, verify safety invariants via snapshot fuzzing, and output a clean-room legal functional specification for legal reproduction."*

---

## 2. CLI Execution

### Phase 1 to 5: Disassembly, AST Reconstruction & Control Flow
```bash
python scripts/reverse_engineering_analyst.py --target-binary assets/firmware_sample.bin --mode full
```
* **Output:**
  - Extracts section headers, function entry points, and opcode histograms.
  - Generates ASCII Control Flow Graph (CFG) and cyclomatic complexity metrics.
  - Reconstructs deobfuscated high-level AST pseudocode.

### Phase 6: Dynamic Firmware Snapshot Fuzzing
```bash
python scripts/firmware_fuzzing_harness.py --iterations 100 --target-state-machine
```
* **Output:** Executes 100 snapshot mutations with sub-millisecond execution, measuring branch coverage, state transitions, and edge anomaly detection without hardware emulation overhead.

### Phase 7 to 9: Clean-Room Legal Functional Specification Export
```bash
python scripts/clean_room_export_engine.py --analysis-file reports/re_analysis.json --output-spec docs/clean_room_spec.md
```
* **Output:**
  - Enforces Chinese Wall isolation: strips copyrighted strings and proprietary symbols.
  - Generates verifiable input/output state tables, packet framing specifications, and algorithmic invariants.

### Phase 10: Dynamic FSD Download & Interactive UI
Launch the interactive web portal:
```bash
python scripts/reverse_engineering_server.py --port 8080
```
Navigate to `http://localhost:8080` to view the 10-phase visual dashboard and click **"Export Clean-Room Functional Spec (FSD)"** to download the clean-room markdown document directly in the browser.

---

## 3. Python API Integration

```python
from scripts.reverse_engineering_analyst import ReverseEngineeringAnalyst
from scripts.firmware_fuzzing_harness import FirmwareFuzzingHarness
from scripts.clean_room_export_engine import CleanRoomExportEngine

# 1. Analyze binary
analyst = ReverseEngineeringAnalyst()
analysis_report = analyst.analyze_binary_payload(b"\x7fELF\x02\x01\x01\x00" + b"\x90" * 64)

# 2. Run fuzzing harness
harness = FirmwareFuzzingHarness()
fuzz_results = harness.run_fuzzing_campaign(iterations=50)

# 3. Export clean-room functional spec
exporter = CleanRoomExportEngine()
spec_doc = exporter.generate_clean_room_specification(analysis_report, fuzz_results)

print("Clean-Room Spec Length:", len(spec_doc))
print("Chinese Wall Compliant:", "CHINESE WALL AUDIT: PASS" in spec_doc)
```
