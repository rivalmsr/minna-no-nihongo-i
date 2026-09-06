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

_Terakhir diperbarui: 2026-09-06 · total sesi: 17_

---

## Sesi 1 — 文字・語彙 (Moji-Goi)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Baca kanji (cara baca) | `MG-yomi` | 33 | 34 | 97% | 🟢 |
| Tulis kanji (penulisan) | `MG-hyouki` | 32 | 34 | 94% | 🟢 |
| Kosakata dalam konteks | `MG-bunmyaku` | 30 | 34 | 88% | 🟢 |
| Sinonim / 言い換え類義 | `MG-ruigi` | 33 | 34 | 97% | 🟢 |

## Sesi 2 — 文法・読解 (Bunpou-Dokkai)
| Subtipe | Tag | Benar | Total | Akurasi | Status |
|---------|-----|-------|-------|---------|--------|
| Tata bahasa (grammar) | `DK-bunpou` | 30 | 35 | 86% | 🟢 |
| Susun kalimat (★) | `DK-narabekae` | 16 | 18 | 89% | 🟢 |
| Tata bahasa dalam teks (cloze) | `DK-bunshou` | 13 | 14 | 93% | 🟢 |
| Bacaan pendek | `DK-dokkai` | 33 | 34 | 97% | 🟢 |
| Bacaan informasi (info-search) | `DK-joho` | 31 | 34 | 91% | 🟢 |

---

## Weak types (prioritas soal `/jlpt review`)
**Tak ada 🔴/🟡 — sembilan subtipe JLPT tetap 🟢.** Mock 2026-09-06 skor **14/16 (88%)**, Sesi 1 **7/8**, Sesi 2 **7/8**. Dua miss, keduanya slip (bukan pola/subtipe lemah baru): 1) **MG-ruigi** turun tipis 100%→**97%** (tetap 🟢): 「あの レストランは 遠（とお）くないです」 dijawab **広（ひろ）いです** padahal padanan 遠くない = **近（ちか）いです** (dekat). User tertukar antara 'tidak jauh' (=dekat) dengan 'luas' — kesalahan makna sifat, bukan struktur parafrase; sisa soal ruigi (有名 = みんな知っている) benar. 2) **DK-bunpou** 88%→**86%** (tetap 🟢): 「写真を（　）も いいですか」 dijawab **とらないで** padahal pola 〜てもいいですか menuntut **て-form**: とって. Pola izin (L15) tercampur dgn bentуk larangan — sinyal て-form vs ないで masih sesekali goyah di bawah tekanan format ujian. **Sinyal positif:** MG-yomi 97%, MG-hyouki 94%, MG-bunmyaku 88% (つけます・おつり benar), semua blok berteks S2 sempurna (bunshou 2/2 でも・くれます, dokkai 2/2, joho 2/2) → wacana & info-search kokoh. **Rekomendasi:** lanjut mock berkala lawan decay; sesekali sisipkan (a) MG-ruigi antonim/derajat (遠い↔近い, ひろい↔せまい, たかい↔ひくい) agar pasangan sifat makin refleks, dan (b) DK-bunpou drill 〜てもいいです／〜てはいけません／〜ないでください berdampingan supaya pemilihan て vs ないで otomatis. Rotasi tema hindari hobi-musik/jadwal-kelas/surat-teman di mock berikut.
