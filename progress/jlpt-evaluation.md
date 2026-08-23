# Evaluasi Mock JLPT N5 (tertulis) — Tracker per Subtipe

Diperbarui otomatis oleh skill `/jlpt` setiap selesai sesi. Melacak akurasi
**per subtipe soal JLPT N5 tertulis** (2 sesi: 文字・語彙 + 文法・読解), lalu
memeringkat **weak types** untuk memandu `/jlpt review`.

> **Terpisah dari `evaluation.md`.** `evaluation.md` = tracker grammar `/quiz` (per
> pola/partikel/lesson) dan **tidak disentuh** oleh `/jlpt`. File ini khusus subtipe
> JLPT. `聴解` (listening) di luar cakupan (butuh audio).

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-08-23 · total sesi: 3_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 6 | 6 | 100% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 5 | 6 | 83% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 6 | 6 | 100% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 6 | 6 | 100% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 6 | 8 | 75% | 🟡 |
| Susun kalimat (★) | `DK-narabekae` | 4 | 4 | 100% | 🟢 |
| Bacaan pendek | `DK-dokkai` | 5 | 6 | 83% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 5 | 6 | 83% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
_Sesi 2026-08-23 (mock ketiga, **15/16 = 94%**): Sesi 2 **8/8 SEMPURNA** — `DK-bunpou`
membaik (semua grammar benar: たことがあります/てください/なります+に), `DK-dokkai` &
`DK-joho` tembus 🟢. Kelemahan grammar `/quiz` lama (辞書形↔て, に) **tidak lagi terbawa**
ke mock (sudah 🟢 di /quiz). Satu-satunya error = 1 penulisan kanji mirip._
1. 🟡 **`DK-bunpou` (grammar)** — 75% (6/8). Naik dari 60%. Sesi ini **3/3 benar**
   (`こと`, `そうじして`, `に`); defisit tinggal ekor data lama (に-waktu & 辞書形↔て 2 mock
   lalu). Nyaris 🟢 — sudah bukan kelemahan aktif.

**Sinyal yang perlu diperhatikan:**
- ✅ **Sesi 2 (文法・読解) 8/8** — grammar solid: てください pakai て (`そうじして`),
  たことがあります (`こと`), なります+に (`に`), susun まえに benar. Kelemahan grammar `/quiz`
  yang dulu terbawa (に-waktu, 辞書形↔て) kini teratasi karena sudah 🟢 di `evaluation.md`.
- ✅ **読解 & 情報検索 tembus 🟢** (83%) — 2/2 lagi berturut; pemahaman bacaan stabil.
- 🔺 **Kanji bentuk mirip (MG-hyouki)** — 1 error: `新聞` ditulis `新間`. Akar: **聞**（ぶん,
  "berita/dengar") vs **間**（ま/あいだ, "sela/antara") bentuknya mirip (門 + 耳 vs 門 + 日).
  MG-hyouki tetap 🟢 (83%); waspadai pasangan kanji-mirip saat drill penulisan.
- **Sesi 2026-08-23 (mock ketiga) skor 15/16 (94%)** — 1 salah = penulisan kanji mirip
  (bukan grammar/bacaan). Mock terbaik sejauh ini.
