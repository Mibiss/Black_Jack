from hand import Hand
from chip import Chip


class Player:
    def __init__(self, name: str, hand: Hand) -> None:
        self.name = name
        self.hand = hand
        self.chips = Chip()

    def __str__(self) -> str:
        print(f"{self.name} has {self.chips} chips")

    def setChips(self, amount: int):
        self.chips.total = amount
