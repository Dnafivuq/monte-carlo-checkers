from typing import TypeAlias
from abc import ABC, abstractmethod

Move: TypeAlias = str


class Player(ABC):
    pass


class GameState(ABC):
    pass
