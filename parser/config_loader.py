from pathlib import Path

from parser.yaml_parser import load_yaml


class ConfigLoader:
    """Load infrastructure configuration files."""

    SUPPORTED_EXTENSIONS = {".yaml", ".yml"}

    def load(self, file_path):
        path = Path(file_path)

        if path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
            raise ValueError(
                "Only .yaml and .yml configuration files are supported."
            )

        return load_yaml(path)
