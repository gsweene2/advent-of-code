from unittest.mock import patch

from advent_of_code.y2022.d5 import (
    solution_1,
    solution_2,
)


@patch("advent_of_code.y2022.d5._get_file_as_list")
def test_solution_1(mock__get_file_as_list):
    # Arrange
    input_list = [
        b"mock_data",
    ]
    mock__get_file_as_list.return_value = input_list

    # Act
    r = solution_1("https://some-fake-url.com/input")

    # Assert
    assert 0 == r


@patch("advent_of_code.y2022.d5._get_file_as_list")
def test_solution_2(mock__get_file_as_list):
    # Arrange
    input_list = [
        b"mock_data",
    ]
    mock__get_file_as_list.return_value = input_list

    # Act
    r = solution_2("https://some-fake-url.com/input")

    # Assert
    assert 0 == r
