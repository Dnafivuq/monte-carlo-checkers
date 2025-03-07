import pytest
from src.checkers import Checkers, CheckersPiece, CheckersPlayer # importing packages 101


def test_example():
    assert 1 == 1


def test_enums():
    assert CheckersPlayer.WHITE == CheckersPiece.WHITE


if __name__ == "__main__":
    test_example()