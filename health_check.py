from pathlib import Path


def check_project_structure():
    """Check whether the main AutoDevOps directories exist."""

    required_paths = [
        Path("cli"),
        Path("parser"),
        Path("schemas"),
        Path("templates"),
        Path("generators"),
        Path("executor"),
        Path("logs"),
        Path("tests"),
        Path("examples"),
        Path("output"),
    ]

    missing = [
        str(path)
        for path in required_paths
        if not path.exists()
    ]

    return missing


if __name__ == "__main__":
    missing_paths = check_project_structure()

    if missing_paths:
        print("Missing project paths:")
        for path in missing_paths:
            print(f"- {path}")
    else:
        print("✓ AutoDevOps project structure is ready.")
