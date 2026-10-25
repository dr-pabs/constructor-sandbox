import subprocess
import sys
from pathlib import Path

from sandbox.greet import greet, main

REPO_ROOT = Path(__file__).resolve().parent.parent


def run_cli(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", "sandbox.greet", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=30,
    )


def test_greet() -> None:
    assert greet("World") == "Hello, World!"


def test_greet_ada() -> None:
    assert greet("Ada") == "Hello, Ada!"


def test_main_prints_greeting(capsys) -> None:
    assert main(["Alice"]) == 0
    assert capsys.readouterr().out == "Hello, Alice!\n"


def test_cli_prints_greeting() -> None:
    result = run_cli("Ada")
    assert result.returncode == 0
    assert result.stdout == "Hello, Ada!\n"


def test_cli_missing_argument_exits_nonzero() -> None:
    result = run_cli()
    assert result.returncode != 0
    assert result.stdout == ""
    assert "name" in result.stderr
