import json
import subprocess
import sys
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
MAIN_FILE = next(
    (parent / "main.py" for parent in SCRIPT_PATH.parents if (parent / "main.py").exists()),
    None,
)


def main() -> int:
    if MAIN_FILE is None:
        print(f"ERROR: Could not locate main.py from script path: {SCRIPT_PATH}")
        return 1

    if not MAIN_FILE.exists():
        print(f"ERROR: File not found: {MAIN_FILE}")
        return 1

    result = subprocess.run(
        [sys.executable, str(MAIN_FILE)],
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode != 0:
        print("ERROR: main.py failed")
        print(result.stderr)
        return 1

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        print("ERROR: Output is not valid JSON")
        print(exc)
        print("Raw output:")
        print(result.stdout)
        return 1

    required_top_level_keys = {"message", "calculation", "status"}

    if set(data.keys()) != required_top_level_keys:
        print("ERROR: JSON does not have the expected top-level keys")
        print(f"Expected: {required_top_level_keys}")
        print(f"Actual: {set(data.keys())}")
        return 1

    if data["message"] != "Hello, World!":
        print("ERROR: Invalid message")
        return 1

    if data["status"] != "success":
        print("ERROR: Invalid status")
        return 1

    calculation = data["calculation"]

    if calculation.get("expression") != "2 + 2":
        print("ERROR: Invalid calculation.expression")
        return 1

    if calculation.get("result") != 4:
        print("ERROR: Invalid calculation.result")
        return 1

    print("OK: JSON output is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
