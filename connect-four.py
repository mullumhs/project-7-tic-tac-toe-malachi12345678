
board = []
playerIndex = {0 : "O" , 1 : "X"}

def initialiseBoard():
    for cols in range(7):
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
  
    if playsCount == 0:
        playsCount += 1
    else:
        playsCount -= 1

    print(playerIndex[playsCount])



playerTurn()
initialiseBoard()
displayBoard()
input()
