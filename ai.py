import random


class AI:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.best_move = None

    def easy_move(self, board):
        while True:
            move = random.randint(0, len(board[0]) - 1)
            if board[0][move] == 0:
                return move
        
    