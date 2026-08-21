from pathlib import Path

from generators.template_engine import TemplateEngine


class AnsibleGenerator:
    """Generate Ansible inventory from YAML data."""

    def __init__(self):
        self.engine = TemplateEngine("templates/ansible")

    def generate(self, config, output_directory="output/ansible"):
        output_path = Path(output_directory)
        output_path.mkdir(parents=True, exist_ok=True)

        content = self.engine.render(
            "inventory.ini.j2",
            config
        )

        file_path = output_path / "inventory.ini"
        file_path.write_text(content, encoding="utf-8")

        return file_path
