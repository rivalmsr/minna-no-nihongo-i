# Evaluasi Mock JLPT N5 (tertulis) — Tracker per Subtipe

Diperbarui otomatis oleh skill `/jlpt` setiap selesai sesi. Melacak akurasi
**per subtipe soal JLPT N5 tertulis** (2 sesi: 文字・語彙 + 文法・読解), lalu
memeringkat **weak types** untuk memandu `/jlpt review`.

> **Terpisah dari `evaluation.md`.** `evaluation.md` = tracker grammar `/quiz` (per
> pola/partikel/lesson) dan **tidak disentuh** oleh `/jlpt`. File ini khusus subtipe
> JLPT. `聴解` (listening) di luar cakupan (butuh audio).

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-08-28 · total sesi: 8_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 15 | 16 | 94% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 15 | 16 | 94% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 14 | 16 | 88% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 16 | 16 | 100% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 19 | 23 | 83% | 🟢 |
| Susun kalimat (★) | `DK-narabekae` | 7 | 9 | 78% | 🟡 |
| Bacaan pendek | `DK-dokkai` | 15 | 16 | 94% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 14 | 16 | 88% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
_Sesi 2026-08-28 (mock kedelapan, **14/16 = 88%**): Sesi 1 文字・語彙 **8/8 SEMPURNA** (kanji 🔴
先生/時計=とけい/友達 ✓, kosakata 🔴 でかけます/つくります ✓, ruigi やすい=ねだんたかくない / 両親=
父と母 ✓). Sesi 2 6/8. 🎉 **Dua celah 🟡 `/quiz` TUTUP di mock ini:** soal 9 **のりかえる+に** ✓
(bukan を) & soal 10 **はたらく+で** ✓ (bukan に) — pasangan partikel はたらく/つとめる yang jadi
lubang mock ke-7 kini benar. はじまる (自動詞) ✓. **2 salah:** soal 12 **`DK-narabekae`** (posisi
ます-stem: `図書館へ 本を かり に 行きます`, ★③=かり dijawab に) → narabekae turun 88%→🟡 78%;
soal 16 **`DK-joho`** (salah baca baris やすみ: 水よう日 dijawab 月よう日 — kurang teliti, bukan
grammar)._
1. 🟡 **`DK-narabekae` (78%, 7/9)** — soal 12: keliru posisi **ます-stem + に 行きます** (pilih に,
   kunci かり/stem). Pola L13 `[tempat]へ [objek]を [stem]に 行きます` — stem sebelum に. Perlu
   didrill lagi (rangka slot membantu; jangan bocorkan urutan di panel).

**Sinyal yang perlu diperhatikan:**
- 🎉 **Pasangan partikel はたらく(で)↔つとめる(に) & のりかえる(に) TUTUP di JLPT** — lubang mock ke-7
  kini benar, sejalan dgn `/quiz` yang juga menaikkan L15/L16. Refleks partikel membaik.
- ✅ **Sesi 1 文字・語彙 SEMPURNA tiga mock beruntun** — kanji/kosakata 🔴 & sinonim konsisten. Bias 🔴 solid.
- 🔺 **Fokus tersisa = `DK-narabekae` (susun kalimat)** — spesifik ke posisi ます-stem dalam pola
  stem+に行きます. Satu-satunya subtipe 🟡; selebihnya 🟢 83–100%. Soal 16 (joho) miss = ketelitian,
  bukan pola — pantau saja, tak perlu drill khusus.
- **Rekomendasi:** JLPT tetap sangat matang (88% mock ini, 7 dari 8 subtipe 🟢). Drill sisa 🟡 lewat
  `/jlpt review` atau `/quiz` (pola `L13-に-tujuan` dalam format susun kalimat). Grammar `/quiz` masih
  punya 🟡 L16-に-naik/自他 & L15 untuk dikonfirmasi lagi.
- **Sesi 2026-08-28 (mock kedelapan) skor 14/16 (88%)** — sedikit turun dari 94% karena narabekae +
  ketelitian joho; tapi pasangan partikel はたらく/つとめる/のりかえる yang kronis kini tuntas.
