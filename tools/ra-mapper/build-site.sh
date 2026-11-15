#!/usr/bin/env bash
# Build the RA mapper into <site dir>/en/mapper/ — a build-instance-site source
# step (`bun run site:mapper <site dir>`), which replaced ra-mapper.yml's
# Actions deploy when the site became agent-run (bean n3h9).
#
# The current version is the IG's (`version:` in sushi-config.yaml), listed
# first so it becomes the mapper's default; the other SemVer folders follow,
# newest first. See archimate/README.md.
set -euo pipefail
OUT=$(cd "${1:?usage: build-site.sh <site dir>}" && pwd)
cd "$(dirname "${BASH_SOURCE[0]}")"

CURRENT=$(sed -n 's/^version:[[:space:]]*\([^[:space:]#]*\).*/\1/p' ../../sushi-config.yaml | head -n1)
MODELS=(); LABELS=()
add() {
  local m
  m=$(find "$1" -maxdepth 1 -name '*.archimate' -type f | head -1)
  if [ -n "$m" ]; then MODELS+=("$m"); LABELS+=("$2"); fi
}
if [ -n "$CURRENT" ] && [ -d "../../archimate/$CURRENT" ]; then
  add "../../archimate/$CURRENT" "WHO RA $CURRENT (current)"
else
  echo "warning: sushi-config.yaml is at version '${CURRENT:-<none>}' but archimate/${CURRENT:-<none>}/ does not exist — the mapper has no current model." >&2
fi
for NAME in $(ls ../../archimate | grep -E '^[0-9]+\.[0-9]+\.[0-9]+(-[0-9A-Za-z.-]+)?$' | sort -rV); do
  [ "$NAME" = "$CURRENT" ] && continue
  add "../../archimate/$NAME" "WHO RA $NAME"
done
[ ${#MODELS[@]} -gt 0 ] || { echo "no ArchiMate model to map" >&2; exit 1; }

echo "Building mapper with: ${LABELS[*]}"
T=$(mktemp -d)
python3 build_ra_mapper.py "${MODELS[@]}" -l "${LABELS[@]}" -o "$T/SMART-RA-Mapper.html"
# Rendered pages live under /<locale>/ (folio-assistant#2527); /mapper/ forwards
# here (tools/site-redirects.sh).
mkdir -p "$OUT/en/mapper"
cp "$T/SMART-RA-Mapper.html" "$OUT/en/mapper/index.html"
cp "$T/SMART-RA-Mapper.html" "$OUT/en/mapper/SMART-RA-Mapper.html"
rm -rf "$T"
