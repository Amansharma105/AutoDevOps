from pathlib import Path

from generators.template_engine import TemplateEngine


class TerraformGenerator:
    """Generate Terraform configuration from YAML data."""

    def __init__(self):
        self.engine = TemplateEngine("templates/terraform")

    def generate(self, config, output_directory="output/terraform"):
        output_path = Path(output_directory)
        output_path.mkdir(parents=True, exist_ok=True)

        content = self.engine.render(
            "main.tf.j2",
            config
        )

        file_path = output_path / "main.tf"
        file_path.write_text(content, encoding="utf-8")

        return file_path
