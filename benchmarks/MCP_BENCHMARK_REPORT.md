# ⚡ Canlı MCP Sunucusu ve Araç Performans Skorkartı

**Tarih:** 2026-10-28 | **Protokol:** JSON-RPC 2.0 (stdio) | **Sunucu:** `zobar-mcp-engine`
**El Sıkışma (Handshake) Gecikmesi:** `62.44 ms`

| Araç Adı (Tool Name) | Çağrı Sayısı | Min (ms) | Ortalama (ms) | p95 (ms) | Maks (ms) | Durum |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `smart_route` | 25 | 0.08 | **0.15** | 0.16 | 1.23 | ✅ PASS (Sub-10ms) |
| `semantic_cache_query` | 25 | 0.03 | **0.05** | 0.07 | 0.08 | ✅ PASS (Sub-10ms) |
| `compress_context` | 25 | 0.06 | **0.12** | 0.17 | 0.51 | ✅ PASS (Sub-10ms) |
| `simulate_unit_economics` | 25 | 0.04 | **0.05** | 0.07 | 0.08 | ✅ PASS (Sub-10ms) |
| `generate_image_prompt` | 25 | 0.04 | **0.05** | 0.07 | 0.07 | ✅ PASS (Sub-10ms) |
| `step_ecs_simulation` | 25 | 3.99 | **4.41** | 4.92 | 5.12 | ✅ PASS (Sub-10ms) |

> [!IMPORTANT]
> Bu skorkart, mock veya varsayımsal hesaplama değil; çalışan canlı bir subprocess üzerinden `stdio` boru hattı açılarak ölçülmüş **gerçek donanım gecikmesidir**.