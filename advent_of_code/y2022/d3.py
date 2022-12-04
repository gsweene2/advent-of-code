from advent_of_code.y2022.util import _get_file_as_list

URL = "https://adventofcode.com/2022/day/3/input"


def count_priorities(input_url):
    rucksacks_list = _get_file_as_list(input_url)
    total = 0
    for input in rucksacks_list:
        i_str = input.decode("utf-8")
        h1, h2 = i_str[: len(i_str) // 2], i_str[len(i_str) // 2 :]
        r = set(list(h1)).intersection(set(list(h2)))
        total += _get_priority(r)
    return total


def count_badge_priorities(input_url):
    rucksacks_list = _get_file_as_list(input_url)
    total, rucksacks_group = 0, []
    for input in rucksacks_list:
        i_str = input.decode("utf-8")
        if not rucksacks_group:
            rucksacks_group = [i_str]
        else:
            rucksacks_group.append(i_str)
        if len(rucksacks_group) == 3:
            common = (
                set(rucksacks_group[0])
                .intersection(set(rucksacks_group[1]))
                .intersection(set(rucksacks_group[2]))
            )
            total += _get_priority(common)
            rucksacks_group = []
    return total


def _get_priority(s):
    p = ord(next(iter(s))) - 96
    return p if p > 0 else p + 58


if __name__ == "__main__":
    r = count_priorities(URL)
    print(f"Sum priorities: {r}")

    r = count_badge_priorities(URL)
    print(f"Sum Badge Priorities: {r}")
