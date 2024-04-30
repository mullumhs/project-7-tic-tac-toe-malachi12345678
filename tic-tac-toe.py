board = []
playerIndex = {0 : "O" , 1 : "X"}
import time
import os

def initialiseBoard():
    for cols in range(3):
        board.append(["_","_","_"])
    
def displayBoard():
    for rows in board:
        rowIndex = 3
        print(rowIndex,end="|")
        rowIndex -= 1
        for cols in rows:
            
            print(cols, end="|") 
        print("")
    
    print(" A B C")

    

initialiseBoard()
displayBoard()