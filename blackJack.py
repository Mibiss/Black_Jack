import chip, hand, deck
from os import system


def take_bet():
    print(f"total amount: {chips.total}")
    while True:
        try:
            amount = int(input("Choose the bet amount: "))
        except:
            print(f"Please choose the amount in integer!")
            continue
        if amount < 1 or amount > chips.total:
            print(f"Please choose between 1 and {chips.total}!")
            continue
        else:
            chips.total -= amount
            break
    return amount


def hit(deck, hand):
    hand.add_card(deck.deal())


def hit_or_stand(deck, hand):
    print(hand)
    while True:
        try:
            user_input = input("hit or stand: ").lower()
        except:
            print(f"Please choose choose between hit or stand! ")
            continue
        if user_input != str:
            print(f"Please choose between hit or stand!")
            continue
        elif user_input not in ["hit", "stand"]:
            print(f"Please choose between hit or stand!")
            continue
        else:
            if user_input == "hit":
                hit(deck=deck, hand=hand)
            else:
                return False
            break


def show_some(player, dealer):
    print("The Player has: ")
    for cards in player.all_cards:
        print(cards, end=", ")
    print("\n")
    print("The Dealer has: ")
    print(dealer.all_cards[0], "and a flipped card")


def show_all(player, dealer):
    pass


def player_busts():
    pass


def player_wins():
    pass


def dealer_busts():
    pass


def dealer_wins():
    pass


def push():
    pass


if __name__ == "__main__":
    mihail = hand.Hand()
    dealer = hand.Hand()
    dck = deck.Deck()
    chips = chip.Chip()

    dck.shuffle()

    playing = True
    while True:
        # Print an opening statement

        # Create & shuffle the deck, deal two cards to each player

        # Set up the Player's chips

        # Prompt the Player for their bet

        # Show cards (but keep one dealer card hidden)

        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand

            # Show cards (but keep one dealer card hidden)

            # If player's hand exceeds 21, run player_busts() and break out of loop

            break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17

        # Show all cards

        # Run different winning scenarios

        # Inform Player of their chips total

        # Ask to play again

        break
