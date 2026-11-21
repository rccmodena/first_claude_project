import pytest

from first_claude_project.cli import main


def test_cli_default(capsys: pytest.CaptureFixture[str]) -> None:
    assert main([]) == 0
    assert capsys.readouterr().out == "Hello, world!\n"


def test_cli_with_name(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--name", "Ada"]) == 0
    assert capsys.readouterr().out == "Hello, Ada!\n"


def test_cli_empty_name_fails(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--name", " "]) == 2
    assert "must not be empty" in capsys.readouterr().err


def test_cli_with_greet(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--name", "Ada", "--greet", "Hi"]) == 0
    assert capsys.readouterr().out == "Hi, Ada!\n"


def test_cli_greet_without_name(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--greet", "Ciao"]) == 0
    assert capsys.readouterr().out == "Ciao, world!\n"


def test_cli_empty_greet_fails(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--greet", " "]) == 2
    assert "greeting must not be empty" in capsys.readouterr().err
