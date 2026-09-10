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

_Terakhir diperbarui: 2026-09-10 · total sesi: 22_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 43 | 44 | 98% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 41 | 44 | 93% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 38 | 44 | 86% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 42 | 44 | 95% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 34 | 40 | 85% | 🟢 |
| Susun kalimat (★) | `DK-narabekae` | 21 | 23 | 91% | 🟢 |
| Tata bahasa dalam teks (cloze) | `DK-bunshou` | 21 | 24 | 88% | 🟢 |
| Bacaan pendek | `DK-dokkai` | 43 | 44 | 98% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 41 | 44 | 93% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
**Mock sempurna 16/16 — tak ada subtipe 🔴/🟡, semua tetap 🟢 & naik.** Sorotan: dua subtipe terlemah bulan lalu justru terangkat lewat soal yang dirancang menyasar kelemahannya. (1) **DK-bunshou** (cloze wacana): kedua rumpang benar — （１）だから (sebab-akibat: banyak belajar→capek, bukan でも/それから) & （２）くれて (teman が subjek membeli KE aku → くれる, bukan あげる/もらう). Ini persis dua jenis miss mock 2026-09-09 (でも salah pilih & arah pemberian) — kini terbaca benar. (2) **DK-bunpou** ことができます (辞書形+こと) ✓. (3) **DK-narabekae** 寝るまえに歯を みがきます, ★③=歯 ✓ (辞書形+まえに). Sesi 1 mulus: yomi 午後/新聞 (bacaan panjang/dakuten benar), hyouki 東 (bukan look-alike 束/車/重), bunmyaku cue-lock tajam (寝る前+電気→けします; 沖縄へ→りょこう). ruigi まずい=おいしくない, りょうしん=父と母. **Tak ada kelemahan baru.** Rekomendasi: pertahankan; mock berikut rotasi tema (hindari hobi-olahraga / jam-buka-toko / diary-belajar) & sentuh subtipe yang porsinya tipis di mock ini (bunpou/narabekae cuma 1 soal masing-masing) — atau pakai /jlpt bunpou untuk porsi grammar lebih besar.
