# Evaluasi Mock JLPT N5 (tertulis) — Tracker per Subtipe

Diperbarui otomatis oleh skill `/jlpt` setiap selesai sesi. Melacak akurasi
**per subtipe soal JLPT N5 tertulis** (2 sesi: 文字・語彙 + 文法・読解), lalu
memeringkat **weak types** untuk memandu `/jlpt review`.

> **Terpisah dari `evaluation.md`.** `evaluation.md` = tracker grammar `/quiz` (per
> pola/partikel/lesson) dan **tidak disentuh** oleh `/jlpt`. File ini khusus subtipe
> JLPT. `聴解` (listening) di luar cakupan (butuh audio).

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-08-22 · total sesi: 2_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 4 | 4 | 100% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 4 | 4 | 100% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 4 | 4 | 100% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 4 | 4 | 100% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 3 | 5 | 60% | 🟡 |
| Susun kalimat (★) | `DK-narabekae` | 3 | 3 | 100% | 🟢 |
| Bacaan pendek | `DK-dokkai` | 3 | 4 | 75% | 🟡 |
| Bacaan informasi (info-search) | `DK-joho` | 3 | 4 | 75% | 🟡 |

---

## Weak types (prioritas soal `/jlpt review`)
_Sesi 1 文字・語彙 semua LULUS 🟢 (baca/tulis kanji, kosakata, sinonim). Titik lemah
kini di Sesi 2, terutama `DK-bunpou`._
1. 🟡 **`DK-bunpou` (grammar)** — 60% (3/5). **Turun** dari 100% — kedua error sesi
   2026-08-22 = pola grammar yang memang lemah di `/quiz`: (a) partikel に titik waktu
   (`6時に おきます`, pilih を) & (b) `〜てから` butuh **て-form** (`見て から`, pilih
   辞書形 `見る`). ➜ Arahkan ke **`/quiz review`** (辞書形↔て & partikel に).
2. 🟡 **`DK-dokkai` (bacaan pendek)** — 75% (3/4). Naik dari 50%; sesi ini 2/2 benar.
   Nyaris 🟢.
3. 🟡 **`DK-joho` (info-search)** — 75% (3/4). Naik dari 50%; sesi ini 2/2 benar
   (jam Sabtu & hari libur benar). Nyaris 🟢.

**Catatan sesi 2026-08-22 (mock kedua, 14/16):** Sesi 1 文字・語彙 **8/8 lagi** → keempat
subtipe MG naik 🟢. Sesi 2 **6/8**: bacaan (読解 2/2 + 情報 2/2) **membaik**, tapi dua
error pindah ke **grammar** (`DK-bunpou`) — persis pola lemah `/quiz` (に-waktu & 辞書形↔
て). Bukti kelemahan grammar `/quiz` terbawa ke mock; latih via `/quiz review`.
