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

_Terakhir diperbarui: 2026-09-01 · total sesi: 12_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 23 | 24 | 96% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 23 | 24 | 96% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 21 | 24 | 88% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 24 | 24 | 100% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 26 | 30 | 87% | 🟢 |
| Susun kalimat (★) | `DK-narabekae` | 11 | 13 | 85% | 🟢 |
| Tata bahasa dalam teks (cloze) | `DK-bunshou` | 3 | 4 | 75% | 🟡 |
| Bacaan pendek | `DK-dokkai` | 23 | 24 | 96% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 22 | 24 | 92% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
Mock ke-12 skor **15/15 (100%)** (soal 10 narabekae cacat—duplikat パーティーで di rangka+potongan—dibuang, tak dihitung). Satu-satunya weak: **`DK-bunshou` (文章の文法/cloze) 🟡 75% (3/4)** — kini cukup 3 attempt untuk berstatus. **Kabar baik:** dua rumpang cloze sesi ini benar semua, termasuk **arah pemberian `くれました`** (友達が わたしに 花を〜 → orang lain memberi KE aku) yang jadi error mock lalu, dan penghubung wacana `それから`. Status 🟡 murni karena baseline 1/2 lama; tren naik. Subtipe lain solid & stabil: `MG-ruigi` 100% (24/24), `MG-yomi`/`MG-hyouki` 96%, `DK-dokkai` 96%, `DK-joho` 92%, `MG-bunmyaku` 86%→**88%** (りょこう & けして benar dgn cue konteks), `DK-bunpou` 87%.

**Sinyal:** ⚠️ `DK-bunshou` masih 🟡 — perlu 1–2 mock lagi memuat cloze (penghubung + あげる/くれる/もらう + 指示語) untuk mengangkat ke 🟢. Item 🔴 Anki (先生/友達 kanji, りょこう/けします kosakata) tertangani dalam soal normal. **Rekomendasi:** `/jlpt review` atau mock berikut selipkan ≥1 blok `DK-bunshou`.
