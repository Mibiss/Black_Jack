from os import system
import chip, hand, deck


def take_bet() -> None:
    """Asking the player how much they want to bet."""
    print(f"total amount: {player_chips.total}")
    while True:
        try:
            player_chips.bet = int(input("Choose the bet amount: "))
        except:
            print(f"Please choose the amount in integer!")
            continue
        else:
            if player_chips.bet < 1 or player_chips.bet > player_chips.total:
                print(f"Please choose between 1 and {player_chips.total}!")
                continue
            else:
                break


def hit(deck: deck.Deck, hand: hand.Hand) -> None:
    """Adding a card object to a hand object"""
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck: deck.Deck, hand: hand.Hand) -> None:
    """Asking the player to hit(get one more card)
    or to stand(stand on this amount of cards)"""
    while True:
        user_input = input("hit or stand: ").lower()

        if user_input not in ["hit", "stand"]:
            print(f"Please choose between hit or stand!")
            continue

        elif user_input == "hit":
            hit(deck=deck, hand=hand)
            show_some(player=player1, dealer=dealer1)

            if player_busts(player=hand):
                break
            continue
        else:
            break


def show_some(player: hand.Hand, dealer: hand.Hand) -> None:
    """Printing all Player's cards and 1 of the Dealer's cards
    and the value of the Player's cards"""
    system("cls")
    print("The Player has: ")
    print(*player.all_cards, sep=", ")
    print(f"Value of Player's hand is: {player.value}")
    print("\n")
    print("The Dealer has: ")
    print(dealer.all_cards[0], "and a hidden card")
    print("\n")


def show_all(player: hand.Hand, dealer: hand.Hand) -> None:
    """Printing all Player's and the Dealer's cards
    with their corresponding value"""
    system("cls")
    print("The Player has: ")
    print(*player.all_cards, sep=", ")
    print(f"Value of Player's hand is: {player.value}")
    print("\n")
    print("The Dealer has: ")
    print(*dealer.all_cards, sep=", ")
    print(f"Value of Dealer's hand is: {dealer.value}")
    print("\n")


def player_busts(player: hand.Hand) -> bool:
    """Checking if Player's value is not over 21"""
    if player.value > 21:
        return True
    else:
        return False


def dealer_busts(dealer: hand.Hand) -> bool:
    """Checking if Dealer's value is not over 21"""
    if dealer.value > 21:
        return True
    else:
        return False


def player_wins(player: hand.Hand, dealer: hand.Hand) -> bool:
    """Checking if Player's value is higher than Dealer's"""
    if player.value > dealer.value:
        return True
    else:
        return False


def dealer_wins(player: hand.Hand, dealer: hand.Hand) -> bool:
    """Checking if Dealer's value is higher than Player's"""
    if player.value < dealer.value:
        return True
    else:
        return False


def replay() -> bool:
    """Asks if you want to play again"""

    choice = input("Play again? Enter Yes or No: ").lower()

    return choice == "yes"


def push() -> None:
    """Printing out that the game is a tie"""
    show_all(player=player1, dealer=dealer1)
    print("This round is a tie!!!")


if __name__ == "__main__":
    counter = 0

    # Set up the Player's chips
    player_chips = chip.Chip()

    playing = True
    # Print an opening statement
    print("Welcome to Black Jack!!")

    while True:
        # Checking if player still has chips to play with
        if player_chips.total <= 0:
            print("No chips to play!")
            break

        counter += 1

        # Creating 2 players
        player1 = hand.Hand()
        dealer1 = hand.Hand()

        # Create & shuffle the deck, deal two cards to each player
        default_deck = deck.Deck()
        default_deck.shuffle()

        player1.add_card(default_deck.deal())
        player1.add_card(default_deck.deal())
        dealer1.add_card(default_deck.deal())
        dealer1.add_card(default_deck.deal())

        # Showing round number and prompting the Player for their bet
        print(f"Round number: {counter}")
        take_bet()

        # Showing cards (but keeping one dealer card hidden)
        show_some(player=player1, dealer=dealer1)

        while playing:
            # Prompting Player to Hit or Stand
            hit_or_stand(deck=default_deck, hand=player1)

            # Showing cards (but keeping one dealer card hidden)
            show_some(player=player1, dealer=dealer1)

            # If player's hand exceeds 21, run player_busts()
            if player_busts(player=player1):
                player_chips.lose_bet()
                print(f"Player chips: {player_chips.total}")
                print("Player busted!")
            break

        if player1.value <= 21:
            # If Player hasn't busted, playing Dealer's hand until Dealer reaches 17
            while dealer1.value < 17:
                hit(deck=default_deck, hand=dealer1)

            # Showing all cards
            show_all(player=player1, dealer=dealer1)

            # Checking if dealer busted
            if dealer_busts(dealer=dealer1):
                player_chips.win_bet()
                print("Dealer Busted!!!!")
                if not replay():
                    break

            else:
                # Running different winning scenarios
                if player_wins(player=player1, dealer=dealer1):
                    player_chips.win_bet()
                    print("Player has Won!!!!")
                    if not replay():
                        break

                elif dealer_wins(player=player1, dealer=dealer1):
                    player_chips.lose_bet()
                    print("Dealer has Won!!!!")
                    if not replay():
                        break

                else:
                    push()
                    player_chips
                    if not replay():
                        break

        # Informing Player of their chips total
        print("Your total chips are", player_chips.total)

        # Asking to play again
