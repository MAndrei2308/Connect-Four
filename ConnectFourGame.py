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
    print()

def apply_move(board, column, player):
    for i in range(len(board) - 1, -1, -1):
        if board[i][column] == 0:
            board[i][column] = player
            return True
    return False

def if_valid_move(board, column):
    if column < 0 or column >= len(board[0]):
        print("Invalid column. Please enter a value between 0 and", len(board[0]) - 1)
        return False
    if board[0][column] != 0:
        print("Column is full. Please try another column.")
        return False
    return True

# rulara jocului
def get_params():
    if len(sys.argv) != 3:
        print("Usage: python ConnectFourGame.py rows columns")
        sys.exit(1)
    try:
        rows = int(sys.argv[1])
        columns = int(sys.argv[2])
    except ValueError:
        print("Invalid parameters. Please provide integer values for rows and columns.")
        sys.exit(1)
    if rows <= 0 or columns <= 0:
        print("Invalid parameters. Please provide positive values for rows and columns.")
        sys.exit(1)
    return rows, columns

def run_game():
    rows, columns = get_params()
    board = initialize_board(rows, columns)
    print_board(board)

    current_player = 1
    
    while True:
        column = int(input(f"Player {current_player}, please enter a column: "))
        if if_valid_move(board, column):
            apply_move(board, column, current_player)
            print_board(board)
            current_player = 3 - current_player


run_game()