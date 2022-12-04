"""

2 players.

Each choose a secret number.
The digits must all be different.

Each player takes a turn at guessing the other's number.
A guess receives information on the number of matches in response.

A digit in the right position is a bull.
A digit in the wrong position is a cow.

"""


def is_valid_guess(guess: str) -> bool:
    """Confirm a secret number entry or guess is compliant with the rules."""
    all_numbers = all(c in "0123456789" for c in guess)
    correct_length = len(guess) == 4
    no_duplicates = len(guess) == len(set(guess))
    return all([all_numbers, correct_length, no_duplicates])


def respond_to_guess(guess: str, truth: str) -> tuple[str, str, str, str]:
    """Respond to a guess. Guess assumed to be valid."""
    response = []
    for i, digit in enumerate(guess):
        if digit in truth:
            if truth[i] == digit:
                response.append("B")
            else:
                response.append("C")
        else:
            response.append(".")
    return tuple(response)


def format_response(response: tuple[str, str, str, str]) -> str:
    """Format the response as a sentence not revealing the location-specific info."""
    bullstring = cowstring = ""
    bulls = sum(c == "B" for c in response)
    if bulls == 1:
        bullstring = "1 bull"
    if bulls > 1:
        bullstring = f"{bulls} bulls"
    cows = sum(c == "C" for c in response)
    if cows == 1:
        cowstring = "1 cow"
    if cows > 1:
        cowstring = f"{cows} cows"
    return f"{bullstring}{', ' if bulls and cows else ''}{cowstring}"


def format_history(history: list[list[tuple[str, str]]]) -> str:
    """Display the game history in a human-readable format."""
    s = ""
    for i, turn in enumerate(history, 1):
        s += f"| {' ' if i < 10 else ''}{i} |"
        for j, (guess, response) in enumerate(turn):
            s += f" {guess} | {response:<15} |"
        s += "\n"
    return s
