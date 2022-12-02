from typing import List
import os
import requests

URL = "https://adventofcode.com/2022/day/1/input"
SESSION = os.environ.get("ADVENT_SESSION")


def find_largest_sum(sums_url) -> int:
    inputs_list = _get_file_as_list(sums_url)
    local_sum, max_sum = 0, float("-inf")
    for i in inputs_list:
        if not i:
            max_sum = max(local_sum, max_sum)
            local_sum = 0
        else:
            local_sum += int(i)
    return max_sum


def _get_file_as_list(url) -> List:
    if not SESSION:
        raise Exception("No Session token. Set `ADVENT_SESSION` in the environment")

    headers = {"cookie": f"session={SESSION}"}
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.content.splitlines()


if __name__ == "__main__":
    r = find_largest_sum(URL)
    print(f"Max Sum: {r}")
