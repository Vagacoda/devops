#!/usr/bin/env bash
cd "$(dirname "$0")" || exit 1
exec python3 chat.py
if ! command -v python3 >/dev/null 2>&1; then
echo "Python3를 먼저 설치하세요." >&2
exit 1
fi

echo "End"
