#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# sync-anki-verbs.sh
# Regenerasi reference/anki-verbs.md dari deck Anki (UPSTREAM source of truth).
#
# Folder Anki (`learn-anki/minna-no-nihongo-1`) adalah sumber yang terus di-update
# user. Jalankan script ini tiap kali deck itu berubah supaya pool kata kerja untuk
# /quiz tetap sinkron. File output = TURUNAN, jangan di-edit tangan.
#
# Pakai: bash scripts/sync-anki-verbs.sh
# ---------------------------------------------------------------------------
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ANKI_DIR="$PROJECT_ROOT/../../learn-anki/minna-no-nihongo-1"
OUT="$PROJECT_ROOT/reference/anki-verbs.md"

if [ ! -d "$ANKI_DIR" ]; then
  echo "ERROR: folder Anki tidak ditemukan: $ANKI_DIR" >&2
  echo "Sesuaikan ANKI_DIR di script bila lokasi deck berpindah." >&2
  exit 1
fi

# Ekstrak baris kata kerja satu grup (I/II/III) dari semua mnn-*.txt, urut per bab.
# Kolom Anki: <kata><TAB><arti>; kata kerja ditandai grup di token terakhir kolom-1.
gen_group() {
  local grp="$1" f base L
  for f in "$ANKI_DIR"/mnn-*.txt; do
    base="$(basename "$f")"
    L="$(printf '%s' "$base" | sed -E 's/mnn-0?([0-9]+)\.txt/\1/')"
    awk -F'\t' -v grp="$grp" -v L="$L" '
      {
        n = split($1, p, " ")
        if (p[n] == grp) {
          form = $1; sub(/ [^ ]+$/, "", form)   # buang token grup di akhir
          printf "| %s | %s | L%s |\n", form, $2, L
        }
      }' "$f"
  done
}

TABLE_I="$(gen_group I)"
TABLE_II="$(gen_group II)"
TABLE_III="$(gen_group III)"
N_I="$(printf '%s\n' "$TABLE_I" | grep -c '^|' || true)"
N_II="$(printf '%s\n' "$TABLE_II" | grep -c '^|' || true)"
N_III="$(printf '%s\n' "$TABLE_III" | grep -c '^|' || true)"
N_TOTAL=$(( N_I + N_II + N_III ))
TODAY="$(date +%Y-%m-%d)"

cat > "$OUT" <<EOF
# Pool Kata Kerja (動詞) — Sumber Active Recall Quiz

> ⚙️ **FILE AUTO-GENERATED — jangan edit tangan.** Regenerasi dari deck Anki dengan
> \`bash scripts/sync-anki-verbs.sh\`. Upstream source of truth = folder
> \`learn-anki/minna-no-nihongo-1/mnn-*.txt\` (yang kamu update untuk Anki). Jalankan
> ulang script tiap kali deck bertambah/berubah agar /quiz tetap sinkron.

Ekstraksi **semua kata kerja** dari deck Anki. Tujuan file ini bukan menghafal arti
(itu tugas Anki), tapi **membiasakan MEMAKAI kata kerja** dalam kalimat &
mengkonjugasikannya — konsep **active recall**. \`/quiz\` memakai file ini sebagai
kolam verb utama untuk soal konjugasi & pemakaian.

> Ringkasan cepat (anchor — baca ini saja saat quiz):
> - **${N_TOTAL} verb**, dikelompokkan **grup I (${N_I}) / II (${N_II}) / III (${N_III})** (penentu bentuk て・ない・辞書・た).
> - **Grup II** paling mudah: buang ます → tempel langsung (\`たべます→たべて／たべない／たべる／たべた\`).
> - **Grup III** cuma 2 pola: \`〜します\` & \`〜きます\` (irregular, hafal).
> - **Grup I** butuh **音便** (lihat tabel 音便 di bawah) untuk bentuk て／た.
> - Bab konjugasi: **て = L14**, **ない = L17**, **辞書形 = L18**, **た = L19**.
> - Soal tata bahasa tetap **hanya** dari lesson yang tersedia di \`lessons/\`.

## Cara pakai untuk active recall (target soal)

Alih-alih "apa arti のみます?", soal harus memaksa **produksi bentuk & konteks**:
- **Konjugasi:** \`およぎます\` → bentuk て? (\`およいで\`) · ない? (\`およがない\`) · た? (\`およいだ\`)
- **Pemakaian dalam pola in-scope:** \`〜てください\`, \`〜ています\`, \`〜なければなりません\`,
  \`〜たことがあります\`, \`〜たり〜たり\`, \`〜ことができます\`, dll. dengan verb dari pool ini.
- **Pasangan mirip / 他動詞↔自動詞:** \`はじめます（を）↔はじまります（が）\`, \`でます↔だします\`,
  \`のります（に）↔おります（を）\`, \`つけます↔けします\`, \`あけます↔しめます\`.

## 音便 bentuk て／た — GRUP I (yang paling sering lupa)

| Akhiran ます | → て | → た | Contoh |
|-------------|------|------|--------|
| 〜います・〜ちます・〜ります | って | った | かいます→かって, まちます→まって, とります→とって |
| 〜みます・〜びます・〜にます | んで | んだ | のみます→のんで, よびます→よんで, あそびます→あそんで |
| 〜きます | いて | いた | かきます→かいて（**例外 いきます→いって**） |
| 〜ぎます | いで | いだ | およぎます→およいで／およいだ |
| 〜します | して | した | はなします→はなして／はなした |

Grup II: buang ます, tempel て／ない／る／た langsung. Grup III: \`します→して／しない／する／した\`,
\`きます→きて／こない／くる／きた\`.

---

## GRUP I (${N_I}) — perlu 音便 untuk て／た
| ます形 | Arti | Bab |
|--------|------|-----|
${TABLE_I}

## GRUP II (${N_II}) — buang ます, tempel langsung
| ます形 | Arti | Bab |
|--------|------|-----|
${TABLE_II}

## GRUP III (${N_III}) — します／きます (irregular)
| ます形 | Arti | Bab |
|--------|------|-----|
${TABLE_III}

---

_Auto-generated ${TODAY} oleh \`scripts/sync-anki-verbs.sh\` dari
\`learn-anki/minna-no-nihongo-1/mnn-*.txt\`. Total ${N_TOTAL} verb._
EOF

echo "OK → $OUT"
echo "Grup I: $N_I · Grup II: $N_II · Grup III: $N_III · Total: $N_TOTAL"
