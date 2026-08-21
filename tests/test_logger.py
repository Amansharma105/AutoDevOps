from logs.logger import get_logger


def test_logger():

    logger = get_logger("test")

    assert logger is not None
    assert logger.name == "test"
