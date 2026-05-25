"""
Author: Mohamadamin Kazemi
Date: 2024-05-24
Title: Rock, Paper, Scissors Game
Description: A simple text-based Rock, Paper, Scissors game implemented in Python.
"""

import random
from typing import Dict, Tuple


class RockPaperScissors:
    """A text-based Rock, Paper, Scissors game.

    :ivar name: The name of the player.
    :vartype name: str
    """

    CHOICES: Tuple[str, ...] = ("rock", "paper", "scissors")

    WINNING_MOVES: Dict[str, str] = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    def __init__(self, name: str):
        """Initialize the game with the player's name.

        :param name: The name of the player.
        """
        self.name = name

    def get_player_choice(self) -> str:
        """Prompt the player for a valid move.

        :return: The player's validated choice.
        """
        prompt = f"Please enter your choice ({', '.join(self.CHOICES)}): "

        while True:
            choice = input(prompt).strip().lower()

            if choice in self.CHOICES:
                return choice

            print(
                f"Invalid choice. "
                f"Please choose between: {', '.join(self.CHOICES)}\n"
            )

    def get_computer_choice(self) -> str:
        """Generate a random move for the computer.

        :return: The computer's choice.
        """
        choice = random.choice(self.CHOICES)

        print(f"Computer chooses: {choice}")

        return choice

    def decide_winner(
        self,
        player_choice: str,
        computer_choice: str
    ) -> str:
        """Determine the winner of the round.

        :param player_choice: The player's selected move.
        :param computer_choice: The computer's selected move.
        :return: A message declaring the result of the round.
        """
        if player_choice == computer_choice:
            return "It's a tie!"

        if self.WINNING_MOVES[player_choice] == computer_choice:
            return f"Congratulations! {self.name} wins!"

        return f"Sorry! {self.name} loses!"

    def play(self) -> None:
        """Execute a single round of the game.
        """
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()

        result = self.decide_winner(
            player_choice,
            computer_choice
        )

        print(result)


def main() -> None:
    """Main entry point for the game loop.
    """
    print("Welcome to Rock, Paper, Scissors!")

    player_name = input("Enter your name: ").strip() or "Player"

    game = RockPaperScissors(player_name)

    while True:
        print("-" * 30)

        game.play()

        continue_game = input(
            "\nPlay again? "
            "(Press 'q' to quit, any other key to continue): "
        )

        if continue_game.strip().lower() == "q":
            print(f"Thanks for playing, {game.name}!")

            break


if __name__ == "__main__":
    main()
