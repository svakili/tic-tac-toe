# Tic-Tac-Toe Code in Python

from random import randint

def drawGrid(matrix):
    for row in xrange(0,3):
        for col in xrange(0,3):
            print matrix[row][col],
            if col<2: 
                print "|",
        print "" 
        if row<2:
            print "---------"
    print "\n"
    

def whoToBegin():
    firstPlayer = raw_input("Do you want to start the game? (y/n)")

    if firstPlayer == 'y':
        machineTurn = False
    else:
        machineTurn = True
    return machineTurn

def checkWinner(matrix):
    winner = ' '
    if matrix[0][0] == matrix[1][1] == matrix[2][2]:
        winner = matrix[0][0]
    elif matrix[0][2] == matrix[1][1] == matrix[2][0]:
        winner = matrix[1][1]
    else:
        for line in xrange(0,3):
            if matrix[line][0] == matrix[line][1] == matrix[line][2]:
                winner = matrix[line][0]
            elif matrix[0][line] == matrix[1][line] == matrix[2][line]:
                winner = matrix[0][line]
    
    if winner == 'X':
        return "You Win!"
    elif winner == "O":
        return "You Lose!"
    
    for row in xrange(1,4):
        for col in xrange(1,4):
            if not(isCellFull(matrix, row, col)):
                return ' '
    
    return "It's a draw!"

def isCellFull(matrix, row, col):
    if matrix[row-1][col-1] == ' ': 
        return False
    return True

def machinePlay():
    cellTaken = True
    while cellTaken:
        row = randint(1,3)
        col = randint(1,3)
        cellTaken = isCellFull(matrix, row, col)
    matrix[row-1][col-1] = 'O'
    drawGrid(matrix)

def playerPlay():
    cellTaken = True
    while cellTaken:
        row_s, col_s = raw_input("Enter row and column separated by space: ").split()
        row = int(row_s)
        col = int(col_s)
        cellTaken = isCellFull(matrix, row, col)
        if cellTaken:
            print ("The cell is already taken.")
    matrix[row-1][col-1] = 'X'
    drawGrid(matrix)

matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

machineTurn = whoToBegin()

while checkWinner(matrix) == ' ':
    if machineTurn:
        machinePlay()
        machineTurn = not machineTurn
    else:
        playerPlay()
        machineTurn = not machineTurn

print checkWinner(matrix)