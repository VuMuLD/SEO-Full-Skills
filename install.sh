#!/usr/bin/env bash
# SEO All-in-One — macOS/Linux installer.
# Copies this folder to ~/.claude/skills/seo and creates a private Python venv.
# Usage: bash install.sh [--optional] [--no-venv]
set -euo pipefail

OPTIONAL=0; NOVENV=0
for arg in "$@"; do
  case "$arg" in
    --optional) OPTIONAL=1 ;;
    --no-venv) NOVENV=1 ;;
  esac
done

SRC="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
DEST="$HOME/.claude/skills/seo"

if [[ "$SRC" != "$DEST" ]]; then
  if [[ -d "$DEST" ]]; then
    BACKUP="$DEST.bak-$(date +%Y%m%d%H%M%S)"
    echo "Existing skill found, backing up to $BACKUP"
    mv "$DEST" "$BACKUP"
  fi
  mkdir -p "$(dirname "$DEST")"
  cp -R "$SRC" "$DEST"
  echo "Skill copied to $DEST"
fi

[[ "$NOVENV" == 1 ]] && { echo "Done (no venv)."; exit 0; }

PY=""
for cand in python3 python; do
  if command -v "$cand" >/dev/null 2>&1 && "$cand" -c 'import sys; raise SystemExit(0 if sys.version_info >= (3,10) else 1)'; then
    PY="$cand"; break
  fi
done
[[ -z "$PY" ]] && { echo "Python 3.10+ not found." >&2; exit 1; }

"$PY" -m venv "$DEST/.venv"
VPY="$DEST/.venv/bin/python"
"$VPY" -m pip install --upgrade pip --quiet
"$VPY" -m pip install -r "$DEST/requirements.txt"
if [[ "$OPTIONAL" == 1 ]]; then
  "$VPY" -m pip install -r "$DEST/requirements-optional.txt"
  "$VPY" -m playwright install chromium
fi

echo
echo "Installed. Python for the scripts: $VPY"
echo "Restart Claude Code, then try:  /seo audit https://example.com"
