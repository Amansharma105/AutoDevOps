from generators.output_manager import OutputManager


def test_output_manager(tmp_path):

    manager = OutputManager(tmp_path)

    directory = manager.get_target_directory("terraform")

    assert directory.exists()
    assert directory.name == "terraform"
    
