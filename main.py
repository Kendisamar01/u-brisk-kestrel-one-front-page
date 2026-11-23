import argparse
import os
from pathlib import Path


ENTRY = "Seven Ukrainian sea drones sank Russia's corvette Merkury at Benghazi, dragging the war into the Mediterranean"
MAX_LENGTH = 200


def validate_entry(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text or len(text) > MAX_LENGTH:
        raise ValueError("entry must be 1 to 200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("entry must be UTF-8 text") from exc
    return text


def write_entry(output_dir: str | Path) -> Path:
    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / "entry.txt"
    target.write_bytes(validate_entry(ENTRY).encode("utf-8"))
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description="Write the front-page headline entry.")
    parser.add_argument("--output-dir", default=os.environ.get("OUTPUT_DIR", "/output"))
    args = parser.parse_args()
    target = write_entry(args.output_dir)
    print(f"wrote {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
