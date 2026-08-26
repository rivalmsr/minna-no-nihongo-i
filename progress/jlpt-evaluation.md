# Evaluasi Mock JLPT N5 (tertulis) — Tracker per Subtipe

Diperbarui otomatis oleh skill `/jlpt` setiap selesai sesi. Melacak akurasi
**per subtipe soal JLPT N5 tertulis** (2 sesi: 文字・語彙 + 文法・読解), lalu
memeringkat **weak types** untuk memandu `/jlpt review`.

> **Terpisah dari `evaluation.md`.** `evaluation.md` = tracker grammar `/quiz` (per
> pola/partikel/lesson) dan **tidak disentuh** oleh `/jlpt`. File ini khusus subtipe
> JLPT. `聴解` (listening) di luar cakupan (butuh audio).

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-08-26 · total sesi: 6_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 11 | 12 | 92% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 11 | 12 | 92% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 10 | 12 | 83% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 12 | 12 | 100% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 14 | 17 | 82% | 🟢 |
| Susun kalimat (★) | `DK-narabekae` | 6 | 7 | 86% | 🟢 |
| Bacaan pendek | `DK-dokkai` | 11 | 12 | 92% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 11 | 12 | 92% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
_Sesi 2026-08-26 (mock keenam, **15/16 = 94%**): **SEMUA 8 subtipe tetap 🟢.** Sesi 1
文字・語彙 **8/8 SEMPURNA** — termasuk **つける↔けす AKHIRNYA BENAR** (`エアコンを つけます`, cue
panas→nyalakan): kelemahan kronis 2 mock beruntun kini tertutup. Juga jukujikun 時計=とけい ✓,
kanji 🔴 先生/友達/東 ✓. Satu-satunya error = Sesi 2 soal 9: **`まえに`↔`てから`** (「ねる（　）
はを みがきます」pilih てから, harusnya まえに = "sebelum"). Subtipe terendah kini `DK-bunpou`
82% — ditarik oleh miss まえに ini._
1. ⚠️ **`まえに` (sebelum) ↔ `てから` (setelah) tertukar** — soal 9. Bukan cuma makna
   berlawanan, tapi **bentuk sambung beda**: `まえに` butuh **辞書形** (ねる**まえに**), `てから`
   butuh **て形** (寝**てから**). Jangkar: 辞書形+まえに = "SEBELUM"; て形+てから = "SETELAH, baru".
   Sisipkan lagi di `DK-bunpou`/`/quiz` (L16-てから vs L18-まえに).
2. ✅ **`DK-narabekae` kini RELIABEL** — 86% (6/7). Soal 12 diuji ULANG **tanpa bocoran panel**
   (rule anti-leak diterapkan: tak ada urutan di `question`, `description` kosong) → **tetap
   benar** (`かいもの`, pola stem+に行きます). Skor susun kalimat sekarang jujur. Keluar dari
   daftar "tak reliabel".

**Sinyal yang perlu diperhatikan:**
- 🎉 **つける↔けす TUTUP** — benar di mock ini setelah salah 2× beruntun. Pasangan lawan-arti
  kronis akhirnya terkunci (cue konteks membantu). Pantau sekali lagi untuk konfirmasi.
- ✅ **Kanji 🔴 Anki konsisten** — 先生/友達/東 & jukujikun 時計=とけい benar. Bias kanji 🔴 solid.
- ✅ **DK-narabekae bersih tanpa hint** — bukti paham urutan, bukan artefak panel bocor.
- 🔺 **Fokus tersisa = pasangan waktu まえに↔てから** (mirip pola kronis lawan-arti, tapi ini
  grammar bukan verb). Sempit & spesifik. Selebihnya matang.
- **Rekomendasi:** JLPT sudah sangat matang (94% dua mock beruntun, semua subtipe 🟢). Sisa
  lubang tipis = `まえに↔てから`. Drill via `/quiz lesson 16` (てから) + `/quiz lesson 18` (まえに)
  atau `/jlpt review`. Grammar `/quiz` juga masih punya 🟡 arah beri-terima (L7).
- **Sesi 2026-08-26 (mock keenam) skor 15/16 (94%)** — level tertinggi bertahan; lubang
  bergeser dari lawan-arti verb (tutup) ke pasangan waktu まえに↔てから.
