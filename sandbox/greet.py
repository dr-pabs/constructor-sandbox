import sys


def greet(name: str) -> str:
    return f"Hello, {name}!"


def main() -> None:
    name = sys.argv[1]
    print(greet(name))


if __name__ == "__main__":
    main()
