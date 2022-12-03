from enum import Enum

from advent_of_code.y2022.util import _get_file_as_list

URL = "https://adventofcode.com/2022/day/2/input"


class GameMove(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


"""
  X Y Z
A 3 6 0
B 0 3 6
C 6 0 3 
"""
SCORE_MATRIX = [[3, 6, 0], [0, 3, 6], [6, 0, 3]]


def sum_game_scores(games_url) -> int:
    games_list = _get_file_as_list(games_url)
    score = 0
    for game in games_list:
        game_moves = game.decode(encoding="utf-8").split(" ")
        opp, own = _parse_move(game_moves[0]), _parse_move(game_moves[1])
        score += _calculate_score(opp, own)
    return score


def _parse_move(move) -> GameMove:
    if move in ("A", "X"):
        return GameMove.ROCK
    if move in ("B", "Y"):
        return GameMove.PAPER
    if move in ("C", "Z"):
        return GameMove.SCISSORS
    m = f"Unexpected move: '{move}'"
    raise Exception(m)


def _calculate_score(opponent: GameMove, own: GameMove) -> int:
    return own.value + SCORE_MATRIX[opponent.value - 1][own.value - 1]


if __name__ == "__main__":
    r = sum_game_scores(URL)
    print(f"Score: {r}")
