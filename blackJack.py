import chip, hand, deck, player
from os import system


def take_bet():
    print(f"total amount: {player1.chips.total}")
    while True:
        try:
            amount = int(input("Choose the bet amount: "))
        except:
            print(f"Please choose the amount in integer!")
            continue
        if amount < 1 or amount > player1.chips.total:
            print(f"Please choose between 1 and {player1.chips.total}!")
            continue
        else:
            player1.chips.total -= amount
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
                show_some(player=player1.hand, dealer=dealer1.hand)
                break
            else:
                return False


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
    print([cards + ", " for cards in player.all_cards])
    print("\n")
    print("The Dealer has: ")
    print([cards + ", " for cards in dealer.all_cards])
    print("\n")


def player_busts(player, chips):
    value = 0
    for cards in player.all_cards:
        value += cards.value
    chips.lose_bet()
    if value > 21:
        return True


def dealer_busts(player, dealer):
    if dealer_points > 21:
        print("Dealer busted!")
        return True


def player_wins(player, dealer):
    if player_points > dealer_points:
        print("Player wins")
        return True


def dealer_wins(player, dealer):

    if player.all_cards < dealer_points:
        print("Dealer wins!")
        return True


def push():
    pass


if __name__ == "__main__":

    playing = True
    while True:
        hand1 = hand.Hand()
        hand2 = hand.Hand()

        # Print an opening statement
        print("Welcome to Black Jack!!")
        name = input("Your name: ")
        player1 = player.Player(name=name, hand=hand1)
        dealer1 = player.Player(name="dealer", hand=hand2)

        # Create & shuffle the deck, deal two cards to each player
        default_deck = deck.Deck()
        default_deck.shuffle()

        player1.hand.add_card(default_deck.deal())
        player1.hand.add_card(default_deck.deal())
        dealer1.hand.add_card(default_deck.deal())
        dealer1.hand.add_card(default_deck.deal())
        # Set up the Player's chips
        player1.setChips(amount=1000)

        # Prompt the Player for their bet
        take_bet()

        # Show cards (but keep one dealer card hidden)
        show_some(player=player1.hand, dealer=dealer1.hand)

        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(deck=default_deck, hand=player1.hand)

            # Show cards (but keep one dealer card hidden)
            show_some(player=player1.hand, dealer=dealer1.hand)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_busts(player=player1.hand, chips=player1.chips):
                print(f"Player {player1.chips.total}")
                print("Player busted!!")
            break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17

        # Show all cards

        # Run different winning scenarios

        # Inform Player of their chips total

        # Ask to play again

        break
