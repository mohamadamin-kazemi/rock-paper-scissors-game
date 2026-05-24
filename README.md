# Rock Paper Scissors Game 🎮

A simple text-based **Rock, Paper, Scissors** game built with Python.  
Play against the computer directly from your terminal.

---

## Features

- Interactive command-line gameplay
- Random computer choices
- Input validation
- Replay option
- Clean and beginner-friendly Python code
- Uses object-oriented programming (OOP)

---

## Project Structure

```text
ROCK-PAPER-SCISSORS-GAME/
│
├── src/
│   └── main.py
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## Requirements

- Python 3.12.11
- No external libraries are required

---

## How to Run

1. **Clone the repository**

```bash
git clone https://github.com/mohamadamin-kazemi/rock-paper-scissors-game.git
```

2. **Navigate to the project folder**

```bash
cd rock-paper-scissors-game
```

3. **Run the game**

```bash
python src/main.py
```

---

## Gameplay Example

```text
Welcome to Rock, Paper, Scissors!
Enter your name: Amin
------------------------------
Please enter your choice (rock, paper, scissors): rock
Computer chooses: scissors
Congratulations! Amin wins!

Play again? (Press 'q' to quit, any other key to continue):
```

---

## Rules

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- If both choices are the same, the result is a tie

---

## Code Overview

### `RockPaperScissors` Class

Handles the main game logic:

- Getting the player's choice
- Generating the computer's choice
- Deciding the winner
- Running a game round

### `main()` Function

Controls:

- Welcome message
- Player setup
- Replay loop
- Game exit

---

## Concepts Used

- Classes and Objects
- Dictionaries
- Tuples
- Type Hints
- Loops
- Functions
- Input Validation
- Random Module

---

## Author

**Mohamadamin Kazemi**

---

## License

This project is licensed under the MIT License.
