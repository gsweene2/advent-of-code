import responses

from advent_of_code.y2022.util import _get_file_as_list


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
