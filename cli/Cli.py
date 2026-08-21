import typer

from parser.yaml_parser import load_yaml
from schemas.validator import validate_config
from generators.terraform_generator import TerraformGenerator
from generators.ansible_generator import AnsibleGenerator
from logs.logger import get_logger

app = typer.Typer(
    help="AutoDevOps - Infrastructure as Code Generator & Cloud Deployer"
)

logger = get_logger()


@app.command()
def validate(file: str):
    """Validate a YAML infrastructure configuration."""

    try:
        config = load_yaml(file)
        is_valid, message = validate_config(config)

        if is_valid:
            typer.secho(
                "✓ Configuration is valid.",
                fg=typer.colors.GREEN
            )
            logger.info("Configuration validated successfully: %s", file)
        else:
            typer.secho(
                f"✗ {message}",
                fg=typer.colors.RED
            )
            logger.error("Configuration validation failed: %s", file)

    except (FileNotFoundError, ValueError) as error:
        typer.secho(
            f"✗ Error: {error}",
            fg=typer.colors.RED
        )
        logger.error("Validation error: %s", error)


@app.command()
def generate(
    file: str,
    target: str = typer.Option(
        "terraform",
        help="Target generator: terraform or ansible"
    )
):
    """Generate Infrastructure as Code from a YAML file."""

    try:
        config = load_yaml(file)

        is_valid, message = validate_config(config)

        if not is_valid:
            typer.secho(
                f"✗ {message}",
                fg=typer.colors.RED
            )
            return

        if target == "terraform":
            generator = TerraformGenerator()
        elif target == "ansible":
            generator = AnsibleGenerator()
        else:
            typer.secho(
                "✗ Unsupported target. Use terraform or ansible.",
                fg=typer.colors.RED
            )
            return

        output_file = generator.generate(config)

        typer.secho(
            f"✓ Generated: {output_file}",
            fg=typer.colors.GREEN
        )

        logger.info(
            "Generated %s configuration: %s",
            target,
            output_file
        )

    except (FileNotFoundError, ValueError) as error:
        typer.secho(
            f"✗ Error: {error}",
            fg=typer.colors.RED
        )
        logger.error("Generation error: %s", error)


@app.command()
def version():
    """Show AutoDevOps version."""

    typer.echo("AutoDevOps v1.0.0")


if __name__ == "__main__":
    app()
