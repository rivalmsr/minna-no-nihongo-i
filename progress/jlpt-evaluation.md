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

_Terakhir diperbarui: 2026-09-09 · total sesi: 21_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 41 | 42 | 98% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 39 | 42 | 93% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 36 | 42 | 86% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 40 | 42 | 95% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 33 | 39 | 85% | 🟢 |
| Susun kalimat (★) | `DK-narabekae` | 20 | 22 | 91% | 🟢 |
| Tata bahasa dalam teks (cloze) | `DK-bunshou` | 19 | 22 | 86% | 🟢 |
| Bacaan pendek | `DK-dokkai` | 41 | 42 | 98% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 39 | 42 | 93% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
Semua sembilan subtipe tetap 🟢. Mock 2026-09-09 13/16 (81%): Sesi 1 文字・語彙 8/8 SEMPURNA (yomi 時間/電車, hyouki 友達/大きい, bunmyaku つけます/なくします cue-lock jalan, ruigi やすい=値段たかくない & 有名=みんな知っている), semua miss terkonsentrasi di Sesi 2 (5/8). Tiga miss: (1) DK-bunpou てから — 'あさごはんを たべて（）、でかけます' dijawab あとで, padahal あとで butuh 辞書形/た (たべた あとで); rangkaian て+から = 'setelah…baru' → から belum terkunci; (2) DK-bunshou penghubung — 'pesta ulang tahun（）kamu juga datang yuk' dijawab でも (kontras), konteksnya sebab-akibat/ajakan → だから; arah wacana belum dibaca; (3) DK-bunshou sebab — 'ada banyak masakan enak（）menantikan' dijawab まで, cue sebab → から. DK-bunshou anjlok 95%→86% (dua miss cloze sekaligus), DK-bunpou turun 87%→85% jadi subtipe terlemah teratas. Q10 並べ替え di-OVERRIDE benar: たり simetris (ほんを よんだり テレビを みたり juga urutan sah) → ★③ punya dua jawaban valid; soal rancu, bukan kesalahan user. Sisa Sesi 2 kokoh: DK-narabekae 91%, DK-dokkai 2/2 (belanja+resto), DK-joho 2/2 (menu 千円 & diskon lunch 七百円). Angka: MG-yomi 98%, MG-hyouki 93%, MG-bunmyaku 86%, MG-ruigi 95%, DK-bunpou 85%, DK-narabekae 91%, DK-bunshou 86%, DK-dokkai 98%, DK-joho 93% — semua 🟢. Rekomendasi: latih penghubung wacana (だから/でも/それから/から-sebab) di teks cloze + bedakan てから (bentuk て) vs た+あとで. Rotasi tema mock berikut: hindari belanja-akhirpekan / menu-restoran / surat-teman-ultah; jaga cue-lock 文脈規定 tetap tajam.
