from executor.command_runner import CommandRunner


class AnsibleExecutor:
    """Execute Ansible commands."""

    def __init__(self):
        self.runner = CommandRunner()

    def ping(self, inventory):
        """Check connectivity with Ansible hosts."""

        return self.runner.run(
            [
                "ansible",
                "all",
                "-i",
                inventory,
                "-m",
                "ping"
            ]
        )

    def check_playbook(self, playbook, inventory=None):
        """Check an Ansible playbook without executing it."""

        command = [
            "ansible-playbook",
            "--syntax-check",
            playbook
        ]

        if inventory:
            command.extend(["-i", inventory])

        return self.runner.run(command)
