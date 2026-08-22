from parser.config_summary import ConfigSummary


def test_config_summary():

    config = {
        "resources": [
            {
                "name": "web-server",
                "type": "web_server",
                "provider": "aws"
            },
            {
                "name": "database",
                "type": "database",
                "provider": "aws"
            }
        ]
    }

    summary = ConfigSummary().create(config)

    assert summary["total_resources"] == 2
    assert summary["resource_types"]["web_server"] == 1
    assert summary["resource_types"]["database"] == 1
    assert summary["providers"]["aws"] == 2
