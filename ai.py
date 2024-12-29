import random


class AI:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.best_move = None

    def get_move(self, board):
        if self.difficulty == "easy":
            return self.easy_move(board)
        elif self.difficulty == "medium":
            return self.medium_move(board)
        # elif self.difficulty == "hard":
        #     return self.hard_move(board)

    def easy_move(self, board):
        while True:
            move = random.randint(0, len(board[0]) - 1)
            if board[0][move] == 0:
                self.best_move = move
                break
        return self.best_move
    
    def medium_move(self, board):
        # check if AI can win
        for col in range(len(board[0])):
            if self.if_valid_move(col, board) and self.check_winning_move(col, 2, board):
                self.best_move = col
                return self.best_move
            
        # check if player can win and block
        for col in range(len(board[0])):
            if self.if_valid_move(col, board) and self.check_winning_move(col, 1, board):
                self.best_move = col
                return self.best_move
            
        # if no winning moves, choose random move
        return self.easy_move(board)
    
    def if_valid_move(self, column, board):
        return board[0][column] == 0
    
    def check_winning_move(self, column, player, board):
        for i in range(len(board)):
            if board[i][column] == 0:
                board[i][column] = player
                if self.if_won(player, board):
                    board[i][column] = 0
                    return True
                board[i][column] = 0
        return False
    
    def if_won(self, player, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == player:
                    # horizontal
                    if j + 3 < len(board[i]) and board[i][j + 1] == player and board[i][j + 2] == player and board[i][j + 3] == player:
                        return True
                    # vertical
                    if i + 3 < len(board) and board[i + 1][j] == player and board[i + 2][j] == player and board[i + 3][j] == player:
                        return True
                    # primary diagonal
                    if i + 3 < len(board) and j + 3 < len(board[i]) and board[i + 1][j + 1] == player and board[i + 2][j + 2] == player and board[i + 3][j + 3] == player:
                        return True
                    # secondary diagonal
                    if i + 3 < len(board) and j - 3 >= 0 and board[i + 1][j - 1] == player and board[i + 2][j - 2] == player and board[i + 3][j - 3] == player:
                        return True
        return False