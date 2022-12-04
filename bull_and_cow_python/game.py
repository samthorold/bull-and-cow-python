"""

2 players.

Each choose a secret number.
The digits must all be different.

Each player takes a turn at guessing the other's number.
A guess receives information on the number of matches in response.

A digit in the right position is a bull.
A digit in the wrong position is a cow.

"""


def is_valid_guess(guess: str, n: int = 4, can_repeat: bool = False) -> bool:
    """Confirm a secret number entry or guess is compliant with the rules."""
    all_numbers = all(c.upper() in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in guess)
    correct_length = len(guess) == n
    if can_repeat:
        no_duplicates = True
    else:
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
    s = f"\n| Turn | {'Player 1 guess':<15} | {'Player 1 response':<20} |"
    if len(history[0]) > 1:
        s += f" {'Player 2 guess':<15} | {'Player 2 response':<20} |"
    s += "\n"
    for i, turn in enumerate(history, 1):
        s += f"| {i:>4} |"
        for j, (guess, response) in enumerate(turn, 1):
            s += f" {guess:<15} | {response:<20} |"
        s += "\n"
    return s + "\n"
