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

_Terakhir diperbarui: 2026-09-07 · total sesi: 18_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 35 | 36 | 97% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 33 | 36 | 92% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 32 | 36 | 89% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 35 | 36 | 97% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 31 | 36 | 86% | 🟢 |
| Susun kalimat (★) | `DK-narabekae` | 17 | 19 | 89% | 🟢 |
| Tata bahasa dalam teks (cloze) | `DK-bunshou` | 15 | 16 | 94% | 🟢 |
| Bacaan pendek | `DK-dokkai` | 35 | 36 | 97% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 33 | 36 | 92% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
**Tak ada 🔴/🟡 — sembilan subtipe tetap 🟢.** Mock 2026-09-07 skor **15/16 (94%)**: Sesi 1 **7/8**, Sesi 2 **8/8** (sempurna). Miss tunggal: **MG-hyouki** 94%→**92%** (tetap 🟢) — 「やすみ」ditulis **体み** padahal 休み; user tertukar bentuk mirip 休（yasumu, radikal 亻+木）vs 体（karada）. Kesalahan diskriminasi radikal bentuk-mirip, bukan kelemahan subtipe. **Sinyal positif kuat:** seluruh Sesi 2 8/8 — DK-bunpou (L16-に-naik のります), DK-narabekae (L18-ことができます susun benar), DK-bunshou 2/2 (それから penghubung + あげました arah pemberian aku→妹), DK-dokkai 2/2 & DK-joho 2/2 (info-search harga & jam) → wacana, grammar-in-teks, dan pencarian info kokoh. MG-yomi/ruigi 97%, MG-bunmyaku naik ke 89% (けして・なくして benar). **Rekomendasi:** lanjut mock berkala lawan decay; sesekali sisipkan MG-hyouki pasangan radikal bentuk-mirip (休↔体, 大↔太↔犬↔天, 木↔本) agar diskriminasi bentuk makin refleks. Rotasi tema mock berikut: hindari keluarga-akhirpekan / menu-restoran / buku-harian-belanja.
