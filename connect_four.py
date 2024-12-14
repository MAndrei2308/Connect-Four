import sys


class ConnectFour:
    def __init__(self, player, rows, columns):
        self.player = player
        self.rows = rows
        self.columns = columns
        self.board = self.create_board()
        self.winner = None
        self.game_ended = False

    def create_board(self):
        board = []
        for i in range(self.rows):
            board.append([])
            for j in range(self.columns):
                board[i].append(0)
        return board
    
    def print_board(self):
        for row in self.board:
            print(row)
        print()

    def apply_move(self, column, player):
        for i in range(len(self.board) - 1, -1, -1):
            if self.board[i][column] == 0:
                self.board[i][column] = player
                return True
        return False
    
    def if_valid_move(self, column):
        if column < 0 or column >= len(self.board[0]):
            print("Invalid column. Please enter a value between 0 and", len(board[0]) - 1)
            return False
        if self.board[0][column] != 0:
            print("Column is full. Please try another column.")
            return False
        return True
    
    def if_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == 0:
                    return False
        return True
    
    def if_won(self, player):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == player:
                    # horizontal
                    if j + 3 < len(self.board[i]) and self.board[i][j + 1] == player and self.board[i][j + 2] == player and self.board[i][j + 3] == player:
                        return True
                    # vertical
                    if i + 3 < len(self.board) and self.board[i + 1][j] == player and self.board[i + 2][j] == player and self.board[i + 3][j] == player:
                        return True
                    # primary diagonal
                    if i + 3 < len(self.board) and j + 3 < len(self.board[i]) and self.board[i + 1][j + 1] == player and self.board[i + 2][j + 2] == player and self.board[i + 3][j + 3] == player:
                        return True
                    # secondary diagonal
                    if i + 3 < len(self.board) and j - 3 >= 0 and self.board[i + 1][j - 1] == player and self.board[i + 2][j - 2] == player and self.board[i + 3][j - 3] == player:
                        return True
        return False
    
    def check_end_game(self):
        if self.if_won(1):
            self.winner = 1
            self.game_ended = True
        elif self.if_won(2):
            self.winner = 2
            self.game_ended = True
        elif self.if_board_full():
            self.game_ended = True
        return self.game_ended
    
    def run_game(self):
        self.print_board()
        while not self.game_ended:
            try:
                column = int(input(f"Player {self.player}, please enter a column: "))
            except ValueError:
                print("Invalid column. Please enter an integer value.")
                continue
            if self.if_valid_move(column):
                self.apply_move(column, self.player)
                self.print_board()
                if self.check_end_game():
                    if self.winner:
                        print(f"Player {self.winner} has won!")
                    else:
                        print("It's a tie!")
                    break
                self.player = 3 - self.player

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

if __name__ == "__main__":
    rows, columns = get_params()
    game = ConnectFour(1, rows, columns)
    game.run_game()