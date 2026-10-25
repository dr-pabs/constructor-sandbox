"""Greeting helpers."""

import argparse
from typing import Optional, Sequence


def greet(name: str) -> str:
    return f"Hello, {name}!"


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Print a greeting.")
    parser.add_argument("name", help="name to greet")
    args = parser.parse_args(argv)
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
