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

_Terakhir diperbarui: 2026-08-31 · total sesi: 11_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 21 | 22 | 95% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 21 | 22 | 95% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 19 | 22 | 86% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 22 | 22 | 100% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 25 | 29 | 86% | 🟢 |
| Susun kalimat (★) | `DK-narabekae` | 11 | 13 | 85% | 🟢 |
| Tata bahasa dalam teks (cloze) | `DK-bunshou` | 1 | 2 | 50% | ⚪ |
| Bacaan pendek | `DK-dokkai` | 21 | 22 | 95% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 20 | 22 | 91% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
_Tak ada subtipe 🔴/🟡 — 7 dari 8 subtipe tetap 🟢. Mock ke-11 skor **15/16 (94%)**. **Baru ada data:** `DK-bunshou` (文章の文法/cloze) diuji perdana → **1/2 50% ⚪** (belum cukup 3 attempt untuk status). Semua subtipe lain naik/stabil: `MG-bunmyaku` 85%→**86%** (りょこう & けします benar dgn cue konteks), `DK-narabekae` 83%→**85%**, `DK-joho` 90%→**91%**, `MG-ruigi` 100%, `MG-yomi`/`MG-hyouki` 95%, `DK-bunpou` 86%, `DK-dokkai` 95%._

**Sinyal yang perlu diperhatikan:**
- ⚠️ **Arah pemberin dalam wacana (`DK-bunshou`)** — satu-satunya error: `友達が わたしに おみやげを（　）` → kunci **くれました** (subjek=orang lain, penerima=わたし → memberい KE aku); user pilih かいました. Di cloze, arah pemberian dikunci alur cerita (siapa subjek/penerima) — refleks あげる↔もらう↔くれる perlu diperkuat. Perlu ≥2 mock lagi memuat `DK-bunshou` untuk memastikan status.
- ✅ **Sisa JLPT tertulis matang** — tak ada subtipe 🔴/🟡; item 🔴 Anki tertangani dalam konteks soal normal.
- **Rekomendasi:** `/jlpt review` atau mock berikut condongkan porsi `DK-bunshou` (kumpulkan attempt) + selipkan pola pemberian あげる/くれる/もらう dalam teks._
