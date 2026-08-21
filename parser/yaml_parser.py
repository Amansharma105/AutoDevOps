import yaml


def load_yaml(file_path):
    """Load YAML configuration from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        if data is None:
            return {}

        return data

    except FileNotFoundError:
        raise FileNotFoundError(f"YAML file not found: {file_path}")

    except yaml.YAMLError as error:
        raise ValueError(f"Invalid YAML configuration: {error}")
