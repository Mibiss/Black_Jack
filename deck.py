"""
This file is for generating a deck by using card class
"""
import random
import card


class Deck:
    """
    This class generates a deck
    """

    def __init__(self) -> None:

        self.all_cards = []

        for suit in card.suits:
            for rank in card.ranks:
                created_card = card.Card(suit=suit, rank=rank)

                self.all_cards.append(created_card)

    def shuffle(self) -> None:
        """Shufle the cards within the deck"""
        random.shuffle(self.all_cards)

    def deal_one(self) -> card:
        """Deal the last cars of the deck"""
        return self.all_cards.pop()
