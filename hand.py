import card


class Hand:
    def __init__(self) -> None:
        self.all_cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, new_card) -> None:
        self.all_cards.append(new_card)
        self.value += card.values[new_card.rank]

        if new_card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self) -> None:
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def __str__(self) -> str:
        return f"{self.all_cards}"
