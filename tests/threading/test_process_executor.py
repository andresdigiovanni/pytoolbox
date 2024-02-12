from pytoolbox.threading.process_executor import process_executor


def return_identity(num):
    return num


def sum_n_nums(nums):
    return sum(nums)


def sum_2_nums(a, b):
    return a + b


def sum_3_nums(a, b, c):
    return a + b + c


def test_no_parameters():
    # Arrange
    items = [1, 2, 3]

    # Act
    result = list(process_executor(return_identity, items))

    # Assert
    result = sorted(result)
    assert result == [1, 2, 3]


def test_input_as_number():
    # Arrange
    items = [1, 2, 3]

    # Act
    result = list(process_executor(sum_2_nums, items, 100))

    # Assert
    result = sorted(result)
    assert result == [101, 102, 103]


def test_input_as_tuple():
    # Arrange
    items = [(1, 2), (2, 3), (3, 4)]

    # Act
    result = list(process_executor(sum_3_nums, items, 100))

    # Assert
    result = sorted(result)
    assert result == [103, 105, 107]


def test_input_as_list():
    # Arrange
    items = [[1, 2], [2, 3], [3, 4]]

    # Act
    result = list(process_executor(sum_n_nums, items))

    # Assert
    result = sorted(result)
    assert result == [3, 5, 7]


def test_no_args():
    # Arrange
    items = [(1, 2), (2, 3), (3, 4)]

    # Act
    result = list(process_executor(sum_2_nums, items))

    # Assert
    result = sorted(result)
    assert result == [3, 5, 7]
