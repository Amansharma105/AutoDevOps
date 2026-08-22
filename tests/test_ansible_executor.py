from executor.ansible_executor import AnsibleExecutor


def test_ansible_executor():

    executor = AnsibleExecutor()

    assert executor is not None
    assert executor.runner is not None
