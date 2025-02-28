from enum import Enum
from interfaces import GameState


class CheckersPiece(Enum):
    EMPTY = 0
    WHITE = 1
    BLACK = 2
    WHITE_QUEEN = 3
    BLACK_QUEEN = 4


class CheckersPlayer(Enum):
    WHITE = -1
    BLACK = 1


class CheckersState(GameState):
    def __init__(self, board: list[list[CheckersPiece]], active_player: CheckersPlayer):
        self.board = board
        self.active_player = active_player
