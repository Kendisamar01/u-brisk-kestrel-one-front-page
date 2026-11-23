# One Sentence, One Front Page

Writes the front-page headline for Monday 23 November 2026 to `/output/entry.txt`: UTF-8, 1–200 characters, no trailing newline.

Run with `python3 main.py`. For local tests, pass `--output-dir DIR` or set `OUTPUT_DIR=DIR`.

Pure Python standard library. `validate_entry()` rejects empty, whitespace-only and over-200-character entries.
