# Rencana: Integrasi Data Anki ke Knowledge Base

> **Status: RENCANA — belum dieksekusi.** Dokumen forward-looking. Dibuat 2026-08-23.
> Tujuan: menyatukan sinyal dari deck Anki desktop ke dalam KB Minna no Nihongo I &
> latihan `/quiz` + `/jlpt`. Eksekusi menyusul, per fase, setelah disetujui.

## 1. Konteks & temuan

Anki desktop terpasang di laptop ini. Collection bisa dibaca **langsung** dari
SQLite tanpa membuka Anki:

```
~/Library/Application Support/Anki2/User 1/collection.anki2
```

Isi collection (per 2026-08-23):

| Deck | Total | Baru | Muda | Matang | Catatan |
|------|-------|------|------|--------|---------|
| **Minna no Nihongo I** | 896 | 0 | 178 | 718 | ✅ semua dipelajari, ~80% matang |
| **Japanese Kanji N5** | 107 | 0 | 71 | 36 | 🟡 sedang jalan |
| Japanese Kanji N4 | 173 | 173 | 0 | 0 | ⚪ belum mulai (di luar cakupan) |
| Oxford 3000 A1 (Inggris) | 920 | 735 | 82 | 103 | proyek Inggris, di luar cakupan |

- Revlog: 12 Jun → 22 Agu 2026, 8475 review, akurasi harian ~62–82%.
- Dua deck target (Minna, Kanji N5) pakai notetype **Basic** (`Front` / `Back`).
  - Minna Front = kana; Back = arti Indonesia. Verb ditandai grup di token akhir Front
    (`だします I`, `たべます II`, `きます III`).
  - Kanji N5 Front = kanji; Back = `bacaan | arti` (mis. `先 | せん | dahulu, depan`).

### Dua sinyal berbeda dari Anki

1. **Isi** (kata/kanji + arti) — sudah ada padanannya di `reference/n5-vocabulary.md`
   & `reference/anki-verbs.md`. Menyalin ulang = duplikat, nilai rendah.
2. **Sinyal perilaku** (`lapses`, `ease`, `ivl`, `revlog`) — **belum dipakai KB sama
   sekali.** Inilah nilai uniknya: Anki tahu **item mana yang empiris sering dilupakan**.
   Contoh lapses tertinggi deck Minna: だします (13×), もらいます (13×), つけます (12×),
   けします (12×), おいくつ (12×), りょこう (12×).

> **Insight inti:** `progress/evaluation.md` melacak kelemahan per **pola grammar**;
> Anki melacak kelemahan per **item kosakata/kanji**. Menikahkan keduanya → `/quiz` &
> `/jlpt` bisa memilih "kendaraan" kosakata/kanji yang benar-benar sulit, **di dalam**
> pola yang lemah. Selaras dengan filosofi CLAUDE.md ("verb = kendaraan active recall").

### ⚠️ Masalah yang sudah ada (harus diperbaiki)

`reference/anki-verbs.md` mendeklarasikan dirinya AUTO-GENERATED dari
`learn-anki/Minna no Nihongo I/MNN*.txt` via `scripts/sync-anki-verbs.sh`. **Folder
`.txt` itu sudah tidak ada di laptop ini** → script sekarang langsung `exit 1`. Deck
sudah pindah total ke dalam `collection.anki2`. Akibatnya file verb pool berpotensi
**basi**: file mendeklarasikan 87 verb, collection punya ~113 kartu bertanda grup.

## 2. Rencana per fase

Tiga fase saling menumpuk (A fondasi → B data baru → C mengikat ke latihan).

### Fase A — Perbaiki & upgrade pipeline sync (fondasi)

**Masalah:** sumber `.txt` hilang, `anki-verbs.md` basi & script mati.

**Rencana:**
- Tulis ulang `scripts/sync-anki-verbs.sh` (atau skrip Python pendamping) agar baca
  **langsung dari `collection.anki2`**, bukan `.txt`.
  - Salin DB ke lokasi sementara dulu (hindari lock kalau Anki terbuka), query read-only.
  - Filter deck Minna (`did = 1781493801806`), ekstrak Front bertanda grup `I/II/III`.
  - Kolom `name` deck pakai collation `unicase` yang tidak ada di sqlite3 CLI →
    **group by `did`**, map nama deck manual (jangan `ORDER BY`/`GROUP BY` kolom nama).
- Regen `reference/anki-verbs.md` dengan verb terkini + kelompok I/II/III.
- **Upgrade:** tambah kolom **kesulitan** dari `lapses` (mis. 🔴 lapses ≥ 8, 🟡 4–7,
  ⚪ 0–3) supaya /quiz tahu verb mana yang perlu porsi lebih.
- Perbarui header file & komentar script agar menunjuk sumber baru (collection.anki2),
  bukan folder `.txt` yang sudah tiada.

**Keputusan desain yang perlu diambil dulu:**
- **Portabilitas path:** hardcode `~/Library/Application Support/Anki2/User 1/` atau
  jadikan variabel/argumen? (Path khusus macOS + nama profil "User 1".)
- **Snapshot vs live:** file turunan tetap (commit-able) — sudah benar; tinggal ganti
  sumbernya.

**Output:** `scripts/sync-anki-verbs.sh` (diperbaiki), `reference/anki-verbs.md`
(regen + kolom kesulitan).

### Fase B — Laporan item lemah (data baru)

**Rencana:**
- Buat `progress/anki-weak-items.md` — daftar item paling sering dilupakan, dari
  `lapses` (dan/atau `ease` rendah), untuk deck Minna & Kanji N5.
  - Query: `SELECT lapses, reps, flds FROM cards JOIN notes … ORDER BY lapses DESC`.
  - Pisahkan section: **Kosakata/Verb lemah** (Minna) & **Kanji lemah** (N5).
  - Sertakan furigana untuk semua kanji (konvensi KB — lihat `furigana-everywhere`).
- Tandai file sebagai **turunan** (regenerasi dari collection), jangan diedit tangan.

**Keputusan desain:**
- Ambang "lemah": pakai `lapses` absolut, atau relatif (mis. top-15%)? Sertakan juga
  kartu `queue = -1` (suspended) atau abaikan?
- Frekuensi refresh: manual via script yang sama seperti Fase A?

**Output:** `progress/anki-weak-items.md`.

### Fase C — Integrasi ke skill /quiz & /jlpt (mengikat)

**Rencana:**
- Update `.claude/skills/quiz/SKILL.md`: saat memilih "kendaraan" kosakata/verb,
  **boboti** ke item lemah Anki (`anki-weak-items.md`) — di dalam pola lemah dari
  `evaluation.md`. Tetap patuh: soal grammar hanya dari `lessons/`.
- Update `.claude/skills/jlpt/SKILL.md`: subtipe baca/tulis kanji (MG-*) & kosakata
  boboti ke kanji/kata lemah Anki. Konsisten dgn hint-fading yang sudah ada.
- Update `CLAUDE.md` bila sumber data baru ini jadi bagian tetap alur quiz.

**Keputusan desain:**
- Seberapa besar bobotnya? Jangan sampai item lemah Anki menenggelamkan tujuan utama
  (uji pola grammar). Anki = pemilih *kosakata*, bukan pengganti *pola*.
- Hemat token: `anki-weak-items.md` harus punya anchor ringkas (baca ~20 baris),
  seperti file lain — jangan Read utuh saat quiz.

## 3. Risiko & catatan

- **Ketergantungan lingkungan:** pipeline hanya jalan di laptop yang ada Anki desktop-nya.
  Di mesin lain script harus gagal anggun (pesan jelas), bukan menghasilkan file kosong.
- **Path & profil macOS-spesifik** (`Application Support`, profil "User 1") — rapuh
  kalau profil di-rename. Pertimbangkan variabel konfigurasi.
- **Jangan campur deck di luar cakupan** (Kanji N4, Oxford 3000 A1) ke KB Jepang N5.
- **File turunan tetap tak boleh diedit tangan** — sama seperti `anki-verbs.md` sekarang.
- **AnkiConnect (port 8765) tidak aktif** saat ini; kalau nanti mau query real-time
  (saat Anki terbuka) itu jalur alternatif, tapi baca DB langsung sudah cukup & lebih
  independen.

## 4. Urutan eksekusi yang disarankan

1. **Fase A** dulu — memperbaiki yang benar-benar rusak, verb pool /quiz akurat lagi.
2. **Fase B** — menghasilkan sinyal item-lemah baru.
3. **Fase C** — mengikat A+B ke latihan harian.

Eksekusi menunggu persetujuan. Saat mengeksekusi, patuhi konvensi CLAUDE.md
(furigana wajib, file turunan tak diedit tangan, update README/taxonomy bila perlu,
laporkan tiap perubahan).
