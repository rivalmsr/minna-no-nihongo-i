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

_Terakhir diperbarui: 2026-09-08 · total sesi: 20_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 39 | 40 | 98% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 37 | 40 | 93% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 34 | 40 | 85% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 38 | 40 | 95% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 33 | 38 | 87% | 🟢 |
| Susun kalimat (★) | `DK-narabekae` | 19 | 21 | 90% | 🟢 |
| Tata bahasa dalam teks (cloze) | `DK-bunshou` | 19 | 20 | 95% | 🟢 |
| Bacaan pendek | `DK-dokkai` | 39 | 40 | 98% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 37 | 40 | 93% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
**Semua sembilan subtipe tetap 🟢** — mock 2026-09-08 **13/16 (81%)**: Sesi 2 **8/8 sempurna**, semua kekeliruan terkonsentrasi di **Sesi 1 文字・語彙 (5/8)**. Tiga miss: (1) **MG-bunmyaku げんきん** — soal 'bayar tanpa kartu → ___' dijawab きっぷ (karcis), cue 'カードを つかわないで' menutup ke uang tunai; (2) **MG-bunmyaku もらいます** — 'dapat hadiah dari teman' dijawab つくりました, arah から→もらう belum terkunci (item 🔴 Anki, konsisten sulit); (3) **MG-ruigi むずかしい⇄かんたんじゃない** — dijawab かんたんです (justru antonim), belum menangkap negasi parafrase. **MG-bunmyaku turun 89%→85%** (dua miss sekaligus) jadi subtipe terlemah teratas, diikuti **DK-bunpou 87%**. Sesi 2 kokoh: DK-bunpou (て+てもいいです, とって), DK-narabekae (辞書形 diksusun betul: ふじさんに のぼった ことが あります = たことがあります), DK-bunshou 2/2 (でも kontras + あげます arah わたし→母), DK-dokkai 2/2 & DK-joho 2/2 (harga otona 千五百円 & hari libur 木曜日). **Angka:** MG-yomi 98%, MG-hyouki 93%, MG-bunmyaku 85%, MG-ruigi 95%, DK-bunpou 87%, DK-narabekae 90%, DK-bunshou 95%, DK-dokkai 98%, DK-joho 93% — semua 🟢. **Rekomendasi:** fokus 文脈規定 — latih cue-locking (kartu/tunai, から→もらう vs あげる) & parafrase negasi (むずかしい=かんたんじゃない, bukan かんたん). Rotasi tema mock berikut: hindari hobi-suiei / jadwal-bioskop / keluarga-masak; teruskan bentuk-mirip 表記 (大↔太↔犬↔天).
