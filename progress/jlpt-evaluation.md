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

_Terakhir diperbarui: 2026-09-02 · total sesi: 13_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 25 | 26 | 96% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 25 | 26 | 96% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 23 | 26 | 88% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 26 | 26 | 100% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 27 | 31 | 87% | 🟢 |
| Susun kalimat (★) | `DK-narabekae` | 12 | 14 | 86% | 🟢 |
| Tata bahasa dalam teks (cloze) | `DK-bunshou` | 5 | 6 | 83% | 🟢 |
| Bacaan pendek | `DK-dokkai` | 25 | 26 | 96% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 24 | 26 | 92% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
🎉 **Tidak ada 🔴 maupun 🟡** — semua subtipe JLPT 🟢. Mock 2026-09-02 skor **16/16 (100%)**. **Tonggak:** `DK-bunshou` (文章の文法/cloze) yang jadi satu-satunya weak (🟡 75%) kini **🟡→🟢 83% (5/6)** — dua rumpang sesi ini benar semua: penghubung pertentangan `でも` (山の上さむい↔けしききれい) & arah pemberian `くれました` (友達が わたしに お茶を → orang lain memberi KE aku). Ini pola yang dulu sering keliru, sekarang mantap. Subtipe lain stabil tinggi: `MG-ruigi` 100% (26/26), `MG-yomi`/`MG-hyouki` 96%, `DK-dokkai` 96%, `DK-joho` 92%, `MG-bunmyaku` 88% (つけます & りょこう benar dgn cue konteks), `DK-narabekae` 86%, `DK-bunpou` 87%. **Sinyal:** tak ada kelemahan tersisa — semua ≥83%. **Rekomendasi:** lanjut mock penuh berkala (lawan decay); tema teks terus dirotasi (avoid belanja/bus/ulang-tahun & sekolah/toko/gunung di mock berikut).
