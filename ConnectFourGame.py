# initializarea tablei de joc
import sys


def initialize_board(rows, columns):
    board = []
    for i in range(rows):
        board.append([])
        for j in range(columns):
            board[i].append(0)
    return board

# afisarea tablei de joc
def print_board(board):
    for row in board:
        print(row)

# rulara jocului
def run_game():

    if len(sys.argv) != 3:
        print("Usage: python ConnectFourGame.py <rows> <columns>")
        return

    rows = int(sys.argv[1])
    columns = int(sys.argv[2])
    
    board = initialize_board(rows, columns)
    print_board(board)

run_game()