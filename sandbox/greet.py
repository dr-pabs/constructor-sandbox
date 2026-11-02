"""Greeting CLI: ``python -m sandbox.greet <name>``."""

import sys


def greet(name: str) -> str:
    """Return a greeting for ``name``."""
    return f"Hello, {name}!"


def main(argv=None) -> None:
    """Print a greeting for the name in ``argv[1]``; exit non-zero if missing."""
    if argv is None:
        argv = sys.argv
    if len(argv) < 2:
        print("usage: python -m sandbox.greet <name>", file=sys.stderr)
        sys.exit(2)
    print(greet(argv[1]))


if __name__ == "__main__":
    main()
