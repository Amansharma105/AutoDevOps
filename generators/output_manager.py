from pathlib import Path


class OutputManager:
    """Manage generated Infrastructure as Code files."""

    def __init__(self, output_directory="output"):
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

    def get_target_directory(self, target):
        """Return the output directory for a target."""
        target_directory = self.output_directory / target

        target_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        return target_directory

    def list_files(self, target=None):
        """List generated files."""
        directory = self.output_directory

        if target:
            directory = directory / target

        if not directory.exists():
            return []

        return [
            path
            for path in directory.iterdir()
            if path.is_file()
        ]
