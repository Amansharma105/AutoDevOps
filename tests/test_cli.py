from typer.testing import CliRunner

from cli.cli import app


runner = CliRunner()


def test_version():

    result = runner.invoke(app, ["version"])

    assert result.exit_code == 0
    assert "AutoDevOps v1.0.0" in result.stdout


def test_validate_sample():

    result = runner.invoke(
        app,
        ["validate", "examples/sample.yaml"]
    )

    assert result.exit_code == 0
    assert "Configuration is valid" in result.stdout
