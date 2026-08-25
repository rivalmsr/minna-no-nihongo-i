# Estimasi Biaya Token — /quiz & /jlpt

> ⚠️ **Estimasi kasar (±30%), bukan telemetri eksakt.** Diturunkan dari ukuran file
> nyata + pola baca/tulis tiap skill. Tujuannya memberi gambaran biaya & menunjukkan di
> mana token habis, bukan angka tagihan pasti. Untuk angka pasti, lihat usage report
> resmi Claude Code (mis. `/cost` bila tersedia).
>
> **Cara hitung:** file campuran Bahasa Indonesia + Jepang → ~**0.35 token/byte**
> (Jepang ~1 token/char tapi 3 byte UTF-8; Indonesia/ASCII ~0.25 token/byte). Ukuran file
> diambil dari `wc -c`. Perbarui tabel bila file inti berubah signifikan.

## Ringkasan
| | Konten sekali jalan | **Billed** (dgn re-send antar-turn) |
|---|---|---|
| **/quiz** (12 soal) | **~25–30K** | **~45–90K** |
| **/jlpt** (16 soal, 2 sesi) | **~35–45K** | **~70–160K** |

Rentang "billed" lebar karena bergantung **jumlah turn × ukuran konteks** dan **prompt
caching** (TTL 5 menit — kalau panel dijawab cepat, cache warm → jauh lebih murah).

## Anggaran baca (input) — bagian yang dikontrol desain hemat-token
| Sumber | /quiz | /jlpt |
|---|---|---|
| SKILL file (di-inject saat command) | ~6K | ~6K |
| CLAUDE.md (tiap sesi) | ~3K | ~3K |
| `evaluation.md` | ~1.8K | ~1.8K¹ |
| `jlpt-evaluation.md` | — | ~1.4K |
| `quiz-taxonomy.md` | ~3.1K | ~3.1K |
| `n5-synonyms.md` | — | ~0.9K |
| `anki-weak-items.md` (**anchor 🔴 saja**, ~20/137 baris) | ~0.5K | ~0.5K |
| lesson anchors (~0.4K × 3) | ~1.2K | ~1.5K |
| grep on-demand (kosakata/pola) | ~1–2K | ~2–3K |
| **Subtotal baca** | **~17–18K** | **~21–24K** |

¹ `evaluation.md` opsional di `/jlpt` (untuk membias soal grammar ke pola lemah).

## Generasi (output)
| | /quiz | /jlpt |
|---|---|---|
| Soal besar di chat | ~2–3K | ~4–6K (ada teks bacaan) |
| Panel AskUserQuestion | ~1.5K (3 panel) | ~2K (4 panel) |
| Lembar hasil + penjelasan | ~2–3K | ~3–4K |
| Update tracker (edit) | ~1–2K | ~1–2K |
| **Subtotal output** | **~7–10K** | **~10–16K** |

## Kenapa "billed" > "konten"
Tiap sesi punya banyak **turn**: baca state → panel 1 → panel 2 → … → nilai → edit
tracker. Setiap turn, konteks percakapan **dikirim ulang** ke model. Prompt caching
menekan biaya re-send kalau turn berdekatan (< 5 menit).

## Faktor yang menaikkan / menurunkan biaya
- 🔺 **`/jlpt` > `/quiz`** — 16 soal vs 12, ada teks bacaan, dan **cerita diulang di tiap
  panel** (aturan penyajian bacaan — trade-off UX ↔ token; lihat `docs/perbaikan-kb.md`).
- 🔺 Sesi lambat (panel dijawab > 5 menit) → cache dingin → re-send penuh.
- 🔻 **Baca-anchor** (bukan file utuh) — inti hemat: `vocabulary.md`/`particles.md`/lesson
  penuh **tak** dibaca. Ini yang menahan subtotal baca tetap ~17–24K.
- 🔻 Sesi kecil `/quiz lesson X N` (mis. 5 soal, 1 lesson) → jauh lebih murah.

## Kapan memperbarui dokumen ini
Bila salah satu berubah signifikan: ukuran SKILL/CLAUDE.md, jumlah soal default, aturan
penyajian (mis. cerita di panel), atau file inti yang dibaca. Hitung ulang pakai
`wc -c` × 0.35.
