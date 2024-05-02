board = []
playerIndex = {0 : "O" , 1 : "X"}
boardIndex = {"A3" : [0 , 0] , "B3" : [1 , 0] , "C3" : [2 , 0] , "3A" : [0 , 0] , "3B" : [1 , 0] , "3C" : [2 , 0] , 
              "A2" : [0 , 1] , "B2" : [1 , 1] , "C2" : [2 , 1] , "2A" : [0 , 1] , "2B" : [1 , 1] , "2C" : [2 , 1] , 
              "A1" : [0 , 2] , "B1" : [1 , 2] , "C1" : [2 , 2] , "1A" : [0 , 2] , "1B" : [1 , 2] , "1C" : [2 , 2] , }
turnsCount = 0
import os

def initialiseBoard():
    for cols in range(3):
        board.append(["_","_","_"])
   
def displayBoard():
    print("")
    print("")
    print("  _._._")
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
    playsCount = 1  
    winCheck = False

    while winCheck == False and turnsCount < 9:
        if board[0][0] == "x" and board[0][1] == "x" and board[0][2] == "x":
            winCheck = True



        if playsCount == 0:
            playsCount += 1
        else:
            playsCount -= 1
        
        while True:
            squareChoice = input("choose column (A,B,C) and row (1,2,3)")
            squareIndex = squareChoice.upper()

            try:
                if board[boardIndex[squareIndex][1]][boardIndex[squareIndex][0]] == "_":
                    board[boardIndex[squareIndex][1]][boardIndex[squareIndex][0]] = playerIndex[playsCount]
                    break
                else:
                    print("square is taken, choose again")
                    continue
            except:
                print("invalid input, choose again")
                continue
       
        turnsCount += 1
        os.system('cls')
        displayBoard()
    
    print("sigma")    

initialiseBoard()
displayBoard()
play()