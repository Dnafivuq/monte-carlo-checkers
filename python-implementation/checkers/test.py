from checkers import Checkers
import pytest


def test_diagonal_top_right():
    game = Checkers()
    diag_1, diag_2 = game._get_diagonals(3)
    assert diag_1 == []
    assert diag_2 == [28, 24, 21, 17, 14, 10, 7]


if __name__ == "__main__":
    test_diagonal_top_right()
