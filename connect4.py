import sys
import os

print("------------------")
print("|   Welcome to   |")
print("|   Connect 4    |")
print("------------------")
print()
print("Two players are required for this game.")
print()


def make_board():
    return [["." for _ in range(7)] for _ in range(6)]

def print_board(board):
    for row in board:
        print("".join(row))

def find_landing_row(board,col):
    for row in range(5, -1, -1):
        if board[row][col] == ".":
            return row
    return None

def player1():
    player1choice = input("Player 1, Column 1,2,3,4,5,6,7?:")
    player1choice_valid = int(player1choice)
    col = player1choice_valid - 1
    row = find_landing_row(board,col)
    board[row][col] = "X"

def player2():
    player2choice = input("Player 2, Column 1,2,3,4,5,6,7?:")
    player2choice_valid = int(player2choice)
    col = player2choice_valid - 1
    row = find_landing_row(board,col)
    board[row][col] = "O"

def check_win(board):
    for row in range(6):
        for col in range(7):
            if col <= 3 and board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3] != ".":
                if board[row][col] == "X":
                    return True
                elif board[row][col] == "O":
                    return False
            if row <= 2 and board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] != ".":
                if board[row][col] == "X":
                    return True
                elif board[row][col] == "O":
                    return False
    return None

def win_confirm(x_win):
    if x_win == True:
        print()
        print("Congrats! X Won!")
    if x_win == False:
        print()
        print("Congrats! O Won!")
    return

def play_again(board):
    again = input("Do you want to play Connect 4 again? (y/n): ").strip().lower()
    if again == "y":
        return
    elif again == "n":
        sys.exit()
    else:
        print()
        print("Please enter 'y' or 'n'.")
        print()
        again = input("Do you want to play Connect 4 again? (y/n): ").strip().lower()
        if again == "y":
            return
        elif again == "n":
            sys.exit()
        else:
            sys.exit()

board = make_board()
print_board(board)
x_win = None

while x_win == None:
    player1()
    x_win = check_win(board)
    if x_win != None:
        win_confirm(x_win)
        play_again(board)
        board = make_board()
        print_board(board)
        player1()
    print_board(board)
    player2()
    x_win = check_win(board)
    if x_win != None:
        win_confirm(x_win)
        play_again(board)
        board = make_board()
        x_win = None
    print_board(board)
