
board = []


def initialiseBoard():
    for cols in range(7):
        board.append(["-","-","-","-","-","-","-"])
    
def displayBoard():
    print(" 1 2 3 4 5 6 7 ")

    for rows in board:
        print("",end="|")
        for cols in rows:
            
            print(cols, end="|") 
        print("")

def playerTurn():
    playsCount = 1

    if playsCount #divsible by 2 remainder 0



initialiseBoard()
displayBoard()