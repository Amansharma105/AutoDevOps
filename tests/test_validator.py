from parser.yaml_parser import load_yaml
from schemas.validator import validate_config


def test_sample_configuration():
    config = load_yaml("examples/sample.yaml")

    is_valid, message = validate_config(config)

    assert is_valid is True
    assert message == "Configuration is valid."
