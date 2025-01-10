import random


class AI:
    """
    A class to represent an AI player in Connect Four.

    Attributes
        difficulty(str): The difficulty level of the AI player.
        best_move(int): The best move chosen by the AI player.
    """
    def __init__(self, difficulty):
        """
        Initializes the AI player with the given difficulty level.

        Args:
            difficulty(str): The difficulty level of the AI player.
        """
        self.difficulty = difficulty
        self.best_move = None

    def get_move(self, board):
        """
        Returns the best move for the AI player based on the current game board.

        Args:
            board(list[list[int]]): The current game board state.

        Returns:
            int: The column number of the best move chosen by the AI player.
        """
        if self.difficulty == "easy":
            return self.easy_move(board)
        elif self.difficulty == "medium":
            return self.medium_move(board)
        elif self.difficulty == "hard":
            return self.hard_move(board)

    def easy_move(self, board):
        """
        Returns a random valid move for the AI player.

        Args:
            board(list[list[int]]): The current game board state.

        Returns:
            int: The column number of the random move chosen by the AI player.
        """
        while True:
            move = random.randint(0, len(board[0]) - 1)
            if board[0][move] == 0:
                self.best_move = move
                break
        print ("AI chose a random move")
        return self.best_move
    
    def medium_move(self, board):
        """
        Returns a valid move for the AI player based on the current game board.
        
        The AI priorities:
        1. Win the game if possible.
        2. Block the opponent from winning.
        3. Choose a random move if no other strategies are applicable.

        Args:
            board(list[list[int]]): The current game board state.

        Returns:
            int: The column number of the move chosen by the AI player.
        """
        # check if AI can win
        for col in range(len(board[0])):
            if self.if_valid_move(col, board) and self.check_winning_move(col, 2, board):
                print ("AI found a winning move")
                self.best_move = col
                return self.best_move
            
        # check if player can win and block
        for col in range(len(board[0])):
            if self.if_valid_move(col, board) and self.check_winning_move(col, 1, board):
                print ("AI found a blocking move")
                self.best_move = col
                return self.best_move
            
        # if no winning moves, choose random move
        return self.easy_move(board)
    
    def if_valid_move(self, column, board):
        """
        Checks if the given column is a valid move on the current game board.

        Args:
            column(int): The column number to check.
            board(list[list[int]]): The current game board state.

        Returns:
            bool: True if the column is a valid move, False otherwise.
        """
        return board[0][column] == 0
    
    def check_winning_move(self, column, player, board):
        """
        Checks if the given move will result in a win for the specified player.

        Args:
            column(int): The column number to check.
            player(int): The player number (1 or 2) making the move.
            board(list[list[int]]): The current game board state.

        Returns:
            bool: True if the move results in a win, False otherwise.
        """
        for i in range(len(board)-1, 0, -1):
            if board[i][column] == 0:
                board[i][column] = player
                if self.if_won(player, board):
                    board[i][column] = 0
                    return True
                board[i][column] = 0
                return False
        return False
    
    def hard_move(self, board):
        """
        Chooses the best move for the AI player with advanced strategies.

        The AI priorities:
        1. Win the game if possible.
        2. Block the opponent from winning.
        3. Create opportunities for a 3 in a row (or block the opponent from creating a 3 in a row).
        4. Select a random valid move if no other strategies are applicable.

        Args:
            board(list[list[int]]): The current game board state.

        Returns:
            int: The column number of the move chosen by the AI player.
        """
        # check if AI can win
        for col in range(len(board[0])):
            if self.if_valid_move(col, board) and self.check_winning_move(col, 2, board):
                print ("AI found a winning move")
                self.best_move = col
                return self.best_move
            
        # check if player can win and block
        for col in range(len(board[0])):
            if self.if_valid_move(col, board) and self.check_winning_move(col, 1, board):
                print ("AI found a blocking move")
                self.best_move = col
                return self.best_move
            
        # check if AI can create a 3 in a row and win
        for col in range(len(board[0])):
            if self.if_valid_move(col, board) and self.check_winning_2_move(col, 2, board):
                print ("AI found a winning 2 move")
                self.best_move = col
                return self.best_move

        # check if player can create a 3 in a row and block
        for col in range(len(board[0])):
            if self.if_valid_move(col, board) and self.check_winning_2_move(col, 1, board):
                print ("AI found a blocking 2 move")
                self.best_move = col
                return self.best_move
            
        # if no winning moves, choose random move
        return self.easy_move(board)
    
    def if_won(self, player, board):
        """
        Checks if the given player has won the game.
        The function try to find a 4 in a row in all directions (vertical, horizontal, primary diagonal, secondary diagonal).

        Args:
            player(int): The player number (1 or 2) to check for a win.
            board(list[list[int]]): The current game board state.

        Returns:
            bool: True if the player has won, False otherwise.
        """
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
    
    def check_winning_2_move(self, column, player, board):
        """
        Checks if the given move will result in a 3 in a row for the specified player.

        Args:
            column(int): The column number to check.
            player(int): The player number (1 or 2) making the move.
            board(list[list[int]]): The current game board state.

        Returns:
            bool: True if the move results in a 3 in a row, False otherwise.
        """
        for i in range(len(board)-1, 0, -1):
            if board[i][column] == 0:
                board[i][column] = player
                if self.if_2_won(player, board):
                    board[i][column] = 0
                    return True
                board[i][column] = 0
                return False
        return False
    
    def if_2_won(self, player, board):
        """
        Checks if the given player has a 3 in a row on the game board.
        The function try to find a 3 in a row in all directions (vertical, horizontal, primary diagonal, secondary diagonal).

        Args:
            player(int): The player number (1 or 2) to check for a win.
            board(list[list[int]]): The current game board state.

        Returns:
            bool: True if the player has a 3 in a row, False otherwise.
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == player:
                    # horizontal
                    if (j + 2 < len(board[i]) and board[i][j + 1] == player and board[i][j + 2] == player) and (j - 1 >= 0 and j + 3 < len(board[i]) and board[i][j - 1] == 0 and board[i][j + 3] == 0):
                        return True
                    # vertical
                    if (i + 2 < len(board) and board[i + 1][j] == player and board[i + 2][j] == player) and (i + 3 < len(board) and board[i + 3][j] == 0):
                        return True
                    # primary diagonal
                    if (i + 2 < len(board) and j + 2 < len(board[i]) and board[i + 1][j + 1] == player and board[i + 2][j + 2] == player) and (i - 1 >= 0 and j - 1 >= 0 and i + 3 < len(board) and j + 3 < len(board[i]) and board[i - 1][j - 1] == 0 and board[i + 3][j + 3] == 0):
                        return True
                    # secondary diagonal
                    if (i + 2 < len(board) and j - 2 >= 0 and board[i + 1][j - 1] == player and board[i + 2][j - 2] == player) and (i - 1 >= 0 and j + 1 < len(board[i]) and i + 3 < len(board) and j - 3 >= 0 and board[i - 1][j + 1] == 0 and board[i + 3][j - 3] == 0):
                        return True
        return False