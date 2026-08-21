# Evaluasi Mock JLPT N5 (tertulis) — Tracker per Subtipe

Diperbarui otomatis oleh skill `/jlpt` setiap selesai sesi. Melacak akurasi
**per subtipe soal JLPT N5 tertulis** (2 sesi: 文字・語彙 + 文法・読解), lalu
memeringkat **weak types** untuk memandu `/jlpt review`.

> **Terpisah dari `evaluation.md`.** `evaluation.md` = tracker grammar `/quiz` (per
> pola/partikel/lesson) dan **tidak disentuh** oleh `/jlpt`. File ini khusus subtipe
> JLPT. `聴解` (listening) di luar cakupan (butuh audio).

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-08-21 · total sesi: 1_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 2 | 2 | 100% | ⚪ |
| Tulis kanji (penulisan) | `MG-hyouki` | 2 | 2 | 100% | ⚪ |
| Kosakata dalam konteks | `MG-bunmyaku` | 2 | 2 | 100% | ⚪ |
| Sinonim / 言い換え類義 | `MG-ruigi` | 2 | 2 | 100% | ⚪ |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 2 | 2 | 100% | ⚪ |
| Susun kalimat (★) | `DK-narabekae` | 2 | 2 | 100% | ⚪ |
| Bacaan pendek | `DK-dokkai` | 1 | 2 | 50% | ⚪ |
| Bacaan informasi (info-search) | `DK-joho` | 1 | 2 | 50% | ⚪ |

---

## Weak types (prioritas soal `/jlpt review`)
_Semua subtipe masih ⚪ (Total < 3 attempt) — status resmi belum dihitung. Sinyal awal:_
1. ⚪ **`DK-dokkai` (bacaan pendek)** — 50% (1/2). Salah "menyalin" info dari teks
   (公園 tertukar 学校). Butuh ≥3 attempt untuk status pasti.
2. ⚪ **`DK-joho` (info-search)** — 50% (1/2). Salah baca detail angka (5冊 → 10冊).
   Latih cari kata kunci langsung di teks.

**Catatan sesi 2026-08-21 (mock pertama, 14/16):** Sesi 1 文字・語彙 **8/8** — baca/tulis
kanji, kosakata, sinonim semua kuat. Sesi 2 grammar & susun kalimat **4/4**; dua error
keduanya di **bacaan** (读解/情報検索), bukan tata bahasa.
