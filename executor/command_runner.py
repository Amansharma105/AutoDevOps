import subprocess

from executor.execution_result import ExecutionResult


class CommandRunner:
    """Safely execute infrastructure commands."""

    def run(self, command):
        """Run a command and return a structured result."""

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=False
            )

            return ExecutionResult(
                returncode=result.returncode,
                stdout=result.stdout,
                stderr=result.stderr
            )

        except Exception as error:
            return ExecutionResult(
                returncode=1,
                stdout="",
                stderr=str(error)
            )
