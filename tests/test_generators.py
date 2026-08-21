from generators.terraform_generator import TerraformGenerator
from generators.ansible_generator import AnsibleGenerator


def sample_config():
    return {
        "resources": [
            {
                "name": "web-server",
                "type": "web_server",
                "provider": "aws",
                "region": "ap-south-1",
                "instance_type": "t2.micro",
            }
        ]
    }


def test_terraform_generator(tmp_path):
    generator = TerraformGenerator()

    file_path = generator.generate(
        sample_config(),
        tmp_path / "terraform"
    )

    assert file_path.exists()
    assert file_path.name == "main.tf"


def test_ansible_generator(tmp_path):
    generator = AnsibleGenerator()

    file_path = generator.generate(
        sample_config(),
        tmp_path / "ansible"
    )

    assert file_path.exists()
    assert file_path.name == "inventory.ini"
