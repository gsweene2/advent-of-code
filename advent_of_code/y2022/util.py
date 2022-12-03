from typing import List
import os
import requests

SESSION = os.environ.get("ADVENT_SESSION")


def _get_file_as_list(url) -> List:
    if not SESSION:
        raise Exception("No Session token. Set `ADVENT_SESSION` in the environment")

    headers = {"cookie": f"session={SESSION}"}
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.content.splitlines()
