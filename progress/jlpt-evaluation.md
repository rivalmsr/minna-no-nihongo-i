# Evaluasi Mock JLPT N5 (tertulis) — Tracker per Subtipe

Diperbarui otomatis oleh skill `/jlpt` setiap selesai sesi. Melacak akurasi
**per subtipe soal JLPT N5 tertulis** (2 sesi: 文字・語彙 + 文法・読解), lalu
memeringkat **weak types** untuk memandu `/jlpt review`.

> **Terpisah dari `evaluation.md`.** `evaluation.md` = tracker grammar `/quiz` (per
> pola/partikel/lesson) dan **tidak disentuh** oleh `/jlpt`. File ini khusus subtipe
> JLPT. `聴解` (listening) di luar cakupan (butuh audio).

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-08-27 · total sesi: 7_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 13 | 14 | 93% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 13 | 14 | 93% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 12 | 14 | 86% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 14 | 14 | 100% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 16 | 20 | 80% | 🟢 |
| Susun kalimat (★) | `DK-narabekae` | 7 | 8 | 88% | 🟢 |
| Bacaan pendek | `DK-dokkai` | 13 | 14 | 93% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 13 | 14 | 93% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
_Sesi 2026-08-27 (mock ketujuh, **15/16 = 94%**): **SEMUA 8 subtipe tetap 🟢.** Sesi 1
文字・語彙 **8/8 SEMPURNA** lagi (kanji 🔴 先生/時計=とけい ✓, つける benar `でんきを つけます`
cue gelap→nyalakan). Satu-satunya error = Sesi 2 soal 10: **`はたらく` partikel** (「スーパー
（　）はたらいて います」pilih に, harusnya で). 🎉 **`まえに↔てから` (soal 9) AKHIRNYA BENAR** —
lubang kronis mock ke-6 kini tertutup. Subtipe terendah bergeser ke `DK-bunpou` 80% —
ditarik miss はたらく+で._
1. ⚠️ **`はたらく` (で) ↔ `つとめる` (に) tertukar** — soal 10, pilih に. Dua verba "bekerja di",
   partikel beda: **はたらく + で** (tempat aktivitas: スーパー**で**), **つとめる + に** (melekat ke
   instansi: かいしゃ**に**). Ini **cermin** dari 🟡 `/quiz` `L15-に-vs-で-statis` (dulu keliru
   つとめる+で; kini keliru はたらく+に) — pola yang sama dilihat dari sisi berlawanan. Jangkar:
   はたらく=で (aktivitas), つとめる=に (menempel instansi). Sisipkan lagi di `DK-bunpou`/`/quiz`.
2. 🎉 **`まえに↔てから` TUTUP** — benar di mock ini setelah salah di mock ke-6. Bentuk sambung
   (辞書形+まえに "sebelum" ↔ て形+てから "setelah") kini dibedakan. Pantau sekali lagi untuk
   konfirmasi.

**Sinyal yang perlu diperhatikan:**
- 🎉 **まえに↔てから TUTUP** — pasangan waktu kronis mock lalu kini benar. Bersamaan dgn `/quiz`
  yang juga menutup てから↔あとで, trio まえに/てから/あとで matang.
- ✅ **Sesi 1 文字・語彙 SEMPURNA dua mock beruntun** — kanji 🔴 & つける konsisten. Bias 🔴 solid.
- 🔺 **Fokus tersisa = pasangan partikel `はたらく で ↔ つとめる に`** — mirip ciri titik lemah user
  (dua verb sekelas, partikel beda). Sempit & spesifik; identik dengan 🟡 `/quiz` L15. Selebihnya matang.
- **Rekomendasi:** JLPT sangat matang (94% tiga mock beruntun, semua subtipe 🟢). Sisa lubang
  tipis = `はたらく+で ↔ つとめる+に`. Drill via `/quiz review` (target `L15-に-vs-で-statis`) atau
  `/jlpt review`. Grammar `/quiz` juga masih punya 🟡 L4-jam (7時=しちじ) untuk dikonfirmasi.
- **Sesi 2026-08-27 (mock ketujuh) skor 15/16 (94%)** — level tertinggi bertahan; lubang bergeser
  dari pasangan waktu (tutup) ke pasangan partikel はたらく/つとめる.
