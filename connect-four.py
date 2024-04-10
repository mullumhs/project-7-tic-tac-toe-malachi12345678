
board = []
playerIndex = {0 : "O" , 1 : "X"}
import time

def initialiseBoard():
    for cols in range(6):
        board.append(["_","_","_","_","_","_","_"])
    
def displayBoard():
    print(" 1 2 3 4 5 6 7 ")

    for rows in board:
        print("",end="|")
        for cols in rows:
            
            print(cols, end="|") 
        print("")

def playerTurn():
    playsCount = 1  
    winCheck = False

    while winCheck  == False:
        if playsCount == 0:
            playsCount += 1
        else:
            playsCount -= 1

        print(playerIndex[playsCount])

        colChoice = input("choose column to place in    ")
        colChoice = int(colChoice)
        colChoice   -= 1
        
        for rowTest in range(5,-1,-1):
            if board[rowTest][colChoice] == "_":
                for i in range(0,rowTest):
                    board[i][colChoice] = playerIndex[playsCount]
                    displayBoard()
                    time.sleep(0.25)
                    board[i][colChoice] = "_"
                    displayBoard()
                board[rowTest][colChoice] = playerIndex[playsCount]
                break
            else:
                continue
            
        
        displayBoard()


initialiseBoard()
displayBoard()
playerTurn()