# Evaluasi Mock JLPT N5 (tertulis) — Tracker per Subtipe

> ⚙️ **Tabel AUTO-GENERATED oleh `scripts/kb.py`** (`render`/`record`) dari sumber
> `progress/attempts.jsonl` + `baseline.json` (hanya sesi `kind=jlpt`). **Jangan edit angka
> tabel dengan tangan.** Prosa **Weak types** = milik model (`weak_narrative` saat `record`).

Diperbarui otomatis oleh skill `/jlpt` setiap selesai sesi. Melacak akurasi
**per subtipe soal JLPT N5 tertulis** (2 sesi: 文字・語彙 + 文法・読解), lalu
memeringkat **weak types** untuk memandu `/jlpt review`.

> **Terpisah dari `evaluation.md`.** `evaluation.md` = tracker grammar `/quiz` (per
> pola/partikel/lesson) dan **tidak disentuh** oleh `/jlpt`. File ini khusus subtipe
> JLPT. `聴解` (listening) di luar cakupan (butuh audio).

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-09-07 · total sesi: 19_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 37 | 38 | 97% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 35 | 38 | 92% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 34 | 38 | 89% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 37 | 38 | 97% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 32 | 37 | 86% | 🟢 |
| Susun kalimat (★) | `DK-narabekae` | 18 | 20 | 90% | 🟢 |
| Tata bahasa dalam teks (cloze) | `DK-bunshou` | 17 | 18 | 94% | 🟢 |
| Bacaan pendek | `DK-dokkai` | 37 | 38 | 97% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 35 | 38 | 92% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
**Tak ada 🔴/🟡 — sembilan subtipe tetap 🟢.** Mock 2026-09-07 skor **16/16 (100%)** — Sesi 1 **8/8** & Sesi 2 **8/8**, sempurna tanpa satu slip pun. Sesi 1: 読み方 (来年→らいねん, 毎朝→まいあさ) & 表記 (本, 東) benar termasuk diskriminasi radikal bentuk-mirip (本 vs 木/休/体; 東 vs 車/束/重) — perbaikan pasca miss 休↔体 mock lalu terlihat. 文脈規定 naik solid (りょこう terkunci cue ほっかいどうへ; おしえます dengan subjek 先生→学生). 類義 (つまらない⇄おもしろくない; 両親⇄父と母) mulus. Sesi 2 kokoh menyeluruh: DK-bunpou (かえさ+なければ, ない-stem 返します benar), DK-narabekae (くにへ かえる まえに おみやげを — 辞書形+まえに tersusun tepat), DK-bunshou 2/2 (でも kontras 'susah TAPI indah' + くれて arah pemberian teman→aku dari alur cerita), DK-dokkai 2/2 & DK-joho 2/2 (info transport & jam pertama/hari libur). **Angka bergerak:** MG-yomi 97%, MG-hyouki 92%, MG-bunmyaku 89%, MG-ruigi 97%, DK-bunpou 86%, DK-narabekae naik 89%→90%, DK-bunshou 94%, DK-dokkai 97%, DK-joho 92% — semua 🟢. **Rekomendasi:** lanjut mock berkala lawan decay (skor plafon → sesekali naikkan kesulitan: kanji 🔴 langka 千/北/南, pola grammar campur 2 lesson dalam satu narabekae). Rotasi tema mock berikut: hindari sekolah-rutinitas / jadwal-bus / surat-jalanjalan; MG-hyouki teruskan pasangan bentuk-mirip (大↔太↔犬↔天, 目↔見).
