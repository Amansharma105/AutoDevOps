from typer.testing import CliRunner

from cli.cli import app


runner = CliRunner()


def test_version():
    result = runner.invoke(
        app,
        ["version"]
    )

    assert result.exit_code == 0
    assert "AutoDevOps v1.0.0" in result.stdout


def test_validate_sample():
    result = runner.invoke(
        app,
        ["validate", "examples/sample.yaml"]
    )

    assert result.exit_code == 0
    assert "Configuration is valid" in result.stdout


def test_invalid_file():
    result = runner.invoke(
        app,
        ["validate", "examples/missing.yaml"]
    )

    assert result.exit_code == 0
    assert "Error" in result.stdout


def test_list_output():
    result = runner.invoke(
        app,
        ["list-output"]
    )

    assert result.exit_code == 0


def test_clear_output():
    result = runner.invoke(
        app,
        ["clear-output", "terraform"]
    )

    assert result.exit_code == 0
