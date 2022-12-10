from typing import Tuple

from advent_of_code.y2022.util import _get_file_as_list

URL = "https://adventofcode.com/2022/day/4/input"


def count_overlaps(input_url: str) -> int:
    assignments = _get_file_as_list(input_url)
    total = 0
    for a in assignments:
        e1s, e1e, e2s, e2e = _parse_assignment(a)
        if _is_contained(e1s, e1e, e2s, e2e):
            total += 1
    return total


def _parse_assignment(a: bytes) -> Tuple[int, int, int, int]:
    a_list = a.decode("utf-8").split(",")
    e1, e2 = a_list[0].split("-"), a_list[1].split("-")
    return int(e1[0]), int(e1[1]), int(e2[0]), int(e2[1])


def _is_contained(a_start, a_end, b_start, b_end) -> bool:
    if a_start <= b_start and a_end >= b_end:
        return True
    if a_start >= b_start and a_end <= b_end:
        return True
    return False


if __name__ == "__main__":
    r = count_overlaps(URL)
    print(f"Overlaps: {r}")
