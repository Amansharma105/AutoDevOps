from executor.terraform_executor import TerraformExecutor
from logs.logger import get_logger


class DeploymentManager:
    """Manage infrastructure deployment operations."""

    def __init__(self):
        self.terraform = TerraformExecutor()
        self.logger = get_logger("deployment")

    def validate_terraform(self, directory):
        """Validate generated Terraform configuration."""

        self.logger.info(
            "Validating Terraform configuration: %s",
            directory
        )

        result = self.terraform.validate(directory)

        if result.success:
            self.logger.info("Terraform validation successful.")
        else:
            self.logger.error(
                "Terraform validation failed: %s",
                result.stderr
            )

        return result

    def plan_terraform(self, directory):
        """Create a Terraform execution plan."""

        self.logger.info(
            "Creating Terraform plan: %s",
            directory
        )

        result = self.terraform.plan(directory)

        if result.success:
            self.logger.info("Terraform plan completed.")
        else:
            self.logger.error(
                "Terraform plan failed: %s",
                result.stderr
            )

        return result
        
