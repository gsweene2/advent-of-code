from enum import Enum

from advent_of_code.y2022.util import _get_file_as_list

URL = "https://adventofcode.com/2022/day/2/input"


class GameMove(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# A B C x X Y Z
SCORE_MATRIX = [[3, 6, 0], [0, 3, 6], [6, 0, 3]]

LOSERS = {
    GameMove.ROCK: GameMove.SCISSORS,
    GameMove.PAPER: GameMove.ROCK,
    GameMove.SCISSORS: GameMove.PAPER,
}

WINNERS = {
    GameMove.ROCK: GameMove.PAPER,
    GameMove.PAPER: GameMove.SCISSORS,
    GameMove.SCISSORS: GameMove.ROCK,
}


def sum_game_scores(games_url, intelligent=False) -> int:
    games_list = _get_file_as_list(games_url)
    score = 0
    for game in games_list:
        game_moves = game.decode(encoding="utf-8").split(" ")
        opp_raw, own_raw = game_moves[0], game_moves[1]
        opp = _parse_move(opp_raw)
        own = _determine_move(opp_raw, own_raw) if intelligent else _parse_move(own_raw)
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


def _determine_move(opponent, own) -> GameMove:
    # Lose Case
    if own in ("X"):
        return LOSERS.get(_parse_move(opponent))
    # Draw Case
    if own in ("Y"):
        return _parse_move(opponent)
    # Win Case
    if own in ("Z"):
        return WINNERS.get(_parse_move(opponent))
    m = f"Unexpected move: '{own}'"
    raise Exception(m)


def _calculate_score(opponent: GameMove, own: GameMove) -> int:
    return own.value + SCORE_MATRIX[opponent.value - 1][own.value - 1]


if __name__ == "__main__":
    r = sum_game_scores(URL)
    print(f"Score: {r}")

    r = sum_game_scores(URL, intelligent=True)
    print(f"Score with intelligence: {r}")
