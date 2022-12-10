from unittest.mock import patch

from advent_of_code.y2022.d4 import count_overlaps, _is_contained, _parse_assignment


def test__is_contained() -> None:
    assert not _is_contained(2, 4, 6, 8)
    assert not _is_contained(2, 3, 4, 5)
    assert not _is_contained(5, 7, 7, 9)
    assert _is_contained(2, 8, 3, 7)
    assert _is_contained(6, 6, 4, 6)
    assert not _is_contained(2, 6, 4, 8)


def test__parse_assignment() -> None:
    assert (2, 4, 6, 8) == _parse_assignment(b"2-4,6-8")
    assert (200, 411, 633, 898) == _parse_assignment(b"200-411,633-898")


@patch("advent_of_code.y2022.d4._get_file_as_list")
def test_count_overlaps(mock__get_file_as_list):
    # Arrange
    input_list = [
        b"2-4,6-8",
        b"2-3,4-5",
        b"5-7,7-9",
        b"2-8,3-7",
        b"6-6,4-6",
        b"2-6,4-8",
    ]
    mock__get_file_as_list.return_value = input_list

    # Act
    r = count_overlaps("https://some-fake-url.com/input")

    # Assert
    assert 2 == r
