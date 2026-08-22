
    import typer

from parser.config_loader import ConfigLoader
from parser.config_summary import ConfigSummary

from schemas.validator import validate_config

from generators.terraform_generator import TerraformGenerator
from generators.ansible_generator import AnsibleGenerator
from generators.output_manager import OutputManager

from executor.deployment_manager import DeploymentManager

from logs.logger import get_logger

from health_check import check_project_structure


app = typer.Typer(
    help="AutoDevOps - Infrastructure as Code Generator & Cloud Deployer"
)

logger = get_logger()
config_loader = ConfigLoader()
config_summary = ConfigSummary()
output_manager = OutputManager()


@app.command()
def validate(file: str):
    """Validate a YAML infrastructure configuration."""

    try:
        config = config_loader.load(file)
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
def summary(file: str):
    """Show a summary of the infrastructure configuration."""

    try:
        config = config_loader.load(file)

        is_valid, message = validate_config(config)

        if not is_valid:
            typer.secho(
                f"✗ {message}",
                fg=typer.colors.RED
            )
            return

        result = config_summary.create(config)

        typer.echo(
            f"Total resources: {result['total_resources']}"
        )

        typer.echo("Resource types:")

        for resource_type, count in result["resource_types"].items():
            typer.echo(
                f"  {resource_type}: {count}"
            )

        typer.echo("Providers:")

        for provider, count in result["providers"].items():
            typer.echo(
                f"  {provider}: {count}"
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
        help="Target generator: terraform or ansible"
    )
):
    """Generate Infrastructure as Code."""

    try:
        config = config_loader.load(file)

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


@app.command()
def health():
    """Check the AutoDevOps project structure."""

    missing = check_project_structure()

    if missing:
        typer.secho(
            "✗ Project structure is incomplete.",
            fg=typer.colors.RED
        )

        for path in missing:
            typer.echo(f"- Missing: {path}")

        return

    typer.secho(
        "✓ AutoDevOps project structure is ready.",
        fg=typer.colors.GREEN
    )


@app.command()
def terraform_validate(
    directory: str = "output/terraform"
):
    """Validate generated Terraform configuration."""

    manager = DeploymentManager()
    result = manager.validate_terraform(directory)

    if result.success:
        typer.secho(
            "✓ Terraform configuration is valid.",
            fg=typer.colors.GREEN
        )
    else:
        typer.secho(
            result.stderr,
            fg=typer.colors.RED
        )


@app.command()
def terraform_plan(
    directory: str = "output/terraform"
):
    """Create a Terraform execution plan."""

    manager = DeploymentManager()
    result = manager.plan_terraform(directory)

    if result.stdout:
        typer.echo(result.stdout)

    if not result.success:
        typer.secho(
            result.stderr,
            fg=typer.colors.RED
        )


@app.command()
def ansible_ping(
    inventory: str = "output/ansible/inventory.ini"
):
    """Check Ansible host connectivity."""

    manager = DeploymentManager()
    result = manager.ping_ansible(inventory)

    if result.stdout:
        typer.echo(result.stdout)

    if not result.success:
        typer.secho(
            result.stderr,
            fg=typer.colors.RED
        )


@app.command()
def ansible_check(
    playbook: str,
    inventory: str = None
):
    """Check Ansible playbook syntax."""

    manager = DeploymentManager()

    result = manager.check_ansible_playbook(
        playbook,
        inventory
    )

    if result.stdout:
        typer.echo(result.stdout)

    if result.success:
        typer.secho(
            "✓ Ansible playbook syntax is valid.",
            fg=typer.colors.GREEN
        )
    else:
        typer.secho(
            result.stderr,
            fg=typer.colors.RED
        )


@app.command()
def list_output(
    target: str = typer.Option(
        None,
        help="Optional target: terraform or ansible"
    )
):
    """List generated infrastructure files."""

    files = output_manager.list_files(target)

    if not files:
        typer.echo("No generated files found.")
        return

    for file_path in files:
        typer.echo(str(file_path))


@app.command()
def clear_output(
    target: str = typer.Argument(...)
):
    """Clear generated files for a target."""

    removed = output_manager.clear_target(target)

    typer.secho(
        f"✓ Removed {removed} generated file(s).",
        fg=typer.colors.GREEN
    )


@app.command()
def version():
    """Show AutoDevOps version."""

    typer.echo("AutoDevOps v1.0.0")


if __name__ == "__main__":
    app()
