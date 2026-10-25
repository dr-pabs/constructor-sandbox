from sandbox.greet import greet


def test_greet() -> None:
    assert greet("World") == "Hello, World!"
