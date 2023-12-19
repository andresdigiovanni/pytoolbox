import pytest

from pytoolbox.decorators.logging.log_execution import log_execution


def test_log_execution_returns_correct_result():
    # Arrange
    @log_execution
    def add(a, b):
        return a + b

    # Act
    result = add(2, 3)

    # Assert
    assert result == 5


def test_log_execution_with_no_arguments():
    # Arrange
    @log_execution
    def hello_world():
        return "Hello, World!"

    # Act
    result = hello_world()

    # Assert
    assert result == "Hello, World!"


def test_log_execution_with_keyword_arguments():
    # Arrange
    @log_execution
    def greet(name):
        return f"Hello, {name}!"

    # Act
    result = greet(name="Alice")

    # Assert
    assert result == "Hello, Alice!"


def test_log_execution_with_positional_and_keyword_arguments():
    # Arrange
    @log_execution
    def greet(name, greeting):
        return f"{greeting}, {name}!"

    # Act
    result = greet("Alice", greeting="Hi")

    # Assert
    assert result == "Hi, Alice!"


def test_log_execution_with_exception_raised():
    # Arrange
    @log_execution
    def divide(a, b):
        return a / b

    # Act & Assert
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
