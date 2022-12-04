from advent_of_code.y2022.util import _get_file_as_list

URL = "https://adventofcode.com/2022/day/3/input"


def count_priorities(input_url):
    inputs_list = _get_file_as_list(input_url)
    total = 0
    for input in inputs_list:
        i_str = input.decode("utf-8")
        halves = i_str[: len(i_str) // 2], i_str[len(i_str) // 2 :]
        r = set(list(halves[0])).intersection(set(list(halves[1])))
        total += _get_priority(r)
    return total


def _get_priority(s):
    p = ord(next(iter(s))) - 96
    return p if p > 0 else p + 58


if __name__ == "__main__":
    r = count_priorities(URL)
    print(f"Sum priorities: {r}")
