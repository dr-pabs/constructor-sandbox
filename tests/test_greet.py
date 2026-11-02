import subprocess
import sys
from pathlib import Path

from sandbox.greet import greet

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_greet_returns_greeting():
    assert greet("Ada") == "Hello, Ada!"


def test_cli_prints_greeting():
    result = subprocess.run(
        [sys.executable, "-m", "sandbox.greet", "Ada"],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "Hello, Ada!"
