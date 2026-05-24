import random
from typing import Dict, Tuple

class RockPaperScissors:
    """
    A text-based Rock, Paper, Scissors game.

    Attributes:
        name (str): The name of the player.
    """

    CHOICES: Tuple[str, ...] = ("rock", "paper", "scissors")
    WINNING_MOVES: Dict[str, str] = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    def __init__(self, name: str) -> None:
        """Initializes the game with the player's name."""
        self.name = name

    def get_player_choice(self) -> str:
        """
        Prompts the player for a valid move.

        Returns:
            str: The player's validated choice.
        """
        prompt = f"Please enter your choice ({', '.join(self.CHOICES)}): "
        
        while True:
            choice = input(prompt).strip().lower()
            if choice in self.CHOICES:
                return choice
            
            print(f"Invalid choice. Please choose between: {', '.join(self.CHOICES)}\n")

    def get_computer_choice(self) -> str:
        """
        Generates a random move for the computer.

        Returns:
            str: The computer's choice.
        """
        choice = random.choice(self.CHOICES)
        print(f"Computer chooses: {choice}")
        return choice

    def decide_winner(self, player_choice: str, computer_choice: str) -> str:
        """
        Determines the winner of the round.

        Args:
            player_choice (str): The player's selected move.
            computer_choice (str): The computer's selected move.

        Returns:
            str: A message declaring the result of the round.
        """
        if player_choice == computer_choice:
            return "It's a tie!"

        if self.WINNING_MOVES[player_choice] == computer_choice:
            return f"Congratulations! {self.name} wins!"
        
        return f"Sorry! {self.name} loses!"

    def play(self) -> None:
        """Executes a single round of the game."""
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        
        result = self.decide_winner(player_choice, computer_choice)
        print(result)


def main() -> None:
    """Main entry point for the game loop."""
    print("Welcome to Rock, Paper, Scissors!")
    
    player_name = input("Enter your name: ").strip() or "Player"
    game = RockPaperScissors(player_name)
    
    while True:
        print("-" * 30)
        game.play()

        continue_game = input("\nPlay again? (Press 'q' to quit, any other key to continue): ")
        if continue_game.strip().lower() == 'q':
            print(f"Thanks for playing, {game.name}!")
            break


if __name__ == "__main__":
    main()