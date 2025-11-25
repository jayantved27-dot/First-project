def tic_tac_toe(a, b, c):
    return a + b + c

def printBoard(playerX_move, playerO_move):
    zero = 'X' if playerX_move[0] else ('O' if playerO_move[0] else 0)
    one = 'X' if playerX_move[1] else ('O' if playerO_move[1] else 1)
    two = 'X' if playerX_move[2] else ('O' if playerO_move[2] else 2)
    three = 'X' if playerX_move[3] else ('O' if playerO_move[3] else 3)
    four = 'X' if playerX_move[4] else ('O' if playerO_move[4] else 4)
    five = 'X' if playerX_move[5] else ('O' if playerO_move[5] else 5)
    six = 'X' if playerX_move[6] else ('O' if playerO_move[6] else 6)
    seven = 'X' if playerX_move[7] else ('O' if playerO_move[7] else 7)
    eight = 'X' if playerX_move[8] else ('O' if playerO_move[8] else 8) 
     
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")

def checkWin(playerX_move, playerO_move):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
     
    for win in wins:
        if(tic_tac_toe(playerX_move[win[0]], playerX_move[win[1]], playerX_move[win[2]]) == 3):
            return 1
        
        if(tic_tac_toe(playerO_move[win[0]], playerO_move[win[1]], playerO_move[win[2]]) == 3):
            return 0
             
    return -1

if __name__ == "__main__":
    playerX_move = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    playerO_move = [0, 0, 0, 0, 0, 0, 0, 0, 0]
     
    turn = 1
    print("Welcome to Tic Tac Toe")
    
    total_moves = 0
     
    while(True):
        printBoard(playerX_move, playerO_move)
         
        if(turn == 1):
            print("X's chance")
            value = int(input("Please enter a value[0-8]: "))
            
            if playerX_move[value] == 1 or playerO_move[value] == 1:
                print("Spot already taken! Try again.")
                continue
            
            playerX_move[value] = 1
        else:
            print("O's chance")
            value = int(input("Please enter a value[0-8]: "))
            
            if playerX_move[value] == 1 or playerO_move[value] == 1:
                print("Spot already taken! Try again.")
                continue
                
            playerO_move[value] = 1
             
        total_moves += 1
        
        cwin = checkWin(playerX_move, playerO_move)
        
        if (cwin != -1):
            printBoard(playerX_move, playerO_move)
            print("Match Over")
            if cwin == 1:
                print("Result: X won the match!")
            else:
                print("Result: O won the match!")
            break
        
        if total_moves == 9:
            printBoard(playerX_move, playerO_move)
            print("Match Over")
            print("Result: It's a Draw!")
            break
         
        turn = 1 - turn
