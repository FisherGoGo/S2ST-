"""Create records only. No ASR, MT, TTS, network access or dependencies."""
import argparse
from datetime import datetime, timezone, timedelta
import json
from pathlib import Path
import platform
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from s2st_lab.audio import inspect_wav, sha256, write_json_new


def git_head():
    result = subprocess.run(["git", "rev-parse", "HEAD"], cwd=Path(__file__).resolve().parents[1],
                            capture_output=True, text=True, check=False)
    return result.stdout.strip() if result.returncode == 0 else None


def main():
    parser = argparse.ArgumentParser(description="Create a new record directory; models remain not_run.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        config = json.loads(args.config.read_text(encoding="utf-8-sig"))
        if not isinstance(config, dict):
            raise ValueError("Config must be a JSON object.")
        if config.get("source_language") not in ("zh", "en") or config.get("target_language") not in ("zh", "en"):
            raise ValueError("This scaffold expects source/target languages zh or en.")
        if config["source_language"] == config["target_language"]:
            raise ValueError("Source and target must differ for this cross-language scaffold.")
        metadata = inspect_wav(args.input)
        try:
            commit = git_head()
        except OSError:
            commit = None
        record = {
            "schema_version": 1,
            "created_at": datetime.now(timezone(timedelta(hours=8))).isoformat(),
            "timezone": "Asia/Shanghai", "state": "records_only",
            "input_sha256": metadata["file_sha256"], "config_sha256": sha256(args.config),
            "python": sys.version, "python_executable": sys.executable,
            "platform": platform.platform(), "git_head": commit,
            "git_worktree_state": "not_captured; HEAD alone does not identify uncommitted code",
            "command_argv": sys.argv,
            "stages": {stage: "not_run" for stage in ("asr", "mt", "tts", "evaluation")},
            "metrics": None,
        }
        args.output.mkdir(parents=True, exist_ok=False)
        write_json_new(args.output / "config.json", config)
        write_json_new(args.output / "input.json", metadata)
        write_json_new(args.output / "run.json", record)
        print(f"Records created (models not run): {args.output.resolve()}")
    except (OSError, ValueError) as exc:
        parser.exit(2, f"Record creation failed: {exc}\n")


if __name__ == "__main__":
    main()
