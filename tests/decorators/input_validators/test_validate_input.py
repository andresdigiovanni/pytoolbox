import pytest

from pytoolbox.decorators.input_validators import validate_input


def test_valid_inputs():
    # Arrange
    @validate_input(lambda x: isinstance(x, int))
    def func(a, b):
        return a + b

    # Act
    result = func(1, 2)

    # Assert
    assert result == 3


def test_multiple_valid_inputs():
    # Arrange
    @validate_input(lambda x: isinstance(x, int), lambda x: isinstance(x, str))
    def func(a, b):
        return f"{a}{b}"

    # Act
    result = func(1, "a")

    # Assert
    assert result == "1a"


def test_no_inputs():
    # Arrange
    @validate_input()
    def func():
        return "no inputs"

    # Act
    result = func()

    # Assert
    assert result == "no inputs"


def test_invalid_input():
    # Arrange
    @validate_input(lambda x: isinstance(x, int))
    def func(a):
        return a

    # Act & Assert
    with pytest.raises(ValueError):
        func("a")


def test_too_many_inputs():
    # Arrange
    @validate_input(lambda x: isinstance(x, int))
    def func(a):
        return a

    # Act & Assert
    with pytest.raises(TypeError):
        func(1, 2)


def test_invalid_keyword_argument():
    # Arrange
    @validate_input(lambda x: isinstance(x, int))
    def func(a):
        return a

    # Act & Assert
    with pytest.raises(TypeError):
        func(b=1)
