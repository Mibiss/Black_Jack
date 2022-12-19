import card
import random


class Deck:
    def __init__(self) -> None:

        self.all_cards = []

        for suit in card.suits:
            for rank in card.ranks:
                created_card = card.Card(suit=suit, rank=rank)

                self.all_cards.append(created_card)

    def shuffle(self) -> None:
        random.shuffle(self.all_cards)

    def deal_one(self) -> card:
        return self.all_cards.pop()
