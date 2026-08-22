from parser.config_loader import ConfigLoader


def test_config_loader():

    loader = ConfigLoader()

    config = loader.load("examples/sample.yaml")

    assert isinstance(config, dict)
    assert "resources" in config
    assert len(config["resources"]) > 0


def test_supported_extensions():

    loader = ConfigLoader()

    assert ".yaml" in loader.SUPPORTED_EXTENSIONS
    assert ".yml" in loader.SUPPORTED_EXTENSIONS
