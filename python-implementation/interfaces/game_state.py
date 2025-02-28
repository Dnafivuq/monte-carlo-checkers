from typing import TypeAlias
from abc import ABC, abstractmethod

Move: TypeAlias = str


class Player(ABC):
    def __init__(self):
        pass


class GameState(ABC):
    @abstractmethod
    def get_player(self) -> Player:
        pass

    @abstractmethod
    def get_board(self) -> str:
        pass
