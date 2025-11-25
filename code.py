# Helper function to calculate the sum of three values
# We use this to check if a player has 3 marks in a row (1 + 1 + 1 = 3)
def sum(a, b, c):
    return a + b + c

def printBoard(playerX_move, playerO_move):
    # Determine what to print for each of the 9 positions (0-8)
    # If playerX_move has a 1 at index 0, print 'X'. 
    # Else if playerO_move has a 1 at index 0, print 'O'. 
    # Otherwise, print the position number (0).
    zero = 'X' if playerX_move [0] else ('O' if playerO_move[0] else 0)
    one = 'X' if playerX_move [1] else ('O' if playerO_move[1] else 1)
    two = 'X' if playerX_move [2] else ('O' if playerO_move[2] else 2)
    three = 'X' if playerX_move [3] else ('O' if playerO_move[3] else 3)
    four = 'X' if playerX_move [4] else ('O' if playerO_move[4] else 4)
    five = 'X' if playerX_move [5] else ('O' if playerO_move[5] else 5)
    six = 'X' if playerX_move [6] else ('O' if playerO_move[6] else 6)
    seven = 'X' if playerX_move [7] else ('O' if playerO_move[7] else 7)
    eight = 'X' if playerX_move [8] else ('O' if playerO_move[8] else 8) 
    
    # Print the formatted board
    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")

def checkWin(playerX_move, playerO_move):
    # List of all winning combinations: [Rows, Columns, Diagonals]
    # For example, [0, 1, 2] is the top row, [0, 4, 8] is a diagonal
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    for win in wins:
        # Check if X has marked all 3 spots in the current winning line
        # If sum is 3, it means X has occupied all those positions
        if(sum(playerX_move[win[0]], playerX_move[win[1]], playerX_move[win[2]]) == 3):
            print("X won the match")
            return 1 # Return 1 indicates X won
        
        # Check if O (playerO_move) has marked all 3 spots
        if(sum(playerO_move[win[0]], playerO_move[win[1]], playerO_move[win[2]]) == 3):
            print("O won the match")
            return 0 # Return 0 indicates O won
            
    return -1 # Return -1 means no winner yet
    
if __name__ == "__main__":
    # Initialize the board states: 0 means empty, 1 means occupied
    playerX_move = [0, 0, 0, 0, 0, 0, 0, 0, 0] # Tracks X's moves
    playerO_move = [0, 0, 0, 0, 0, 0, 0, 0, 0] # Tracks O's moves
    
    turn = 1 # Variable to track whose turn it is: 1 for X, 0 for O
    print("Welcome to Tic Tac Toe")
    
    # Infinite loop to keep the game running until someone wins
    while(True):
        printBoard(playerX_move, playerO_move)
        
        if(turn == 1):
            print("X's chance")
            # Get input from user and mark the board for X
            value = int(input("Please enter a value[0-8]: "))
            playerX_move[value] = 1
        else:
            print("O's chance")
            # Get input from user and mark the board for O
            value = int(input("Please enter a value[0-8]: "))
            playerO_move[value] = 1
            
        # Check if anyone has won after the move
        cwin = checkWin(playerX_move, playerO_move)
        if (cwin != -1):
            print("Match Over")
            break # Exit the loop if there is a winner
        
        # Switch turns: If 1, becomes 0. If 0, becomes 1.
        turn = 1 - turn
