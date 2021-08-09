"""This program runs a digital version of the game "Connect Four" so that two users
can play together!
Project name: connectFour.py
File name: project6
Created by: James Lawson and Beth Ann Townsend
"""

#math is imported
import math

def main():
    #creates board
    board=[]
    #variables are set
    column = 0
    counter = 0
    token = ""
    create(board)
    row = len(board) - 1
    notOver = True
    while notOver == True:
        placeToken(board, counter, token)
        counter = counter + 1

#prints a key below the board so that the user knows which column is which
def printList():
    print("0", "  ", "1", "  ", "2", "  ", "3", "  ", "4", "  ", "5") 

#creates the board
def create(board):
    for row in range(7):
        row = []
        for col in range(6):
            row.append("0")
        board.append(row)
    return board

#displays the board
def display(board):
    print('\n'.join([''.join(['{:5}'.format(item) for item in row]) for row in board]))
    print("---------------------------")
    printList()

#places the token
def placeToken(board, counter, token):
    display(board)
    row = len(board) - 1
    if counter % 2 == 0:
        token = "R"
    if counter % 2 == 1:
        token = "Y"
    #user inputs which column they would like to place a token
    column = int(input("Enter column for turn " + token + ": "))
    while board[row][column] != "0":
        row = row - 1
    else:
        #token is added to board
        board[row][column]=token
        #checks for a winning move
        checkHorizontal(board, row, column)
        checkVertical(board, row, column)
        checkDiagonal(board, row, column)

#checks to see if there is 4 in a row horizontal
def checkHorizontal(board, row, column):
    #checking from the right
    if column >= 3:
        if board[row][column] == board[row][column - 1] and board[row][column] == board[row][column - 2] and board[row][column] == board[row][column - 3]:
            #board is displayed
            display(board)
            #message is printed that you have won
            print("You win!")
            #program exists
            exit()

    #checking from the left
    if column <= 2:
        if board[row][column] == board[row][column + 1] and board[row][column] == board[row][column + 2] and board[row][column] == board[row][column + 3]:
            #board is displayed
            display(board)
            #message is printed that you have won
            print("You win!")
            #program exists
            exit()
        
    #chcking from 2nd to right
    if column >= 2 and column < 5:
        if board[row][column] == board[row][column + 1] and board[row][column] == board[row][column - 1] and board[row][column] == board[row][column - 2]:
            #board is displayed
            display(board)
            #message is printed that you have won
            print("You win!")
            #program exists
            exit()
        
    #checking from 2nd to left
    if column <= 3 and column > 0:
        if board[row][column] == board[row][column - 1] and board[row][column] == board[row][column + 1] and board[row][column] == board[row][column + 2]:
            #board is displayed
            display(board)
            #message is printed that you have won
            print("You win!")
            #program exists
            exit()

#checks to see if there is 4 in a row vertical
def checkVertical(board, row, column):
    if row <= 3:
        if board[row][column] == board[row + 1][column] and board[row][column] == board[row + 2][column] and board[row][column] == board[row + 3][column]:
            #board is displayed
            display(board)
            #message is printed that you have won
            print("You win!")
            #program exists
            exit()

#checks to see if there is 4 in a row diagonal
def checkDiagonal(board, row, column):
    #downRight
    if column <= 2 and row <= 4 and column > 0 and row > 1:
        if board[row][column] == board[row + 1][column + 1] and board[row][column] == board[row + 2][column + 2] and board[row][column] == board[row + 3][column + 3]:
            #board is displayed
            display(board)
            #message is printed that you have won
            print("You win!")
            #program exists
            exit()
    
    #downLeft
    if column >= 2 and row < 4 and column > 0:
        if board[row][column] == board[row + 1][column - 1] and board[row][column] == board[row + 2][column - 2] and board[row][column] == board[row + 3][column - 3]:
            #board is displayed
            display(board)
            #message is printed that you have won
            print("You win!")
            #program exists
            exit()
    
    #upRight
    if column <= 2 and row >= 2 and row > 0:
        if board[row][column] == board[row - 1][column + 1] and board[row][column] == board[row - 2][column + 2] and board[row][column] == board[row - 3][column + 3]:
            #board is displayed
            display(board)
            #message is printed that you have won
            print("You win!")
            #program exists
            exit()
    
    #upLeft
    if column >= 2 and row >= 2 and row < 4:
        if board[row][column] == board[row - 1][column - 1] and board[row][column] == board[row - 2][column - 2] and board[row][column] == board[row - 3][column - 3]:
            #board is displayed
            display(board)
            #message is printed that you have won
            print("You win!")
            #program exists
            exit()
    
    #downLeftTwo
    if column >= 2 and row <= 5 and row > 0 and column < 5:
        if board[row][column] == board[row - 1][column + 1] and board[row][column] == board[row + 1][column - 1] and board[row][column] == board[row + 2][column - 2]:
            #board is displayed
            display(board)
            #message is printed that you have won
            print("You win!")
            #program exists
            exit()
       
    #downLeftThree
    if column < 4 and row >= 2 and column > 0 and row < 5:
        if board[row][column] == board[row + 1][column - 1] and board[row][column] == board[row - 1][column + 1] and board[row][column] == board[row - 2][column + 2]:
            #board is displayed
            display(board)
            #message is printed that you have won
            print("You win!")
            #program exists
            exit()
    
    #downRightTwo
    if column <= 4 and row <= 5 and column > 0 and row > 0:
        if board[row][column] == board[row - 1][column - 1] and board[row][column] == board[row + 1][column + 1] and board[row][column] == board[row + 2][column + 2]:
            #board is displayed
            display(board)
            #message is printed that you have won
            print("You win!")
            #program exists
            exit()
    
    #downRightThree
    if column >= 2 and row >= 1 and row < 5 and column <= 4:
        if board[row][column] == board[row + 1][column + 1] and board[row][column] == board[row - 1][column - 1] and board[row][column] == board[row - 2][column - 2]:
            #board is displayed
            display(board)
            #message is printed that you have won
            print("You win!")
            #program exists
            exit()

if __name__ == "__main__":
    main()
