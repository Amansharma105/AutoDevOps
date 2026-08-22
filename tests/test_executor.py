from executor.command_runner import CommandRunner


def test_command_runner():

    runner = CommandRunner()

    result = runner.run(
        ["python", "-c", "print('AutoDevOps')"]
    )

    assert result.success is True
    assert result.returncode == 0
    assert "AutoDevOps" in result.stdout
