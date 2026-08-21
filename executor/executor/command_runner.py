import subprocess


class CommandRunner:
    """Safely execute infrastructure commands."""

    def run(self, command):
        """Run a command and return its output."""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                check=False
            )

            return {
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr
            }

        except Exception as error:
            return {
                "returncode": 1,
                "stdout": "",
                "stderr": str(error)
            }
