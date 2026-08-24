# Evaluasi Mock JLPT N5 (tertulis) — Tracker per Subtipe

Diperbarui otomatis oleh skill `/jlpt` setiap selesai sesi. Melacak akurasi
**per subtipe soal JLPT N5 tertulis** (2 sesi: 文字・語彙 + 文法・読解), lalu
memeringkat **weak types** untuk memandu `/jlpt review`.

> **Terpisah dari `evaluation.md`.** `evaluation.md` = tracker grammar `/quiz` (per
> pola/partikel/lesson) dan **tidak disentuh** oleh `/jlpt`. File ini khusus subtipe
> JLPT. `聴解` (listening) di luar cakupan (butuh audio).

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-08-24 · total sesi: 4_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 7 | 8 | 88% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 7 | 8 | 88% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 7 | 8 | 88% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 8 | 8 | 100% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 9 | 11 | 82% | 🟢 |
| Susun kalimat (★) | `DK-narabekae` | 4 | 5 | 80% | 🟢 |
| Bacaan pendek | `DK-dokkai` | 7 | 8 | 88% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 7 | 8 | 88% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
_Sesi 2026-08-24 (mock keempat, **13/16 = 81%**): **SEMUA 8 subtipe kini 🟢** — `DK-bunpou`
naik 75%→**82% (🟡→🟢)** lewat 3/3 (たり/てから/なければなりません). Tak ada 🔴/🟡 lagi.
3 error tersebar & bukan pola grammar: 1 susun kalimat (salah hitung posisi ★), 2 kosakata
文字語彙 (bacaan jukujikun 時計, pasangan つけます↔けします)._
1. ⚠️ **`DK-narabekae` (susun kalimat)** — 80% (4/5), subtipe akurasi TERENDAH walau 🟢.
   Error soal 12: susun 〜まえに (`ねる まえに 本 を よみます`) → salah tunjuk isi ★③
   (jawab `を`, kunci `本`). **Sebagian karena PENYAJIAN PANEL** — panel klik hanya
   menaruh potongan dipisah `/` tanpa mengulang rangka slot `[①][②][★③][④]`, jadi user
   bingung memetakan (bukan murni tak paham pola まえに). Perbaikan format panel dicatat
   di memory [[quiz-susun-kalimat-format]]. **Bukan kelemahan grammar.**

**Sinyal yang perlu diperhatikan:**
- ✅ **`DK-bunpou` tembus 🟢 (82%)** — 3/3 sesi ini: 〜たり (`聞いたり`), 〜てから (`から`),
  〜なければなりません (stem ない `べんきょうし`). Grammar bukan lagi kelemahan; ekor data
  🟡 lama (に-waktu, 辞書形↔て) tuntas terkejar.
- ✅ **Sesi 2 (文法・読解) 7/8** — hanya 1 error susun kalimat; bacaan `DK-dokkai` &
  `DK-joho` 2/2 lagi (keduanya 88%). Pemahaman bacaan stabil.
- 🔺 **文字語彙 error = kosakata, bukan tulisan-mirip.** (1) 時計 dibaca `じけい` — lupa
  bacaan **jukujikun と**(時→と, bukan じ seperti 何時). (2) `つけます`↔`けします` tertukar
  ("keluar kamar → matikan lampu" = 消します). Pasangan lawan-arti (つける↔けす,
  あける↔しめる) & bacaan istimewa (時計/今日/明日) layak diwaspadai. MG-hyouki 2/2 —
  gap 聞 vs 間 mock lalu **beres** (`新聞` benar).
- **Sesi 2026-08-24 (mock keempat) skor 13/16 (81%)** — turun dari 94% karena 3 error
  "kecil" (kosakata + hitung ★), tapi **semua subtipe kini 🟢** untuk pertama kalinya.
