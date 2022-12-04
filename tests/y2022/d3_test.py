from unittest.mock import patch

from advent_of_code.y2022.d3 import count_priorities, _get_priority


@patch("advent_of_code.y2022.d3._get_file_as_list")
def test_count_priorities(mock__get_file_as_list):
    # Arrange
    input_list = [
        b"vJrwpWtwJgWrhcsFMMfFFhFp",
        b"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        b"PmmdzqPrVvPwwTWBwg",
        b"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        b"ttgJtRGJQctTZtZT",
        b"CrZsJsPPZsGzwwsLwLmpwMDw",
    ]
    mock__get_file_as_list.return_value = input_list

    # Act
    r = count_priorities("https://some-fake-url.com/input")

    # Assert
    assert 157 == r


def test__get_priority():
    # Arragne
    # Act & Assert
    assert 1 == _get_priority("a")
    assert 26 == _get_priority("z")
    assert 27 == _get_priority("A")
    assert 52 == _get_priority("Z")
