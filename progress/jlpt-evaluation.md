# Evaluasi Mock JLPT N5 (tertulis) — Tracker per Subtipe

Diperbarui otomatis oleh skill `/jlpt` setiap selesai sesi. Melacak akurasi
**per subtipe soal JLPT N5 tertulis** (2 sesi: 文字・語彙 + 文法・読解), lalu
memeringkat **weak types** untuk memandu `/jlpt review`.

> **Terpisah dari `evaluation.md`.** `evaluation.md` = tracker grammar `/quiz` (per
> pola/partikel/lesson) dan **tidak disentuh** oleh `/jlpt`. File ini khusus subtipe
> JLPT. `聴解` (listening) di luar cakupan (butuh audio).

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-08-25 · total sesi: 5_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 9 | 10 | 90% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 9 | 10 | 90% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 8 | 10 | 80% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 10 | 10 | 100% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 12 | 14 | 86% | 🟢 |
| Susun kalimat (★) | `DK-narabekae` | 5 | 6 | 83% | 🟢 |
| Bacaan pendek | `DK-dokkai` | 9 | 10 | 90% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 9 | 10 | 90% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
_Sesi 2026-08-25 (mock kelima, **15/16 = 94%**): **SEMUA 8 subtipe tetap 🟢.** Sesi 2
文法・読解 **8/8 SEMPURNA** (DK-bunpou 3/3, narabekae まえに benar, dokkai+joho 4/4). Satu-
satunya error = Sesi 1 soal 5: **つける↔けす lagi** (「へやが くらい→でんきを つけて」pilih けして,
KEBALIKAN). Subtipe akurasi terendah kini **`MG-bunmyaku` 80%** — ditarik turun justru oleh
pasangan lawan-arti ini, bukan kosakata acak._
1. ⚠️ **Pasangan lawan-arti `つける↔けす` = kelemahan KRONIS** (bukan sekadar subtipe). Salah
   di mock ke-4 (matikan lampu) DAN ke-5 (nyalakan lampu) — selalu tertukar arah. Keduanya
   **🔴 leech Anki**. Jangkar: `つける`=ON (nyalakan/pasang), `けす`=OFF (matikan/hapus).
   Waspadai juga pasangan `あける↔しめる`, `はじまる↔おわる`. Ini menyeret `MG-bunmyaku` → 80%.
2. ⚠️ **`DK-narabekae`** — 83% (5/6) **TAK RELIABEL**: soal 12 (まえに) tercatat benar tapi
   panel **membocorkan jawaban** (urutan kalimat di `question` + posisi "★③" di
   `description`), jadi bukan bukti paham urutan. Aturan anti-bocor sudah ditambahkan
   (lihat log 2026-08-25 & [[quiz-susun-kalimat-format]]). Uji ulang tanpa hint di sesi
   berikutnya untuk skor jujur. Tetap subtipe kedua-terendah; data tipis.

**Sinyal yang perlu diperhatikan:**
- ✅ **Sesi 2 (文法・読解) 8/8 SEMPURNA** — DK-bunpou 3/3 (で aktivitas, いった たことがあります,
  さむく なります い→く), narabekae まえに benar, dokkai & joho 2/2. Grammar & bacaan solid.
- ✅ **Kanji 🔴 Anki tuntas** — 先生/時計/東/北 semua benar; **jukujikun 時計=とけい benar**
  (mock lalu salah `じけい`). Bias kanji 🔴 berhasil menutup gap bacaan istimewa.
- 🔺 **Fokus TUNGGAL tersisa = pasangan verb lawan-arti** (つける↔けす dst.), bukan grammar,
  bukan tulisan-mirip, bukan bacaan. Sempit & spesifik.
- **Rekomendasi:** grammar/bacaan JLPT sudah matang (Sesi 2 sempurna 2 sesi beruntun bila
  dihitung DK-bunpou). Yang berbuah sekarang: **drill pasangan verb lawan-arti** — lewat
  Anki (keduanya sudah 🔴) atau `/quiz` yang menyisipkan つける/けす/あける/しめる di pola in-scope.
- **Sesi 2026-08-25 (mock kelima) skor 15/16 (94%)** — kembali ke level tertinggi; satu-
  satunya lubang = pasangan lawan-arti つける↔けす.
