import json
from pathlib import Path

from jsonschema import ValidationError, validate


def load_schema(schema_path=None):
    """Load the JSON schema used to validate YAML configurations."""
    if schema_path is None:
        schema_path = Path(__file__).parent / "config_schema.json"

    with open(schema_path, "r", encoding="utf-8") as file:
        return json.load(file)


def validate_config(config, schema_path=None):
    """Validate a configuration dictionary against the project schema."""
    schema = load_schema(schema_path)

    try:
        validate(instance=config, schema=schema)
        return True, "Configuration is valid."

    except ValidationError as error:
        message = error.message
        return False, f"Configuration validation failed: {message}"
