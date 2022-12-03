import responses
from unittest.mock import patch

from advent_of_code.y2022.d1 import find_largest_sum, _get_file_as_list, sum_n_largest_sums


@patch("advent_of_code.y2022.d1._get_file_as_list")
def test__find_largest_sum(mock__get_file_as_list):
    # Arrange
    input_list = [
        b"1000",
        b"2000",
        b"3000",
        b"",
        b"4000",
        b"",
        b"5000",
        b"6000",
        b"",
        b"7000",
        b"8000",
        b"9000",
        b"",
        b"10000",
    ]
    mock__get_file_as_list.return_value = input_list

    # Act
    r = find_largest_sum("https://some-fake-url.com/input")

    # Assert
    assert 24000 == r


@patch("advent_of_code.y2022.d1._get_file_as_list")
def test__find_largest_sum(mock__get_file_as_list):
    # Arrange
    input_list = [
        b"1000",
        b"2000",
        b"3000",
        b"",
        b"4000",
        b"",
        b"5000",
        b"6000",
        b"",
        b"7000",
        b"8000",
        b"9000",
        b"",
        b"10000",
    ]
    mock__get_file_as_list.return_value = input_list

    # Act
    r = sum_n_largest_sums("https://some-fake-url.com/input", 3)

    # Assert
    assert 45000 == r


@responses.activate
def test___get_file_as_list():
    # Arrange
    file_bytes = b"1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
    responses.add(
        responses.GET, "https://some-fake-url.com/input", body=file_bytes, status=200
    )

    # Act
    r = _get_file_as_list("https://some-fake-url.com/input")

    # Assert
    expected = [
        b"1000",
        b"2000",
        b"3000",
        b"",
        b"4000",
        b"",
        b"5000",
        b"6000",
        b"",
        b"7000",
        b"8000",
        b"9000",
        b"",
        b"10000",
    ]
    assert expected == r
