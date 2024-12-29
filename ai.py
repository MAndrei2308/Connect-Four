import random


class AI:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.best_move = None

    def get_move(self, board):
        if self.difficulty == "easy":
            return self.easy_move(board)
        # elif self.difficulty == "medium":
        #     return self.medium_move(board)
        # elif self.difficulty == "hard":
        #     return self.hard_move(board)

    def easy_move(self, board):
        while True:
            move = random.randint(0, len(board[0]) - 1)
            if board[0][move] == 0:
                self.best_move = move
                break
        return self.best_move
    
    