"""Read-only PCM16 WAV diagnostics, with streaming amplitude statistics."""
import array
import hashlib
import json
import math
from pathlib import Path
import sys
import wave


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def inspect_wav(path):
    path = Path(path).resolve(strict=True)
    try:
        with wave.open(str(path), "rb") as stream:
            channels = stream.getnchannels()
            width = stream.getsampwidth()
            rate = stream.getframerate()
            frames = stream.getnframes()
            if stream.getcomptype() != "NONE" or width != 2:
                raise ValueError("Only uncompressed 16-bit PCM WAV is supported.")
            if channels < 1 or rate < 1 or frames < 1:
                raise ValueError("Empty or invalid WAV metadata.")
            count = total_square = zeros = endpoints = peak = 0
            while raw := stream.readframes(16384):
                if len(raw) % (channels * width):
                    raise ValueError("Truncated WAV: partial sample frame.")
                values = array.array("h")
                values.frombytes(raw)
                if sys.byteorder != "little":
                    values.byteswap()
                for value in values:
                    count += 1
                    total_square += value * value
                    zeros += value == 0
                    endpoints += value in (-32768, 32767)
                    peak = max(peak, abs(value))
            if count != frames * channels:
                raise ValueError("Truncated WAV: data does not match declared frames.")
    except (wave.Error, EOFError) as exc:
        raise ValueError(f"Cannot read PCM WAV: {exc}") from exc
    rms = math.sqrt(total_square / count) / 32768
    return {
        "path": str(path), "file_sha256": sha256(path),
        "sample_rate_hz": rate, "channels": channels, "sample_width_bits": width * 8,
        "frames": frames, "duration_seconds": frames / rate,
        "peak_amplitude": peak / 32768, "rms_amplitude": rms,
        "rms_dbfs": 20 * math.log10(rms) if rms else None,
        "zero_sample_fraction": zeros / count,
        "digital_endpoint_fraction": endpoints / count,
        "interpretation": "Pooled channel statistics. Exact zeros are not VAD silence; endpoints are not a complete clipping detector.",
    }


def write_json_new(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation protects previous experiment artifacts.
    with path.open("x", encoding="utf-8") as stream:
        json.dump(data, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")
