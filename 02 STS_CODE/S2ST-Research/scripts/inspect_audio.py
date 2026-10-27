"""Usage: python scripts/inspect_audio.py --input sample.wav [--output check.json]"""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from s2st_lab.audio import inspect_wav, write_json_new


def main():
    parser = argparse.ArgumentParser(description="Inspect a local PCM16 WAV without modifying it.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = inspect_wav(args.input)
        if args.output:
            write_json_new(args.output, result)
            print(f"Saved: {args.output.resolve()}")
        else:
            print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    except (OSError, ValueError) as exc:
        parser.exit(2, f"Audio check failed: {exc}\n")


if __name__ == "__main__":
    main()
