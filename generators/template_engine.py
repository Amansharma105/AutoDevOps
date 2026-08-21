from pathlib import Path

from jinja2 import Environment, FileSystemLoader


class TemplateEngine:
    """Render Jinja2 templates for infrastructure generation."""

    def __init__(self, template_directory="templates"):
        self.template_directory = Path(template_directory)

        self.environment = Environment(
            loader=FileSystemLoader(self.template_directory),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def render(self, template_name, context):
        """Render a template with the supplied configuration."""
        template = self.environment.get_template(template_name)
        return template.render(**context)
