import random
from typing import Protocol


class Player(Protocol):
    def ask_secret(self, prompt: str, secret_length: int) -> str:
        ...

    def make_guess(
        self,
        prompt: str,
        history: list[list[tuple[str, str]]],
        idx: int,
        secret_length: int,
    ) -> str:
        ...


class TerminalPlayer:
    def ask_secret(self, prompt: str, secret_length: int) -> str:
        return input(prompt)

    def make_guess(
        self,
        prompt: str,
        history: list[list[tuple[str, str]]],
        idx: int,
        secret_length: int,
    ) -> str:
        return input(prompt)


class RandomPlayer:
    def ask_secret(self, prompt: str, secret_length: int) -> str:
        return "".join(random.choices("0123456789", k=secret_length))

    def make_guess(
        self,
        prompt: str,
        history: list[list[tuple[str, str]]],
        idx: int,
        secret_length: int,
    ) -> str:
        return self.ask_secret(prompt=prompt, secret_length=secret_length)
