"""
Formal Systems Engineering & Mathematical Modeling Engine
Zobar Skill — First Principles Rigor, Roofline Models, Queueing Theory & Physics

Mathematical Formulations:
1. Roofline Model: Arithmetic Intensity (FLOPs/Byte) vs Hardware Bandwidth.
   Attainable Performance = min(Peak Compute, Memory Bandwidth * Arithmetic Intensity).
2. Queueing Theory (Little's Law & M/M/1 Latency):
   Average Wait Time: W = 1 / (mu - lambda), Queue Length: L = lambda * W.
3. Amdahl's Law & Gustafson's Law:
   Theoretical Speedup: S(s) = 1 / ((1 - p) + (p / s)).
4. Spring Physics (2nd Order Linear ODE):
   m * d^2x/dt^2 + c * dx/dt + k * x = 0 (Critically Damped, Underdamped, Overdamped).
5. Kelly Criterion for Venture & Feature Capital Allocation:
   f* = (p * (b + 1) - 1) / b.
"""

import math
from typing import Dict, Any, List, Optional, Tuple


class SystemsMathEngine:
    HARDWARE_PROFILES = {
        "nvidia_h100_sxm": {"peak_tflops_fp16": 1979.0, "memory_bandwidth_gb_s": 3350.0},
        "nvidia_a100_80gb": {"peak_tflops_fp16": 312.0, "memory_bandwidth_gb_s": 2039.0},
        "nvidia_rtx_4090": {"peak_tflops_fp16": 165.2, "memory_bandwidth_gb_s": 1008.0},
        "apple_m3_max": {"peak_tflops_fp16": 28.0, "memory_bandwidth_gb_s": 400.0},
        "intel_xeon_8480": {"peak_tflops_fp16": 8.0, "memory_bandwidth_gb_s": 307.0},
    }

    @classmethod
    def calculate_roofline_analysis(
        cls,
        total_flops: float,
        total_bytes_transferred: float,
        hardware_target: str = "nvidia_a100_80gb"
    ) -> Dict[str, Any]:
        """
        Berkeley Roofline Model:
        Determines if a workload is Memory-Bound (limited by RAM/VRAM bandwidth)
        or Compute-Bound (limited by arithmetic ALUs/Tensor Cores).
        """
        hw = cls.HARDWARE_PROFILES.get(hardware_target, cls.HARDWARE_PROFILES["nvidia_a100_80gb"])
        peak_gflops = hw["peak_tflops_fp16"] * 1000.0
        bw_gb_s = hw["memory_bandwidth_gb_s"]

        # Arithmetic Intensity = FLOPs / Byte
        arithmetic_intensity = total_flops / max(total_bytes_transferred, 1.0)
        
        # Knee point (Balance point where workload transitions from Memory to Compute bound)
        machine_balance_intensity = peak_gflops / bw_gb_s

        # Attainable Performance (GFLOP/s)
        attainable_gflops = min(peak_gflops, bw_gb_s * arithmetic_intensity)
        is_memory_bound = arithmetic_intensity < machine_balance_intensity

        # Execution time estimation
        theoretical_min_latency_ms = (total_flops / (attainable_gflops * 1e9)) * 1000.0

        return {
            "hardware_target": hardware_target,
            "arithmetic_intensity_flops_per_byte": round(arithmetic_intensity, 3),
            "machine_balance_knee_point": round(machine_balance_intensity, 3),
            "bottleneck_classification": "MEMORY_BANDWIDTH_BOUND" if is_memory_bound else "COMPUTE_ALU_BOUND",
            "attainable_tflops": round(attainable_gflops / 1000.0, 3),
            "hardware_peak_tflops": hw["peak_tflops_fp16"],
            "memory_bandwidth_gb_s": bw_gb_s,
            "theoretical_min_latency_ms": round(theoretical_min_latency_ms, 4),
            "optimization_recommendation": (
                "VRAM/RAM darboğazı var: PagedAttention, KV-cache quantization (AWQ/INT4) veya Kernel Fusion (FlashAttention) ile bellek erişimini azaltın."
                if is_memory_bound else
                "Hesaplama darboğazı var: Matris tensör çekirdeği optimizasyonu ve FP8/INT8 SIMD paralelleştirmesi uygulayın."
            )
        }

    @classmethod
    def calculate_queueing_latency(
        cls,
        arrival_rate_lambda: float,  # Requests per second arriving
        service_rate_mu: float,       # Requests per second the server can process
        concurrency_channels_c: int = 1
    ) -> Dict[str, Any]:
        """
        Little's Law & M/M/1 Queueing Theory:
        Models queue saturation, average response time, and tail latency risk.
        """
        if arrival_rate_lambda >= (service_rate_mu * concurrency_channels_c):
            return {
                "system_status": "UNSTABLE_QUEUE_OVERFLOW",
                "utilization_rho": round(arrival_rate_lambda / (service_rate_mu * concurrency_channels_c), 2),
                "error": "İstek varış hızı servis kapasitesini aşıyor. Kuyruk sonsuza doğru şişiyor (Buffer Bloat).",
                "recommended_min_capacity": math.ceil(arrival_rate_lambda * 1.3),
            }

        rho = arrival_rate_lambda / (service_rate_mu * concurrency_channels_c)  # System utilization
        # M/M/1 Average Time in System W = 1 / (mu - lambda)
        effective_mu = service_rate_mu * concurrency_channels_c
        avg_latency_seconds = 1.0 / (effective_mu - arrival_rate_lambda)
        avg_queue_depth_l = arrival_rate_lambda * avg_latency_seconds

        # P95 and P99 latency approximations under exponential distribution:
        # P(t) = W * ln(1 / (1 - P))
        p95_latency_ms = avg_latency_seconds * math.log(1.0 / 0.05) * 1000.0
        p99_latency_ms = avg_latency_seconds * math.log(1.0 / 0.01) * 1000.0

        return {
            "system_status": "STABLE",
            "utilization_percent": round(rho * 100.0, 1),
            "arrival_rate_rps": arrival_rate_lambda,
            "service_capacity_rps": effective_mu,
            "average_queue_length_items": round(avg_queue_depth_l, 2),
            "average_latency_ms": round(avg_latency_seconds * 1000.0, 2),
            "p95_tail_latency_ms": round(p95_latency_ms, 2),
            "p99_tail_latency_ms": round(p99_latency_ms, 2),
            "sla_health": "EXCELLENT (<50ms)" if p99_latency_ms < 50.0 else "AT_RISK_TAIL_SPIKE",
        }

    @classmethod
    def calculate_amdahl_speedup(
        cls,
        parallel_fraction_p: float,  # Fraction of code that can be parallelized (0.0 to 1.0)
        processor_cores_s: int        # Number of parallel workers / threads
    ) -> Dict[str, Any]:
        """
        Amdahl's Law:
        Speedup = 1 / ((1 - p) + (p / s))
        Calculates theoretical limits of multi-threading / GPU scaling.
        """
        p = max(min(parallel_fraction_p, 1.0), 0.0)
        s = max(processor_cores_s, 1)

        speedup = 1.0 / ((1.0 - p) + (p / float(s)))
        theoretical_max_speedup = 1.0 / (1.0 - p) if p < 1.0 else float("inf")
        efficiency_percent = (speedup / float(s)) * 100.0

        return {
            "parallel_fraction": p,
            "core_count": s,
            "achieved_speedup_multiplier": round(speedup, 2),
            "theoretical_infinite_core_limit": round(theoretical_max_speedup, 2) if theoretical_max_speedup != float("inf") else "Sonsuz (Embarrassingly Parallel)",
            "multicore_efficiency_percent": round(efficiency_percent, 1),
            "serial_bottleneck_percent": round((1.0 - p) * 100.0, 1),
        }

    @classmethod
    def calculate_spring_physics(
        cls,
        mass_m: float = 1.0,
        stiffness_k: float = 180.0,
        damping_c: float = 12.0,
        initial_displacement: float = 1.0,
        timesteps_count: int = 10,
        dt: float = 0.01667  # 60 FPS delta time
    ) -> Dict[str, Any]:
        """
        Linear 2nd Order Differential Equation for Apple/Framer UI Springs:
        m * x''(t) + c * x'(t) + k * x(t) = 0
        Damping ratio: zeta = c / (2 * sqrt(m * k))
        - zeta = 1: Critically Damped (Fastest settle without oscillation - Apple HIG default)
        - zeta < 1: Underdamped (Bouncy spring, playful micro-interactions)
        - zeta > 1: Overdamped (Sluggish transition)
        """
        omega_0 = math.sqrt(stiffness_k / mass_m)
        zeta = damping_c / (2.0 * math.sqrt(mass_m * stiffness_k))

        regime = (
            "CRITICALLY_DAMPED (Apple HIG Standard - Sıfır Salınım)"
            if abs(zeta - 1.0) < 0.05 else
            ("UNDERDAMPED (Yaylanmalı - Eğlenceli UI)" if zeta < 1.0 else "OVERDAMPED (Ağır - Hantal)")
        )

        # Numerical simulation of trajectory for N frames
        x = initial_displacement
        v = 0.0
        trajectory = []

        for frame in range(timesteps_count):
            a = (-damping_c * v - stiffness_k * x) / mass_m
            v += a * dt
            x += v * dt
            trajectory.append({"frame": frame + 1, "time_s": round((frame + 1) * dt, 3), "position": round(x, 4)})

        return {
            "damping_ratio_zeta": round(zeta, 3),
            "undamped_frequency_hz": round(omega_0 / (2.0 * math.pi), 2),
            "regime": regime,
            "settling_frames_approx": int(4.0 / max(zeta * omega_0 * dt, 0.001)),
            "trajectory_sample": trajectory[:5],
        }

    @classmethod
    def calculate_kelly_capital_allocation(
        cls,
        win_probability_p: float,
        upside_downside_ratio_b: float,
        bankroll_or_time_budget_usd: float = 10000.0
    ) -> Dict[str, Any]:
        """
        Kelly Criterion for Asymmetric Bets & Product Features:
        f* = (p * (b + 1) - 1) / b
        Computes mathematically optimal capital/time allocation to avoid ruin while maximizing CAGR.
        """
        p = max(min(win_probability_p, 0.999), 0.001)
        b = max(upside_downside_ratio_b, 0.01)

        f_star = (p * (b + 1.0) - 1.0) / b
        f_clamped = max(min(f_star, 0.50), 0.0)  # Conservative half-Kelly cap to prevent volatility drag

        recommended_allocation_usd = bankroll_or_time_budget_usd * f_clamped

        return {
            "win_probability_percent": round(p * 100.0, 1),
            "payoff_multiple_ratio": round(b, 2),
            "pure_kelly_fraction": round(f_star, 4),
            "conservative_half_kelly_allocation_percent": round(f_clamped * 100.0, 2),
            "recommended_budget_allocation_usd": round(recommended_allocation_usd, 2),
            "risk_verdict": "POZİTİF ASİMETRİK BEKLENTİ (Yatırım Yapılabilir)" if f_star > 0 else "NEGATİF BEKLENTİ (Sermaye İsrafı - İptal Et)",
        }


if __name__ == "__main__":
    eng = SystemsMathEngine()
    print("=" * 65)
    print("[*] MATEMATİKSEL SİSTEM MÜHENDİSLİĞİ ÇEKİRDEĞİ TESTİ")
    print("=" * 65)

    # 1. Roofline
    roof = eng.calculate_roofline_analysis(total_flops=1e12, total_bytes_transferred=5e10, hardware_target="nvidia_a100_80gb")
    print(f"[*] Roofline Sonucu: {roof['bottleneck_classification']} (Yoğunluk: {roof['arithmetic_intensity_flops_per_byte']} FLOP/B)")

    # 2. Queueing
    queue = eng.calculate_queueing_latency(arrival_rate_lambda=450.0, service_rate_mu=500.0)
    print(f"[*] Kuyruk Teorisi: P99 Gecikme = {queue['p99_tail_latency_ms']}ms | Doluluk: %{queue['utilization_percent']}")

    # 3. Amdahl
    amd = eng.calculate_amdahl_speedup(parallel_fraction_p=0.90, processor_cores_s=16)
    print(f"[*] Amdahl Yasası: %90 Paralel / 16 Çekirdek -> Hızlanma: {amd['achieved_speedup_multiplier']}x")

    # 4. Spring Physics
    spring = eng.calculate_spring_physics(mass_m=1.0, stiffness_k=200.0, damping_c=28.28)
    print(f"[*] Yay Fiziği (Apple Spring): Zeta = {spring['damping_ratio_zeta']} [{spring['regime']}]")

    # 5. Kelly
    kelly = eng.calculate_kelly_capital_allocation(win_probability_p=0.40, upside_downside_ratio_b=4.0, bankroll_or_time_budget_usd=25000.0)
    print(f"[*] Kelly Kriteri: Ayrılacak Bütçe = ${kelly['recommended_budget_allocation_usd']:,} ({kelly['risk_verdict']})")
