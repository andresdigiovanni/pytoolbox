import pytest

from pytoolbox.decorators.utils.retry import retry


def test_successful_execution():
    # Arrange
    @retry()
    def func():
        return True

    # Act
    result = func()

    # Assert
    assert result


def test_successful_execution_after_multiple_attempts():
    # Arrange
    count = 0

    @retry()
    def func():
        nonlocal count
        count += 1
        if count < 3:
            raise Exception("Failed")
        return True

    # Act
    result = func()

    # Assert
    assert result


def test_function_fails_on_all_attempts():
    # Arrange
    @retry()
    def func():
        raise Exception("Failed")

    # Act & Assert
    with pytest.raises(Exception):
        func()


# Tests that the function can accept arguments and keyword arguments
def test_function_accepts_arguments_and_keyword_arguments():
    # Arrange
    @retry(max_tries=2, delay_seconds=0.5)
    def func(x, y=1):
        return x + y

    # Act
    result = func(1, y=2)

    # Assert
    assert result == 3
