1. Project Title
Tic-Tac-Toe: Python Console Game

2. Overview of the Project
This project is a digital implementation of the classic paper-and-pencil game "Tic-Tac-Toe" (also known as Noughts and Crosses). Built using Python, the application runs in a Command Line Interface (CLI) environment. The primary objective of this project is to demonstrate the use of fundamental programming concepts—such as arrays (lists), conditional logic, loops, and input validation—to create an interactive, bug-free gaming experience.

The game allows two players to play locally on the same machine, taking turns to mark spaces in a 3×3 grid. The program acts as a referee, automatically detecting wins, draws, and invalid moves.

3. Features
Interactive 3x3 Grid: A clear, text-based visualization of the board that updates after every turn.

Multiplayer Logic: Supports 2-player "hotseat" gameplay (Player X vs. Player O).

Win Detection Algorithm: Instantly checks for a winner across 8 axes:

3 Horizontal Rows

3 Vertical Columns

2 Diagonals

Smart Input Validation:

Prevents the game from crashing if a user types a letter instead of a number.

Prevents players from overwriting a spot that is already taken.

Draw State Handling: Recognizes when the board is full without a winner and ends the game gracefully.

Restart Mechanism: Allows players to play multiple rounds without restarting the script.

4. Technologies/Tools Used
Programming Language: Python (Version 3.x)

Development Environment (IDE): VS Code / PyCharm / IDLE (or any text editor)

Operating System: Cross-platform (Windows, macOS, Linux)

Version Control: Git (for tracking code changes)

5. Steps to Install & Run the Project
Step 1: Verify Python Installation Ensure Python is installed on your computer. Open your terminal (Command Prompt) and type:

Bash

python --version
Step 2: Download the Project Download the tictactoe.py file to a folder on your computer.

Step 3: Open Terminal Navigate to the folder where you saved the file:

Bash

cd path/to/your/folder
Step 4: Execute the Script Run the game using the following command:

Bash

python tictactoe.py
6. Instructions for Testing
To ensure the game works correctly, perform the following manual tests:

Test Case A: The "Win" Scenario

Start the game.

Player X enters 1.

Player O enters 4.

Player X enters 2.

Player O enters 5.

Player X enters 3.

Expected Result: The game should stop, display the board, and print "Player X Wins!" (Testing the top row win condition).

Test Case B: The "Occupied Spot" Error

Start the game.

Player X enters 5.

Player O tries to enter 5.

Expected Result: The game should display a warning: "Spot already taken, try again" and allow Player O to choose a different number.

Test Case C: The "Invalid Input" Error

Start the game.

Player X enters Z or hello.

Expected Result: The program should not crash. It should display "Invalid input. Please enter a number between 1-9."

Test Case D: The "Draw" Scenario

Play a game where players block each other so no one gets 3 in a row.

Fill the 9th and final square.

Expected Result: The game should declare "It's a Draw!" and ask if you want to play again.
