"""Optional real ASR, using an existing local trusted checkpoint only.

Install/prepare openai-whisper, PyTorch and FFmpeg explicitly before use.
No imports of model dependencies until paths and CLI arguments are validated.
"""
import argparse
from datetime import datetime, timezone, timedelta
import importlib.metadata
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from s2st_lab.audio import sha256, write_json_new


def main():
    parser = argparse.ArgumentParser(description="Transcribe using an existing local Whisper .pt; never download by model name.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--checkpoint", required=True, type=Path)
    parser.add_argument("--language", required=True, choices=("zh", "en"))
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if not args.input.is_file():
        parser.error("Input must be an existing local audio file.")
    if not args.checkpoint.is_file() or args.checkpoint.suffix.lower() != ".pt":
        parser.error("Checkpoint must be an existing local .pt path; model names are not accepted.")
    if args.output.exists():
        parser.error("Output exists; choose a new artifact path.")
    try:
        import whisper
        import torch
    except ImportError as exc:
        parser.exit(2, f"Missing model dependency: {exc}. See the environment guide; nothing was installed.\n")
    if args.device == "cuda" and not torch.cuda.is_available():
        parser.error("CUDA requested but unavailable.")
    checkpoint = args.checkpoint.resolve()
    try:
        t0 = time.perf_counter()
        model = whisper.load_model(str(checkpoint), device=args.device)
        if args.device == "cuda":
            torch.cuda.synchronize()
        t1 = time.perf_counter()
        result = model.transcribe(str(args.input.resolve()), language=args.language,
                                  task="transcribe", fp16=args.device == "cuda")
        if args.device == "cuda":
            torch.cuda.synchronize()
        t2 = time.perf_counter()
        record = {
            "schema_version": 1, "state": "asr_completed",
            "created_at": datetime.now(timezone(timedelta(hours=8))).isoformat(),
            "timezone": "Asia/Shanghai", "command_argv": sys.argv,
            "input_path": str(args.input.resolve()), "input_sha256": sha256(args.input),
            "checkpoint_path": str(checkpoint), "checkpoint_sha256": sha256(checkpoint),
            "openai_whisper_version": importlib.metadata.version("openai-whisper"),
            "torch_version": torch.__version__, "python": sys.version,
            "parameters": {"language": args.language, "task": "transcribe", "device": args.device,
                           "fp16": args.device == "cuda", "other_decode_options": "library defaults; version recorded"},
            "timing_seconds": {"model_load": t1 - t0, "transcribe": t2 - t1},
            "timing_scope": "transcribe includes decode/feature processing; model load and result serialization are separate",
            "text": result["text"], "segments": result.get("segments", []),
            "detected_language": result.get("language"),
        }
        write_json_new(args.output, record)
        print(f"ASR artifact saved: {args.output.resolve()}")
    except Exception as exc:
        # Report real failures and leave a nonzero exit; never substitute mock text.
        parser.exit(1, f"ASR failed ({type(exc).__name__}): {exc}\n")


if __name__ == "__main__":
    main()
