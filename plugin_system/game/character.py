from typing import Protocol


class GameCharacter(Protocol):
    def make_noise(self):
        pass
