import chip, hand, deck
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
                show_some(player=player1, dealer=dealer1)
                break
            else:
                return False


def show_some(player, dealer):
    system("cls")
    print("The Player has: ")
    print(*player.all_cards, sep=", ")
    print("\n")
    print("The Dealer has: ")
    print(dealer.all_cards[0], "and a flipped card")
    print("\n")


def show_all(player, dealer):
    system("cls")
    print("The Player has: ")
    print(*player.all_cards, sep=", ")
    print("\n")
    print("The Dealer has: ")
    print(*dealer.all_cards, sep=", ")
    print("\n")


def player_busts(player, chips):
    value = 0
    print(player1.all_cards, player1.all_cards[0])

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
    
    player1 = hand.Hand()
    dealer1 = hand.Hand()

    # Print an opening statement
    print("Welcome to Black Jack!!")
    
    # Create & shuffle the deck, deal two cards to each player
    default_deck = deck.Deck()
    default_deck.shuffle()

    player1.add_card(default_deck.deal())
    player1.add_card(default_deck.deal())
    dealer1.add_card(default_deck.deal())
    dealer1.add_card(default_deck.deal())
    
    # Set up the Player's chips
    player_chips = chip.Chip()

    playing = True
    
    while True:
        counter += 1

        print(f"Round number: {counter}")
        # Prompt the Player for their bet
        take_bet()

        # Show cards (but keep one dealer card hidden)
        show_some(player=player1, dealer=dealer1)

        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(deck=default_deck, hand=player1)

            # Show cards (but keep one dealer card hidden)
            show_some(player=player1, dealer=dealer1)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_busts(player=player1, chips=player_chips):
                print(f"Player {player_chips.total}")
                print("Player busted!!")
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        dealer_value = 0

        for cards in dealer1.all_cards:
            dealer_value += cards.value

        if dealer_value < 17:
            hit(deck=default_deck, hand=dealer1)

        elif dealer_busts(dealer=dealer1, chips=player_chips)
            print("Dealer Busted!!!!")

        # Show all cards
        show_all(player=player1, dealer=dealer1)

        # Run different winning scenarios
        if player_wins(player=player1, dealer=dealer1, chips=player_hips):
            print("Player has Won!!!!")
        elif dealer_wins(player=player1, dealer=dealer1, chips=player_hips):
            print("Dealer has Won!!!!")
        else:
            print("This round is a tie!!!")
        # Inform Player of their chips total
        print(*player1)

        # Ask to play again
        if not replay():
            break
