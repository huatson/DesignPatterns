"""
game extension that adds a bard character
"""

from dataclasses import dataclass
from game import factory


@dataclass
class Bard:
    name: str

    def make_noise(self):
        print("toos a coin!")


def initialize() -> None:
    factory.register("bard", Bard)
