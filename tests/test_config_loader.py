from parser.config_loader import ConfigLoader


def test_config_loader():

    loader = ConfigLoader()

    config = loader.load("examples/sample.yaml")

    assert isinstance(config, dict)
    assert "resources" in config
    assert len(config["resources"]) > 0
