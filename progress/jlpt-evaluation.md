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

_Terakhir diperbarui: 2026-09-11 · total sesi: 23_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 45 | 46 | 98% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 43 | 46 | 93% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 40 | 46 | 87% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 44 | 46 | 96% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 35 | 41 | 85% | 🟢 |
| Susun kalimat (★) | `DK-narabekae` | 22 | 24 | 92% | 🟢 |
| Tata bahasa dalam teks (cloze) | `DK-bunshou` | 22 | 26 | 85% | 🟢 |
| Bacaan pendek | `DK-dokkai` | 45 | 46 | 98% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 43 | 46 | 93% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
Mock 15/16 (94%) — semua subtipe tetap 🟢, tak ada 🔴/🟡. Satu miss di **DK-bunshou** (指示語): rumpang（２）harusnya その ごはん (merujuk ごはん yang BARU disebut di kalimat sebelumnya = kata tunjuk 'itu' untuk hal yang baru muncul di wacana), dipilih この (この = benda yang secara fisik dekat pembicara SEKARANG, bukan yang baru disebut dalam teks). DK-bunshou turun tipis 88%→85% tapi masih 🟢 — pola miss = rujukan kata tunjuk dalam wacana, mirip jenis kelemahan cloze sebelumnya (connector/arah pemberian). Sisanya mulus: Sesi 1 sempurna 8/8 (yomi 会社/手紙, hyouki 学校/山 look-alike, bunmyaku から+プレゼント→もらう & 朝ルーティン→たべる cue-lock, ruigi やさしい=かんたん・つまらない=おもしろくない); Sesi 2 DK-bunpou でかけて (て+ください) ✓, narabekae ★③=あびて (て-rangkaian pagi→行きます) ✓, dokkai keluarga 2/2, joho menu 2/2 (800円 & 400+300−100=600円 hitung diskon). Rekomendasi: sentuh 指示語 (この・その・あの・どの) dalam wacana di mock/latihan berikut untuk mengunci その='baru disebut'.
