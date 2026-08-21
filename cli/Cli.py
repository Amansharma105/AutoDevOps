import typer

from parser.yaml_parser import load_yaml
from schemas.validator import validate_config

app = typer.Typer(
    help="AutoDevOps - Infrastructure as Code Generator and Cloud Deployer"
)


@app.command()
def validate(file: str):
    """Validate a YAML configuration file."""

    try:
        config = load_yaml(file)
        is_valid, message = validate_config(config)

        if is_valid:
            typer.secho(
                "✓ Configuration is valid.",
                fg=typer.colors.GREEN
            )
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
def version():
    """Show the AutoDevOps version."""

    typer.echo("AutoDevOps v1.0.0")


if __name__ == "__main__":
    app()
