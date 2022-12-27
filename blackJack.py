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
    while True:
        user_input = input("hit or stand: ").lower()
        if user_input not in ["hit", "stand"]:
            print(f"Please choose between hit or stand!")
            continue
        else:
            if user_input == "hit":
                hit(deck=deck, hand=hand)
                show_some(player1, dealer)
            else:
                return False
            continue


def show_some(player, dealer):
    system("cls")
    print("The Player has: ")
    for cards in player.all_cards:
        print(cards, end=", ")
    print("\n")
    print("The Dealer has: ")
    print(dealer.all_cards[0], "and a flipped card")
    print("\n")


def show_all(player, dealer):
    system("cls")
    print("The Player has: ")
    for cards in player.all_cards:
        print(cards, end=", ")
    print("\n")
    print("The Dealer has: ")
    for cards in dealer.all_cards:
        print(cards, end=", ")
    print("\n")


def player_busts():
    if player_points > 21:
        print("Player1 busted!")
        return True


def dealer_busts():
    if dealer_points > 21:
        print("Dealer busted!")
        return True


def player_wins():
    if player_points > dealer_points:
        print("Player wins")
        return True


def dealer_wins():
    if player_points < dealer_points:
        print("Dealer wins!")
        return True


def push():
    pass


if __name__ == "__main__":
    player = hand.Hand()
    dealer = hand.Hand()
    default_deck = deck.Deck()
    chips = chip.Chip()

    default_deck.shuffle()

    player.add_card(dck.deal())
    player.add_card(dck.deal())
    dealer.add_card(dck.deal())
    dealer.add_card(dck.deal())

    show_some(player=player, dealer=dealer)

    playing = True
    while True:
        # Print an opening statement
        print("Welcome to Black Jack!!")

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
