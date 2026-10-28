# ⚡ Canlı MCP Sunucusu ve Araç Performans Skorkartı

**Tarih:** 2026-10-28 | **Protokol:** JSON-RPC 2.0 (stdio) | **Sunucu:** `zobar-mcp-engine`
**El Sıkışma (Handshake) Gecikmesi:** `61.91 ms`

| Araç Adı (Tool Name) | Çağrı Sayısı | Min (ms) | Ortalama (ms) | p95 (ms) | Maks (ms) | Durum |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `smart_route` | 25 | 0.09 | **0.19** | 0.27 | 1.31 | ✅ PASS (Sub-10ms) |
| `semantic_cache_query` | 25 | 0.38 | **0.52** | 0.66 | 1.03 | ✅ PASS (Sub-10ms) |
| `compress_context` | 25 | 0.06 | **0.1** | 0.14 | 0.82 | ✅ PASS (Sub-10ms) |
| `simulate_unit_economics` | 25 | 0.04 | **0.05** | 0.08 | 0.13 | ✅ PASS (Sub-10ms) |
| `generate_image_prompt` | 25 | 0.06 | **0.09** | 0.15 | 0.15 | ✅ PASS (Sub-10ms) |
| `step_ecs_simulation` | 25 | 4.2 | **4.69** | 5.13 | 5.41 | ✅ PASS (Sub-10ms) |

> [!IMPORTANT]
> Bu skorkart, mock veya varsayımsal hesaplama değil; çalışan canlı bir subprocess üzerinden `stdio` boru hattı açılarak ölçülmüş **gerçek donanım gecikmesidir**.