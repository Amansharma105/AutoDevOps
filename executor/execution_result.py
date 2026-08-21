from dataclasses import dataclass


@dataclass
class ExecutionResult:
    """Store the result of an infrastructure command."""

    returncode: int
    stdout: str
    stderr: str

    @property
    def success(self):
        return self.returncode == 0
