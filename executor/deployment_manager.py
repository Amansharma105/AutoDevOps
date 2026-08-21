from executor.terraform_executor import TerraformExecutor


class DeploymentManager:
    """Manage infrastructure deployment operations."""

    def __init__(self):
        self.terraform = TerraformExecutor()

    def validate_terraform(self, directory):
        """Validate generated Terraform configuration."""
        return self.terraform.validate(directory)

    def plan_terraform(self, directory):
        """Create a Terraform execution plan."""
        return self.terraform.plan(directory)
