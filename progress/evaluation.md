# Evaluasi Latihan — Tracker Kelemahan

> ⚙️ **Tabel AUTO-GENERATED oleh `scripts/kb.py`** (`render`/`record`) dari sumber
> `progress/attempts.jsonl` + `baseline.json`. **Jangan edit angka tabel dengan tangan**
> (tertimpa saat render). Prosa **Weak areas** = milik model, disuplai lewat
> `weak_narrative` saat `kb.py record`. Detail: `docs/engine-bookkeeping-plan.md`.

Diperbarui otomatis oleh skill `/quiz` setiap selesai sesi. Melacak akurasi
**per pola kalimat**, **per partikel**, dan **per lesson**, lalu memeringkat
**weak areas** untuk memandu pemilihan soal berikutnya.

**Ambang status:** akurasi <60% 🔴 LEMAH · 60–79% 🟡 · ≥80% 🟢
(butuh minimal **3 attempt** sebelum status dihitung; di bawah itu = ⚪ belum cukup data)

_Terakhir diperbarui: 2026-09-09 · total sesi: 34_

---

## Per pola kalimat
| Tag | Benar | Total | Akurasi | Status |
|-----|-------|-------|---------|--------|
| L4-jam | 7 | 8 | 88% | 🟢 |
| L5-で-transport | 3 | 3 | 100% | 🟢 |
| L6-を-objek | 2 | 2 | 100% | ⚪ |
| L7-に-memberi | 7 | 8 | 88% | 🟢 |
| L7-に-menerima | 8 | 9 | 89% | 🟢 |
| L7-で-alat | 3 | 3 | 100% | 🟢 |
| L7-で-bahasa | 3 | 4 | 75% | 🟡 |
| L7-もう | 3 | 3 | 100% | 🟢 |
| L8-adj-negatif | 2 | 2 | 100% | ⚪ |
| L8-adj-benda | 2 | 2 | 100% | ⚪ |
| L8-どう-どんな | 3 | 3 | 100% | 🟢 |
| L9-から-sebab | 3 | 3 | 100% | 🟢 |
| L9-が-suka | 2 | 2 | 100% | ⚪ |
| L9-が-paham | 2 | 2 | 100% | ⚪ |
| L9-が-pandai | 1 | 1 | 100% | ⚪ |
| L9-punya | 2 | 2 | 100% | ⚪ |
| L10-あります | 6 | 6 | 100% | 🟢 |
| L10-います | 3 | 3 | 100% | 🟢 |
| L10-に-keberadaan | 13 | 16 | 81% | 🟢 |
| L10-posisi | 8 | 9 | 89% | 🟢 |
| L11-まい | 2 | 2 | 100% | ⚪ |
| L11-かい-frekuensi | 2 | 2 | 100% | ⚪ |
| L11-かかります | 2 | 2 | 100% | ⚪ |
| L12-より | 2 | 2 | 100% | ⚪ |
| L12-のほうが | 2 | 2 | 100% | ⚪ |
| L12-lampau-positif | 2 | 2 | 100% | ⚪ |
| L13-に-tujuan | 10 | 12 | 83% | 🟢 |
| L13-を-meninggalkan | 8 | 8 | 100% | 🟢 |
| L13-で-vs-を | 8 | 10 | 80% | 🟢 |
| L13-ています-keadaan | 12 | 15 | 80% | 🟢 |
| L14-te-konjugasi | 35 | 37 | 95% | 🟢 |
| L14-てください | 6 | 7 | 86% | 🟢 |
| L14-ています-progresif | 5 | 6 | 83% | 🟢 |
| L14-ましょうか | 1 | 1 | 100% | ⚪ |
| L15-てもいいです | 3 | 3 | 100% | 🟢 |
| L15-てはいけません | 4 | 5 | 80% | 🟢 |
| L15-ています-keadaan | 8 | 9 | 89% | 🟢 |
| L15-に-vs-で-statis | 9 | 11 | 82% | 🟢 |
| L16-てから | 9 | 10 | 90% | 🟢 |
| L16-て-urutan | 1 | 1 | 100% | ⚪ |
| L16-他動詞-自動詞 | 6 | 7 | 86% | 🟢 |
| L16-に-naik | 10 | 12 | 83% | 🟢 |
| L17-ない-konjugasi | 14 | 15 | 93% | 🟢 |
| L17-なければなりません | 5 | 6 | 83% | 🟢 |
| L17-なくてもいいです | 5 | 6 | 83% | 🟢 |
| L17-ないでください | 3 | 3 | 100% | 🟢 |
| L18-ことができます | 9 | 10 | 90% | 🟢 |
| L18-まえに | 10 | 11 | 91% | 🟢 |
| L18-辞書形-konjugasi | 13 | 15 | 87% | 🟢 |
| L19-たことがあります | 16 | 17 | 94% | 🟢 |
| L19-た-konjugasi | 23 | 24 | 96% | 🟢 |
| L19-なります | 24 | 28 | 86% | 🟢 |
| L19-たり | 15 | 16 | 94% | 🟢 |
| L19-に-vs-を-のぼる | 6 | 6 | 100% | 🟢 |
| L5-と-dengan | 2 | 2 | 100% | ⚪ |
| L5-どこも | 1 | 1 | 100% | ⚪ |
| L6-で-tempat | 1 | 1 | 100% | ⚪ |
| L6-ませんか | 1 | 1 | 100% | ⚪ |
| L6-に-bertemu | 1 | 1 | 100% | ⚪ |
| L4-から-まで | 2 | 2 | 100% | ⚪ |
| L4-kata-kerja | 1 | 1 | 100% | ⚪ |
| L4-に-waktu | 2 | 2 | 100% | ⚪ |
| L5-へ-tujuan | 2 | 2 | 100% | ⚪ |
| L2-の-jenis | 1 | 1 | 100% | ⚪ |
| L2-この-benda | 1 | 1 | 100% | ⚪ |
| L2-なん | 1 | 1 | 100% | ⚪ |
| L2-の-milik | 1 | 1 | 100% | ⚪ |
| L3-どこ | 1 | 1 | 100% | ⚪ |
| L3-いくら | 1 | 1 | 100% | ⚪ |
| L3-どこの-asal | 1 | 1 | 100% | ⚪ |
| L3-ここ-tempat | 1 | 1 | 100% | ⚪ |
| L11-が-vs-を | 1 | 1 | 100% | ⚪ |
| L20-普通形-動詞 | 4 | 5 | 80% | 🟢 |
| L20-普通形-い形 | 3 | 3 | 100% | 🟢 |
| L20-普通形-な形-名詞 | 3 | 3 | 100% | 🟢 |
| L20-普通体-会話 | 1 | 1 | 100% | ⚪ |
| L12-lampau-negatif | 1 | 1 | 100% | ⚪ |
| L16-gabung-sifat | 1 | 2 | 50% | ⚪ |
| L21-と思います | 1 | 1 | 100% | ⚪ |
| L21-でしょう | 1 | 1 | 100% | ⚪ |
| L21-と言いました | 0 | 1 | 0% | ⚪ |
| L21-言葉-うごきます | 1 | 1 | 100% | ⚪ |

## Per partikel
| Partikel | Benar | Total | Akurasi | Status |
|----------|-------|-------|---------|--------|
| から | 5 | 5 | 100% | 🟢 |
| に | 59 | 68 | 87% | 🟢 |
| で | 22 | 26 | 85% | 🟢 |
| を | 28 | 29 | 97% | 🟢 |
| の | 3 | 3 | 100% | 🟢 |
| が | 16 | 16 | 100% | 🟢 |
| へ | 5 | 5 | 100% | 🟢 |
| と | 2 | 2 | 100% | ⚪ |
| より | 1 | 1 | 100% | ⚪ |
| まで | 1 | 1 | 100% | ⚪ |

## Per lesson
| Lesson | Benar | Total | Akurasi | Status |
|--------|-------|-------|---------|--------|
| Lesson 4 | 12 | 13 | 92% | 🟢 |
| Lesson 5 | 8 | 8 | 100% | 🟢 |
| Lesson 6 | 5 | 5 | 100% | 🟢 |
| Lesson 7 | 24 | 27 | 89% | 🟢 |
| Lesson 8 | 8 | 8 | 100% | 🟢 |
| Lesson 9 | 10 | 10 | 100% | 🟢 |
| Lesson 10 | 30 | 34 | 88% | 🟢 |
| Lesson 11 | 7 | 7 | 100% | 🟢 |
| Lesson 12 | 7 | 7 | 100% | 🟢 |
| Lesson 13 | 40 | 47 | 85% | 🟢 |
| Lesson 14 | 30 | 32 | 94% | 🟢 |
| Lesson 15 | 24 | 28 | 86% | 🟢 |
| Lesson 16 | 26 | 31 | 84% | 🟢 |
| Lesson 17 | 15 | 16 | 94% | 🟢 |
| Lesson 18 | 22 | 24 | 92% | 🟢 |
| Lesson 19 | 63 | 70 | 90% | 🟢 |
| Lesson 2 | 4 | 4 | 100% | 🟢 |
| Lesson 3 | 4 | 4 | 100% | 🟢 |
| Lesson 20 | 11 | 12 | 92% | 🟢 |
| Lesson 21 | 3 | 4 | 75% | 🟡 |

---

## Weak areas (prioritas soal berikutnya)
Sesi bersih (11/12) — satu 🟡 lama justru lulus ke 🟢. 1) **L7-で-bahasa 3/4 75% 🟡** — soal で-media sesi ini BENAR (日本語で書きました✓), status masih 🟡 karena riwayat lama belum terhapus; tren naik (67%→75%). Sinyal: kontras で-media↔に sudah mulai mantap, butuh 1–2 konfirmasi lagi untuk lewat ambang 80%. 2) **Lesson 21 3/4 75% 🟡** — bab baru, satu-satunya miss ada di sini: **L21-と言いました** — pada kutipan langsung 「あした休みます」と（　）dijawab **思いました** (tertukar と思います). Beda intinya: 「　」kutipan ucapan → **言いました** (melaporkan perkataan), sedang と思います = pendapat/dugaan tanpa 「　」. と思います sendiri BENAR (便利だと✓, な-adj pakай だ), でしょう juga BENAR (試験でしょう — N tanpa だ), うごきます-が✓. Yang naik ke 🟢: **L15-てはいけません 80%** (電気を消しては✗→ sesi ini とっては/なくしては semua ✓, tak lagi tertukar ke ても), L7-で-alat & L15-てもいいです. Verb recall solid: しって・けして・なくして (音便 す→して) semua ✓. **Rekomendasi:** sesi depan selipkan 1 soal **kontras と言いました↔と思います** (「」 vs tanpa「」) untuk mengunci L21, plus 1 で-media terakhir agar L7-で-bahasa lewat 80%; sisanya lanjut maintenance ke bab yang lama tak disentuh.
