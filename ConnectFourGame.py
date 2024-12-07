import sys

# initializarea tablei de joc
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

# aplicarea mutarii
def apply_move(board, column, player):
    for i in range(len(board) - 1, -1, -1):
        if board[i][column] == 0:
            board[i][column] = player
            return True
    return False

# validarea mutarii
def if_valid_move(board, column):
    if column < 0 or column >= len(board[0]):
        print("Invalid column. Please enter a value between 0 and", len(board[0]) - 1)
        return False
    if board[0][column] != 0:
        print("Column is full. Please try another column.")
        return False
    return True

# obtinerea parametrilor
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

# verificarea daca tabla de joc este plina (remiza)
def if_board_full(board):
    for row in board:
        for cell in row:
            if cell == 0:
                return False
    return True

# verificarea daca un jucator a castigat
def if_won(board, player):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == player:
                # verificarea pe linie
                if j + 3 < len(board[i]) and board[i][j + 1] == player and board[i][j + 2] == player and board[i][j + 3] == player:
                    return True
                # verificarea pe coloana
                if i + 3 < len(board) and board[i + 1][j] == player and board[i + 2][j] == player and board[i + 3][j] == player:
                    return True
                # verificarea pe diagonala principala
                if i + 3 < len(board) and j + 3 < len(board[i]) and board[i + 1][j + 1] == player and board[i + 2][j + 2] == player and board[i + 3][j + 3] == player:
                    return True
                # verificarea pe diagonala secundara
                if i + 3 < len(board) and j - 3 >= 0 and board[i + 1][j - 1] == player and board[i + 2][j - 2] == player and board[i + 3][j - 3] == player:
                    return True
    return False

def check_end_game(board, player):
    if if_won(board, player):
        print(f"Player {player} has won!")
        return True
    if if_board_full(board):
        print("It's a tie!")
        return True


# rularea jocului
def run_game():
    rows, columns = get_params()
    board = initialize_board(rows, columns)
    print_board(board)

    current_player = 1
    
    while True:
        try:
            column = int(input(f"Player {current_player}, please enter a column: "))
        except ValueError:
            print("Invalid column. Please enter an integer value.")
            continue
        if if_valid_move(board, column):
            apply_move(board, column, current_player)
            print_board(board)
            if check_end_game(board, current_player):
                break
            current_player = 3 - current_player

run_game()