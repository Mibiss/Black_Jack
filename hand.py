class Hand:
    def __init__(self) -> None:
        self.all_cards = []

    def add_card(self, new_cards) -> None:
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def adjust_for_ace(self) -> None:
        value = 0
        while value not in [1, 11]:
            value = int(input("What value is your ace?(1 or 11) "))
        return value

    def __str__(self) -> str:
        return f"You got {self.all_cards} in your hand"
