 from executor.command_runner import CommandRunner


class TerraformExecutor:
    """Execute Terraform commands."""

    def __init__(self):
        self.runner = CommandRunner()

    def init(self, directory):
        return self.runner.run(
            ["terraform", f"-chdir={directory}", "init"]
        )

    def validate(self, directory):
        return self.runner.run(
            ["terraform", f"-chdir={directory}", "validate"]
        )

    def plan(self, directory):
        return self.runner.run(
            ["terraform", f"-chdir={directory}", "plan"]
        )
