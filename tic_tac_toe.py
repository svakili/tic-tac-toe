# Tic-Tac-Toe Code in Python

from random import randint

matrix = [[' ', ' ', ' '],[' ', ' ', ''],[' ', ' ', ' ']]

def drawGrid(matrix):
    for row in xrange(0,3):
        for col in xrange(0,3):
            print matrix[row][col],
            if col<2: 
                print "|",
        print "\n" 
        if row<2:
            print "---------"
    
firstPlayer = raw_input("Do you want to start the game? (y/n)")

if firstPlayer == 'y':
    machineTurn = False
else:
    machineTurn = True

def checkWinner(matrix):
    for line in xrange(0,3):
        if matrix[line][0] == matrix[line][1] == matrix[line][2]:
            return matrix[line][0]
        elif matrix[0][line] == matrix[1][line] == matrix[2][line]:
            return matrix[0][line]
    
    if matrix[0][0] == matrix[1][1] == matrix[2][2]:
        return matrix[0][0]
    elif matrix[0][2] == matrix[1][1] == matrix[2][0]:
        return matrix[1][1]

    return ' '

def checkCell(matrix, row, col):
    if matrix[row-1][col-1] == ' ': 
        return False
    return True

while True:
    if machineTurn:
        cellTaken = True
        while cellTaken:
            row = randint(1,3)
            col = randint(1,3)
            cellTaken = checkCell(matrix, row, col)
        matrix[row-1][col-1] = 'O'
        drawGrid(matrix)
        if checkWinner(matrix) != ' ':
            break
        machineTurn = not machineTurn
    else:
        cellTaken = True
        while cellTaken:
            row_s, col_s = raw_input("Enter row and column separated by space: ").split()
            row = int(row_s)
            col = int(col_s)
            cellTaken = checkCell(matrix, row, col)
            if cellTaken:
                print ("The cell is already taken.")
        matrix[row-1][col-1] = 'X'
        drawGrid(matrix)
        if checkWinner(matrix) != ' ':
            break
        machineTurn = not machineTurn

print "You Win" if checkWinner(matrix) == "X" else "You Lose"