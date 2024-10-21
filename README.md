# Guessing Game

## Overview

The **Guessing Game** is a GUI-based Python application that challenges players to guess a randomly generated number between 1 and 10. Players have three attempts to guess the correct number, with real-time feedback on their guesses. The game includes a user-friendly interface with customizable options to enhance the gaming experience.

## Features

- Generates a random number between 1 and 10 (inclusive).
- Provides up to three guesses for the user.
- Feedback for each guess:
  - "Too big" if the guess is greater than the random number.
  - "Too small" if the guess is less than the random number.
  - "Correct" if the guess matches the random number.
- **User Interface:**
  - A changeable picture displayed on the left side.
  - A display area for the user's previous guesses on the top right.
  - An edit box for the user to enter their guess.
  - A button that submits the guess and provides feedback.
  - Combo boxes to allow users to change the interface's color and picture.
  - A change button to apply the selected options.
  - Bottom buttons to close the game and start a new game.

## Requirements

- Python 3.x
- Tkinter (for GUI)

## Installation

1. Clone this repository or download the `GuessingGame.py` file.
2. Ensure you have Python 3.x installed on your machine.
3. Install Tkinter (if not already installed) using the following command:
   ```bash
   pip install tk

