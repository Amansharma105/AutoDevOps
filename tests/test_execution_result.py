from executor.execution_result import ExecutionResult


def test_successful_execution():

    result = ExecutionResult(
        returncode=0,
        stdout="Success",
        stderr=""
    )

    assert result.success is True


def test_failed_execution():

    result = ExecutionResult(
        returncode=1,
        stdout="",
        stderr="Error"
    )

    assert result.success is False
