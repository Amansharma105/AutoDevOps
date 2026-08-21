from executor.command_runner import CommandRunner


def test_command_runner():

    runner = CommandRunner()

    result = runner.run("echo AutoDevOps")

    assert result["returncode"] == 0
    assert "AutoDevOps" in result["stdout"]
