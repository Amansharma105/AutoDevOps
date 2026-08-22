from executor.deployment_manager import DeploymentManager


def test_deployment_manager():

    manager = DeploymentManager()

    assert manager is not None
    assert manager.terraform is not None
    assert manager.logger is not None
