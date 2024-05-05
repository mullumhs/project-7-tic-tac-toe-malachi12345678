#creates emty list "board"
board = []
#used as an index for which token to place
playerIndex = {0 : "O" , 1 : "X"}
#used to allow the player's input to have a corresponding coordinate value
boardIndex = {"A3" : [0 , 0] , "B3" : [1 , 0] , "C3" : [2 , 0] , "3A" : [0 , 0] , "3B" : [1 , 0] , "3C" : [2 , 0] , 
              "A2" : [0 , 1] , "B2" : [1 , 1] , "C2" : [2 , 1] , "2A" : [0 , 1] , "2B" : [1 , 1] , "2C" : [2 , 1] , 
              "A1" : [0 , 2] , "B1" : [1 , 2] , "C1" : [2 , 2] , "1A" : [0 , 2] , "1B" : [1 , 2] , "1C" : [2 , 2] , }
turnsCount = 0
import os

def initialiseBoard():
    #creates a 2d list of 9 squares
    for cols in range(3):
        board.append(["_","_","_"])
   
def displayBoard():
    print("")
    print("")
    print("  _ _ _")
    
    rowIndex = 3 
    for rows in board:
        
        
        print(rowIndex,end="|")
        rowIndex -= 1
        for cols in rows:
            
            print(cols, end="|") 
        print("")

    
    print("  A B C")

def play():
    turnsCount = 0
    playerCount = 1  
    winCheck = False
    drawCheck = False

    while winCheck == False and turnsCount < 9:
        
        if playerCount == 0:
            playerCount += 1
        else:
            playerCount -= 1
        
        while True:
            squareChoice = input("choose column (A,B,C) and row (1,2,3)")
            squareIndex = squareChoice.upper()

            try:
                if board[boardIndex[squareIndex][1]][boardIndex[squareIndex][0]] == "_":
                    board[boardIndex[squareIndex][1]][boardIndex[squareIndex][0]] = playerIndex[playerCount]
                    break
                else:
                    print("square is taken, choose again")
                    continue
            except:
                print("invalid input, choose again")
                continue
       
       
        os.system('cls')
        displayBoard()
        
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2] != "_":
                winCheck = True
                turnsCount += 1 

            elif board[0][row] == board[1][row] == board[2][row] != "_":
                winCheck = True
                turnsCount += 1 

            elif board[0][0] == board[1][1] == board[2][2] != "_":
                winCheck = True
                turnsCount += 1 

            elif board[0][2] == board[1][1] == board[2][0] != "_":
                winCheck = True
                turnsCount += 1 
    
        turnsCount += 1 
    
    if turnsCount == 9:
        print("DRAW")
        input("press enter to continue")
    else:
        
        print(playerIndex[playerCount] , "WINS")
        input("press enter to continue")

def clearBoard():
    #clears the list "board" and clears screen
    board.clear()
    os.system('cls')



while True:
    clearBoard()
    initialiseBoard()
    displayBoard()
    play()

