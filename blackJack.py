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
            player1.chips.bet = amount
            break


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
    for cards in player.all_cards:
        print(cards, end=", ")
    print("\n")
    print("The Dealer has: ")
    for cards in dealer.all_cards:
        print(cards, end=", ")
    print("\n")


def player_busts(player, chips):
    value = 0
    for cards in player.all_cards:
        value += cards.value
    if value > 21:
        chips.lose_bet()
        return True
    else:
        return False


def dealer_busts(dealer, chips):
    value = 0
    for cards in dealer.all_cards:
        value += cards.value
    if value > 21:
        chips.win_bet()
        return True
    else:
        return False


def player_wins(player, dealer, chips):
    dealer_value = 0
    player_value = 0
    for p_cards, d_cards in zip(player.all_cards, dealer.all_cards):
        player_value += p_cards.value
        dealer_value += d_cards.value

    if player_value > dealer_value:
        chips.win_bet()

        return True
    else:
        return False


def dealer_wins(player, dealer, chips):
    dealer_value = 0
    player_value = 0
    for p_cards, d_cards in zip(player.all_cards, dealer.all_cards):
        player_value += p_cards.value
        dealer_value += d_cards.value

    if player_value < dealer_value:
        chips.lose_bet()

        return True
    else:
        return False


def replay() -> bool:

    """Asks if you want to play again"""

    choice = input("Play again? Enter Yes or No: ").lower()

    return choice == "yes"


def push():
    pass


if __name__ == "__main__":
    counter = 0
    print("Welcome to Black Jack!!")
    name = input("Your name: ")
    hand1 = hand.Hand()
    hand2 = hand.Hand()

    # Print an opening statement

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
    player1.setChips(amount=100)

    playing = True
    while True:
        counter += 1

        print(f"Round number: {counter}")
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
        dealer_value = 0

        for cards in dealer1.hand.all_cards:
            dealer_value += cards.value

        if dealer_value < 17:
            hit(deck=default_deck, hand=dealer1.hand)

        elif dealer_busts(dealer=dealer1.hand, chips=player1.chips):
            print("Dealer Busted!!!!")

        # Show all cards
        show_all(player=player1.hand, dealer=dealer1.hand)

        # Run different winning scenarios
        if player_wins(player=player1.hand, dealer=dealer1.hand, chips=player1.chips):
            print("Player has Won!!!!")
        elif dealer_wins(player=player1.hand, dealer=dealer1.hand, chips=player1.chips):
            print("Dealer has Won!!!!")
        else:
            print("This round is a tie!!!")
        # Inform Player of their chips total
        print(player1.chips.total)

        # Ask to play again
        if not replay():
            break
