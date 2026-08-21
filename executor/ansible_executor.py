from executor.command_runner import CommandRunner


class AnsibleExecutor:
    """Execute Ansible commands."""

    def __init__(self):
        self.runner = CommandRunner()

    def ping(self, inventory):
        return self.runner.run(
            f"ansible all -i {inventory} -m ping"
        )
