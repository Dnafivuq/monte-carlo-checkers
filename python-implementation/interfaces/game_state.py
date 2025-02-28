from typing import TypeAlias
from abc import ABC, abstractmethod

Move: TypeAlias = str


class Player:
    pass


class GameState(ABC):
    def __init__(self):
        self.active_player = None
        self.board = None

