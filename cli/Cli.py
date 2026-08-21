import typer

from parser.yaml_parser import load_yaml
from schemas.validator import validate_config
from generators.terraform_generator import TerraformGenerator
from generators.ansible_generator import AnsibleGenerator
from executor.deployment_manager import DeploymentManager
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
            logger.info("Configuration validated: %s", file)
        else:
            typer.secho(
                f"✗ {message}",
                fg=typer.colors.RED
            )

    except (FileNotFoundError, ValueError) as error:
        typer.secho(
            f"✗ Error: {error}",
            fg=typer.colors.RED
        )


@app.command()
def generate(
    file: str,
    target: str = typer.Option(
        "terraform",
        help="Target: terraform or ansible"
    )
):
    """Generate Infrastructure as Code."""

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
                "✗ Unsupported target.",
                fg=typer.colors.RED
            )
            return

        output_file = generator.generate(config)

        typer.secho(
            f"✓ Generated: {output_file}",
            fg=typer.colors.GREEN
        )

        logger.info(
            "Generated %s: %s",
            target,
            output_file
        )

    except (FileNotFoundError, ValueError) as error:
        typer.secho(
            f"✗ Error: {error}",
            fg=typer.colors.RED
        )


@app.command()
def terraform_validate(
    directory: str = "output/terraform"
):
    """Validate generated Terraform configuration."""

    manager = DeploymentManager()

    result = manager.validate_terraform(directory)

    if result["returncode"] == 0:
        typer.secho(
            "✓ Terraform configuration is valid.",
            fg=typer.colors.GREEN
        )
    else:
        typer.secho(
            result["stderr"],
            fg=typer.colors.RED
        )


@app.command()
def terraform_plan(
    directory: str = "output/terraform"
):
    """Create a Terraform execution plan."""

    manager = DeploymentManager()

    result = manager.plan_terraform(directory)

    typer.echo(result["stdout"])

    if result["returncode"] != 0:
        typer.secho(
            result["stderr"],
            fg=typer.colors.RED
        )


@app.command()
def version():
    """Show AutoDevOps version."""

    typer.echo("AutoDevOps v1.0.0")


if __name__ == "__main__":
    app()
