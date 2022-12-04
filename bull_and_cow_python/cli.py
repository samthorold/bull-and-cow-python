import random
from typing import List, Tuple


from bull_and_cow_python.game import (
    format_history,
    format_response,
    is_valid_guess,
    respond_to_guess,
)


def parse_playing_alone(string: str) -> bool:
    """Parse user response to "playing alone?" and return a boolean."""
    if not string:
        return True
    if string.upper().strip() in ["Y", "YES"]:
        return True
    return False


def random_secret(n: int) -> str:
    return "".join(random.sample("0123456789", n))


def ask_player_for_secret(n: int) -> str:
    while not is_valid_guess(
        secret := input("Enter first secret (blank for random): ")
    ):
        if not secret:
            secret = random_secret(n)
            break
        print("Secret was not valid.")
    return secret


def get_player_secrets(players: int, n: int) -> tuple[bool, bool]:
    """Ask 2 players for a secret until the secrets are valid."""
    return tuple(ask_player_for_secret(n) for _ in range(players))


def cli():
    print("*** Bulls and Cows ***")
    max_guesses = 100
    secret_length = 4
    history: List[List[Tuple[str, str]]] = []

    playing_alone = parse_playing_alone(input("Play alone against the computer? (Y/N) [Y] "))

    if not playing_alone:
        player1_secret, player2_secret = get_player_secrets(2, secret_length)
    else:
        player2_secret = random_secret(secret_length)

    for guess_idx in range(max_guesses):
        history.append([])  # new turn
        while not is_valid_guess(player1_guess := input("Enter player 1's guess: ")):
            print("Guess was not valid.")
        if player1_guess == player2_secret:
            print("Player 1 wins.")
            break
        player1_response = format_response(
            respond_to_guess(player1_guess, player2_secret)
        )
        history[-1].append((player1_guess, player1_response))

        if not playing_alone:
            while not is_valid_guess(player2_guess := input("Enter player 2's guess: ")):
                print("Guess was not valid.")
            if player2_guess == player1_secret:
                print("Player 2 wins.")
                break
            player2_response = format_response(
                respond_to_guess(player2_guess, player1_secret)
            )

            history[-1].append((player2_guess, player2_response))

        print(format_history(history))
    if guess_idx + 1 == max_guesses:
        print("Ran out of guesses")
