class Chip:
    def __init__(self) -> None:
        self.total = 100
        self.bet = 0

    def win_bet(self) -> None:
        self.total += self.bet

    def lose_bet(self) -> None:
        self.total -= self.bet
