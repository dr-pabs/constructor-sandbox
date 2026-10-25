from sandbox.greet import greet


def test_greet() -> None:
    assert greet("World") == "Hello, World!"


def test_main_prints_greeting(capsys) -> None:
    from sandbox.greet import main

    assert main(["Alice"]) == 0
    assert capsys.readouterr().out == "Hello, Alice!\n"
