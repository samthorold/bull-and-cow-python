import random
from typing import List, Tuple


from bull_and_cow_python.game import (
    format_history,
    format_response,
    is_valid_guess,
    respond_to_guess,
)


def parse_bool(string: str) -> bool:
    """Parse user response to "playing alone?" and return a boolean."""
    if not string:
        return True
    if string.upper().strip() in ["Y", "YES"]:
        return True
    return False


def ask_bool(prompt: str) -> bool:
    return parse_bool(input(f"{prompt} (Y/N) [Y]: "))


def parse_int(string: str, default: int) -> int:
    if not string:
        return default
    return int(string)


def ask_int(prompt: str, default: int) -> int:
    for _ in range(100):
        try:
            return parse_int(string=input(f"{prompt} {[default]}: "), default=default)
        except Exception:
            pass
    raise ValueError("No valid integers.")


def ask_guess(prompt: str, secret_length: int, can_repeat: bool) -> str:
    for _ in range(100):
        string = input(f"{prompt}: ")
        valid = is_valid_guess(
            guess=(string),
            n=secret_length,
            can_repeat=can_repeat,
        )
        if valid:
            return string
    raise ValueError("No valid secrets.")


def random_secret(n: int, can_repeat: bool) -> str:
    digits = "0123456789"
    if can_repeat:
        return "".join(random.choices(digits, k=n))
    return "".join(random.sample(digits, n))


def ask_player_for_secret(n: int, i: int, can_repeat: bool) -> str:
    while not is_valid_guess(
        guess=(secret := input(f"Player {i} enter secret (blank for random): ")),
        n=n,
        can_repeat=can_repeat,
    ):
        if not secret:
            secret = random_secret(n, can_repeat)
            break
        print("Secret was not valid.")
    return secret


def ask_player_secrets(players: int, n: int, can_repeat: bool) -> tuple[str, ...]:
    """Ask 2 players for a secret until the secrets are valid."""
    return tuple(
        ask_player_for_secret(n=n, i=i, can_repeat=can_repeat)
        for i in range(1, players + 1)
    )


def is_correct_guess(guess: str, secret: str) -> bool:
    return guess.upper() == secret.upper()


def cli():
    print("*** Bulls and Cows ***")
    max_guesses = 100
    history: List[List[Tuple[str, str]]] = []
    secret_length = ask_int("Enter the length of the secret", 4)
    can_repeat = ask_bool("Can secrets repeat elements?")
    playing_alone = ask_bool("Play numeric game alone against the computer?")

    if not playing_alone:
        player1_secret, player2_secret = ask_player_secrets(
            players=2, n=secret_length, can_repeat=can_repeat
        )
    else:
        player1_secret, player2_secret = "", random_secret(
            n=secret_length, can_repeat=can_repeat
        )

    # possibly unbound (?)
    guess_idx = 0

    for guess_idx in range(max_guesses):
        history.append([])  # new turn
        player1_guess = ask_guess(
            prompt="Enter player 1's guess",
            secret_length=secret_length,
            can_repeat=can_repeat,
        )

        if is_correct_guess(player1_guess, player2_secret):
            print("Player 1 wins.")
            break
        player1_response = format_response(
            respond_to_guess(player1_guess, player2_secret)
        )
        history[-1].append((player1_guess, player1_response))

        if not playing_alone:
            player2_guess = ask_guess(
                prompt="Enter player 2's guess",
                secret_length=secret_length,
                can_repeat=can_repeat,
            )
            if is_correct_guess(player2_guess, player1_secret):
                print("Player 2 wins.")
                break
            player2_response = format_response(
                respond_to_guess(player2_guess, player1_secret)
            )

            history[-1].append((player2_guess, player2_response))

        print(format_history(history))
    if guess_idx + 1 == max_guesses:
        print("Ran out of guesses")
