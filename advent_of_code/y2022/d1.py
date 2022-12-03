from typing import List

from advent_of_code.y2022.util import _get_file_as_list

URL = "https://adventofcode.com/2022/day/1/input"


def find_largest_sum(sums_url) -> int:
    inputs_list = _get_file_as_list(sums_url)
    if inputs_list[-1]:
        inputs_list.append(b"")
    local_sum, max_sum = 0, float("-inf")
    for i in inputs_list:
        if not i:
            max_sum = max(local_sum, max_sum)
            local_sum = 0
        else:
            local_sum += int(i)
    return max_sum


def sum_n_largest_sums(sums_url, num_sums) -> int:
    inputs_list = _get_file_as_list(sums_url)
    if inputs_list[-1]:
        inputs_list.append(b"")
    local_sum, sums = 0, []
    for i in inputs_list:
        if not i:
            if not sums:
                sums = [local_sum]
            else:
                sums.append(local_sum)
            local_sum = 0
        else:
            local_sum += int(i)

    if not sums or num_sums > len(sums):
        raise Exception("More sums requested than exist")

    return sum(sorted(sums, reverse=True)[:num_sums])


if __name__ == "__main__":
    r = find_largest_sum(URL)
    print(f"Max Sum: {r}")

    r = sum_n_largest_sums(URL, 3)
    print(f"Sum of 3 largest sums: {r}")
