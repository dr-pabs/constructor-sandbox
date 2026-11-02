import subprocess
import sys
from pathlib import Path

from sandbox.greet import greet

REPO_ROOT = Path(__file__).resolve().parent.parent


def _run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "sandbox.greet", *args],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )


def test_greet() -> None:
    assert greet("Ada") == "Hello, Ada!"


def test_cli_greets_name() -> None:
    result = _run_cli("Ada")
    assert result.returncode == 0
    assert result.stdout == "Hello, Ada!\n"


def test_cli_without_name_exits_nonzero() -> None:
    result = _run_cli()
    assert result.returncode != 0
