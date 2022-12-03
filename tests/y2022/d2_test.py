from unittest.mock import patch

from advent_of_code.y2022.d2 import _calculate_score, sum_game_scores, GameMove


def test__calculate_score():
    # Arrange
    # Act & Assert

    # Ties
    assert 4 == _calculate_score(GameMove.ROCK, GameMove.ROCK)
    assert 5 == _calculate_score(GameMove.PAPER, GameMove.PAPER)
    assert 6 == _calculate_score(GameMove.SCISSORS, GameMove.SCISSORS)

    # Losing
    assert 1 == _calculate_score(GameMove.PAPER, GameMove.ROCK)
    assert 2 == _calculate_score(GameMove.SCISSORS, GameMove.PAPER)
    assert 3 == _calculate_score(GameMove.ROCK, GameMove.SCISSORS)

    # Winning
    assert 7 == _calculate_score(GameMove.SCISSORS, GameMove.ROCK)
    assert 8 == _calculate_score(GameMove.ROCK, GameMove.PAPER)
    assert 9 == _calculate_score(GameMove.PAPER, GameMove.SCISSORS)


@patch("advent_of_code.y2022.d2._get_file_as_list")
def test_sum_game_scores(mock__get_file_as_list):
    # Arrange
    input_list = [
        b"A Y",
        b"B X",
        b"C Z",
    ]
    mock__get_file_as_list.return_value = input_list

    # Act
    r = sum_game_scores(input_list)

    # Assert
    assert 15 == r
