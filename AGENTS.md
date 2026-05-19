# Repository Guidelines

## Project Structure & Module Organization
This repository is intentionally small and Python-first.
- `main.py`: primary entrypoint; currently runs a simple demo flow.
- `lib.py`: helper functions used for lightweight examples/utilities.
- `index.html`: standalone static page asset.
- `README.md`: minimal project overview.

Keep top-level modules focused and single-purpose. If functionality grows, add a `tests/` directory for automated coverage and group features into clearly named modules.

## Build, Test, and Development Commands
- `python3 main.py`: run the current application entrypoint locally.
- `python3 -m py_compile main.py lib.py`: validate Python syntax quickly.
- `python3 -m pytest`: run tests (use once tests are added).

For iterative work, run syntax checks before committing to catch basic issues early.

## Coding Style & Naming Conventions
Use standard Python conventions:
- 4-space indentation, UTF-8 text files, and explicit newlines.
- `snake_case` for functions and variables (for example, `third_dummy_function`).
- Keep functions short and clear; prefer descriptive names over comments.

Match existing style in `main.py` and `lib.py`, and avoid introducing unrelated formatting changes in the same commit.

## Testing Guidelines
No formal test suite is committed yet. Until one is added:
- Validate runtime behavior with `python3 main.py`.
- Run `python3 -m py_compile main.py lib.py` before opening a PR.

When adding tests, use `pytest` with files named `test_*.py` under `tests/`, and cover both expected behavior and edge cases for new logic.

## Commit & Pull Request Guidelines
Recent history uses short, imperative commit messages (for example, `added new function`). Prefer:
- `add third dummy function to lib.py`
- `update main entrypoint output`

For pull requests, include:
- A brief summary of what changed and why.
- The list of modified files.
- Validation steps and command output used to verify changes.
- Linked issue/ticket when applicable.
