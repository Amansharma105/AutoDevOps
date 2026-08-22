from health_check import check_project_structure


def test_project_structure():

    missing = check_project_structure()

    assert missing == []
