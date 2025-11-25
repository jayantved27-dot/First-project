❌⭕ Tic-Tac-Toe Game
A classic, command-line interface (CLI) implementation of Tic-Tac-Toe built using Python. This project allows two players to play against each other on the same machine using a numbered grid system.

📝 Description
This project is a logic-based Python application that simulates a standard 3x3 Tic-Tac-Toe board. It utilizes lists to track player moves and mathematical logic to determine win conditions (rows, columns, and diagonals). The game runs in the terminal and updates the board state after every turn.

✨ Features
Two-Player Mode: Play locally with a friend (Player X vs. Player O).

Real-time Board Rendering: The board refreshes after every move to show the current game state.

Win Detection: Automatically detects if X or O has won via rows, columns, or diagonals.

Draw Detection: Recognizes when all 9 spots are filled without a winner.

Input Validation: Prevents players from overwriting an occupied spot.

💻 Requirements
Python 3.x

🚀 How to Run
Ensure you have Python installed on your system.

Download the main.py (or whatever you named your file) to your computer.

Open your terminal or command prompt.

Navigate to the folder containing the file.

Run the command:

Bash

python main.py
🎮 How to Play
The game uses a 0-8 numbering system to map the board positions. When it is your turn, enter the number corresponding to the spot you want to claim.

The Grid Layout:

Plaintext

 0 | 1 | 2 
---|---|---
 3 | 4 | 5 
---|---|---
 6 | 7 | 8 
The game starts with Player X.

Enter a number (0-8) when prompted.

Player O goes next.

The game continues until a player wins or the board is full (Draw).

📂 Code Structure
printBoard(playerX_move, playerO_move): Handles the visual representation of the grid.

checkWin(playerX_move, playerO_move): Iterates through winning combinations to check for a victory.

tic_tac_toe(a, b, c): A helper function that sums the values of a specific line to calculate logic.

Main Loop: Manages the flow of the game, turn switching, and user input.

🔮 Future Improvements
Add a "Play Again" feature without restarting the script.
Implement a Single Player mode (vs. Computer).
Add a graphical user interface (GUI) using Tkinter or Pygame.

Implement a Single Player mode (vs. Computer).

Add a graphical user interface (GUI) using Tkinter or Pygame.
