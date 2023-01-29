import os
import sys

year, day = sys.argv[1], sys.argv[2]

sln = f"""from typing import Any

from advent_of_code.y2022.util import _get_file_as_list

URL = "https://adventofcode.com/2022/day/{day}/input"


def solution_1(input) -> Any:
    input_list = _get_file_as_list(input)
    # Solution
    return None


def solution_2(input) -> Any:
    input_list = _get_file_as_list(input)
    # Solution
    return None


if __name__ == "__main__":
    r = solution_1(URL)
    print("Solution 1:" + r)

    r = solution_2(URL)
    print("Solution 2:" + r)
"""

print(f"Current dir is {os.getcwd()}...")

sln_file = f"advent_of_code/y{year}/d{day}.py"

print(f"Creating solution file at {sln_file}...")

os.makedirs(os.path.dirname(sln_file), exist_ok=True)

with open(sln_file, "w") as f:
    f.write(sln)

test = f"""from unittest.mock import patch

from advent_of_code.y2022.d{day} import (
    solution_1,
    solution_2,
)


@patch("advent_of_code.y2022.d{day}._get_file_as_list")
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


@patch("advent_of_code.y2022.d{day}._get_file_as_list")
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
"""

test_file = f"tests/y{year}/d{day}_test.py"

print(f"Creating test file at {test_file}...")

with open(test_file, "w") as f:
    f.write(test)

print("Done! Check `git diff --name-only` to verify correct files.")
