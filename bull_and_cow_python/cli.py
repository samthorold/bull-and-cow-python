import random
from typing import List, Tuple


from bull_and_cow_python.game import (
    format_history,
    format_response,
    is_valid_guess,
    respond_to_guess,
)


def cli():
    print("*** Bulls and Cows ***")
    history: List[List[Tuple[str, str]]] = []

    while not is_valid_guess(
        player1_secret := input("Enter first secret (blank for random): ")
    ):
        if not player1_secret:
            player1_secret = "".join(random.sample("0123456789", 4))
            break
        print("Secret was not valid.")

    while not is_valid_guess(
        player2_secret := input("Enter second secret (blank for random): ")
    ):
        if not player2_secret:
            player2_secret = "".join(random.sample("0123456789", 4))
            break
        print("Secret was not valid.")

    for _ in range(100):
        while not is_valid_guess(player1_guess := input("Enter player 1's guess: ")):
            print("Guess was not valid.")
        if player1_guess == player2_secret:
            print("Player 1 wins.")
            break
        player1_response = format_response(
            respond_to_guess(player1_guess, player2_secret)
        )

        while not is_valid_guess(player2_guess := input("Enter player 2's guess: ")):
            print("Guess was not valid.")
        if player2_guess == player1_secret:
            print("Player 2 wins.")
            break
        player2_response = format_response(
            respond_to_guess(player2_guess, player1_secret)
        )

        history.append(
            [
                (player1_guess, player1_response),
                (player2_guess, player2_response),
            ]
        )

        print(format_history(history))
