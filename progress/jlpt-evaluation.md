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

_Terakhir diperbarui: 2026-09-03 · total sesi: 14_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 27 | 28 | 96% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 27 | 28 | 96% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 25 | 28 | 89% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 28 | 28 | 100% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 28 | 32 | 88% | 🟢 |
| Susun kalimat (★) | `DK-narabekae` | 13 | 15 | 87% | 🟢 |
| Tata bahasa dalam teks (cloze) | `DK-bunshou` | 7 | 8 | 88% | 🟢 |
| Bacaan pendek | `DK-dokkai` | 27 | 28 | 96% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 25 | 28 | 89% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
🎉 **Tidak ada 🔴 maupun 🟡** — semua subtipe JLPT tetap 🟢. Mock 2026-09-03 skor **15/16 (94%)**, Sesi 1 sempurna **8/8**. Satu miss di **`DK-joho` 25/28 (89%)** — soal diskon ランチ (カレー ８００円 − １００円 = ７００円) dijawab ９００円, arah hitung terbalik (menambah, bukan mengurangi diskon); bukan salah baca info, murni operasi hitung. Subtipe lain stabil: `MG-ruigi` 100% (28/28), `MG-yomi`/`MG-hyouki`/`DK-dokkai` 96%, `MG-bunmyaku` 89% (つけて & りょこう benar dgn cue), `DK-bunpou` 88%, `DK-bunshou` naik **83%→88% (7/8)** (だから sebab-akibat & くれました arah pemberian dua-duanya benar), `DK-narabekae` 87%. **Sinyal:** tak ada kelemahan pola/subtipe tersisa; miss `DK-joho` = ketelitian hitung, bukan pemahaman baca. **Rekomendasi:** lanjut mock berkala (lawan decay); di `DK-joho` sisipkan sesekali soal berhitung (diskon/kembalian/total) agar operasi tambah↔kurang makin refleks. Rotasi tema jaga hindari masak/menu-restoran/buku-harian di mock berikut.
