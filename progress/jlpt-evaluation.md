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

_Terakhir diperbarui: 2026-08-30 · total sesi: 10_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 19 | 20 | 95% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 19 | 20 | 95% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 17 | 20 | 85% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 20 | 20 | 100% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 24 | 28 | 86% | 🟢 |
| Susun kalimat (★) | `DK-narabekae` | 10 | 12 | 83% | 🟢 |
| Tata bahasa dalam teks (cloze) | `DK-bunshou` | 0 | 0 | 0% | ⚪ |
| Bacaan pendek | `DK-dokkai` | 19 | 20 | 95% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 18 | 20 | 90% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
_🎉 **PERFECT 16/16 (100%)** — mock kesepuluh, tak ada satu pun salah. **Seluruh 8 subtipe 🟢 & semua NAIK:** `MG-yomi` 95%, `MG-hyouki` 95%, `MG-bunmyaku` 83%→**85%** (titik terlemah lama, kini menguat — りょこう & けします benar dgn cue konteks yang mengunci), `MG-ruigi` 100%, `DK-bunpou` 84%→**86%**, `DK-narabekae` 82%→**83%** (おふろに はいってから, koheren pola urutan), `DK-dokkai` 95%, `DK-joho` 90%. Kendaraan 🔴 Anki (kanji 先/時/友/会; kosakata りょこう/けします; verb おります) semua benar di format soal JLPT normal._

**Sinyal yang perlu diperhatikan:**
- ✅ **JLPT tertulis N5 matang penuh** — dua mock beruntun tanpa 🔴/🟡; `MG-bunmyaku` (yang pernah paling rendah) kini 85% stabil. Tak ada lubang subtipe.
- ✅ **Item 🔴 Anki tertangani dalam konteks** — begitu kanji/kosakata sulit muncul di soal JLPT normal (bukan drill), semua terjawab benar → sinyal lapses Anki belum tentu jadi error saat ada konteks.
- **Rekomendasi:** pertahankan lewat **mock berkala** saja; tak ada subtipe untuk dikejar. Energi latihan bisa dialihkan ke pemeliharaan ringan `/quiz` (juga sudah bersih 🟢) — praktis N5 tertulis siap._
