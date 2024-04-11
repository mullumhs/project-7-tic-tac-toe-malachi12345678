
board = []
playerIndex = {0 : "O" , 1 : "X"}
import time
import os

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

def play():
    playsCount = 1  
    winCheck = False

    while winCheck  == False:
        if playsCount == 0:
            playsCount += 1
        else:
            playsCount -= 1

        #print(playerIndex[playsCount])

        colChoice = input("choose column to place in    ")
        colChoice = int(colChoice)
        colChoice   -= 1
        
        for rowChoice in range(5,-1,-1):
            if board[rowChoice][colChoice] == "_":
                for i in range(0,rowChoice):
                    board[i][colChoice] = playerIndex[playsCount]
                    os.system('cls')
                    displayBoard()
                    time.sleep(0.25)
                    board[i][colChoice] = "_"
                    os.system('cls')
                    displayBoard()
                board[rowChoice][colChoice] = playerIndex[playsCount]
                break
            else:
                continue
            
        os.system('cls')
        displayBoard()

        #draw check
        emptySpace = 0
        for rowTest in range(6):
            for colTest in range (5):
                print(board[rowTest][colTest])
                if board[rowTest][colTest] == "_":
                    emptySpace +=1
                else:
                    continue
        if emptySpace > 0:
            winCheck = False
        else:
            print("draw")
            winCheck = True









initialiseBoard()
displayBoard()
play()