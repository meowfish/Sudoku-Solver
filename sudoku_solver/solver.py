import random
import generate
defaultBoard = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]

board = generate.checkBoard(defaultBoard)
    
#prints the board by traversing through matrix
def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
                print("------------------------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ",end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j])+" ", end="")

#finds the first empty space and returns the coordinate
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == 0):
                return (i,j)
    return False

#check if the input is valid
def check(board, number, position):
    #check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    #check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False
    #check the whole box
    box_row = position[1]//3
    box_column = position[0]//3
    for y in range(box_column*3, box_column*3 + 3):
        for x in range(box_row*3, box_row*3 + 3):
            if board[y][x] == number and (y,x) != position:
                return False
    return True

#solves the sudoku
def solution(board):
    #gets the coordinates
    found = findEmpty(board)
    if not found:
        return True
    else:
        row, column = found
    #go through all numbers on each space
    for i in range(1,10):
        if check(board, i, (row, column)):
            board[row][column] = i

            if solution(board):
                return True

            board[row][column] = 0
    return False

def main(board):
    printBoard(board)
    value = input("\n If you would like to see the answer, press b\n")
    if value == "b":
        print("\n\n\n\n")
        solution(board)
        printBoard(board)
