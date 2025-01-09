import sys

from ai import AI

class ConnectFour:
    """
    A class to represent a Connect Four game.

    Attributes
        player1(str): The name or identifier of player 1.
        player2(str): The name or AI instance of player 2.
        current_player(str or AI): The player whose turn it currently is.
        rows(int): The number of rows in the game board.
        columns(int): The number of columns in the game board.
        board(list[list[int]]): The game board represented as a 2D list.
        winner(str): The name of the player who won the game, if any.
        game_ended(bool): A flag to indicate if the game has ended.
    """
    def __init__(self, player1, player2, rows, columns, first_player):
        """
        Initializes the ConnectFour game with the given playres and board dimensions.

        Args:
            player1(str): The name or identifier of player 1.
            player2(str or AI): The name or AI instance of player 2.
            rows(int): The number of rows in the game board.
            columns(int): The number of columns in the game board.
            first_player(str or AI): The player who starts the game.
        """

        self.player1 = player1
        self.player2 = player2
        self.current_player = first_player
        self.rows = rows
        self.columns = columns
        self.board = self.create_board()
        self.winner = None
        self.game_ended = False

    def create_board(self):
        """
        Creates an empty game board with the given number of rows and columns.

        Returns:
            list[list[int]]: A 2D list representing the empty game board.
        """
        board = []
        for i in range(self.rows):
            board.append([])
            for j in range(self.columns):
                board[i].append(0)
        return board
    
    def print_board(self):
        """
        Prints the current state of the game board to console.
        """
        for row in self.board:
            print(row)
        print()

    def apply_move(self, column, player):
        """
        Applies the given move to the game board for the specified player.

        Args:
            column(int): The column where the player wants to place their piece.
            player(int): The player number (1 or 2) making the move.

        Returns:
            bool: True if the move was successfully applied, False otherwise.
        """
        for i in range(len(self.board) - 1, -1, -1):
            if self.board[i][column] == 0:
                self.board[i][column] = player
                return True
        return False
    
    def if_valid_move(self, column):
        """
        Checks if the given column is a valid move for the current player.

        Args:
            column(int): The column where the player wants to place their piece.

        Returns:
            bool: True if the move is valid, False otherwise
        """
        if column < 0 or column >= len(self.board[0]):
            print("Invalid column. Please enter a value between 0 and", len(self.board[0]) - 1)
            return False
        if self.board[0][column] != 0:
            print("Column is full. Please try another column.")
            return False
        return True
    
    def if_board_full(self):
        """
        Checks if the game board is full.

        Returns:
            bool: True if the board is full, False otherwise
        """
        for row in self.board:
            for cell in row:
                if cell == 0:
                    return False
        return True
    
    def if_won(self, player):
        """
        Checks if the given player has won the game.

        Args:
            player(int): The player number (1 or 2) to check for a win.

        Returns:
            bool: True if the player has won, False otherwise
        """
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
        """
        Checks if the game has ended either by a win or a tie.

        Returns:
            bool: True if the game has ended, False otherwise
        """
        if self.if_won(1):
            self.winner = "Player 1"
            self.game_ended = True
        elif self.if_won(2):
            self.winner = "Player 2"
            self.game_ended = True
        elif self.if_board_full():
            self.game_ended = True
        return self.game_ended
        
    def get_move(self):
        """
        Gets the next move from the current player.

        Returns:
            int or None: The column where the player wants to place their piece, or None if input is invalid.
        """
        if isinstance(self.current_player, AI):
            column = self.current_player.easy_move(self.board)
            print(f"{self.current_player.difficulty} AI chose column {column}")
        else:
            try:    
                column = int(input(f"{self.current_player}, enter column: "))
            except ValueError:
                print("Invalid column. Please enter an integer value.")
                return None
        return column
    
    def run_game(self):
        """
        Runs the Connect Four game loop until the game ends.
        """
        self.print_board()
        while not self.game_ended:
            column = self.get_move()
            if column is None:
                continue

            if self.if_valid_move(column):
                if self.current_player == self.player1:
                    player_value = 1
                else:
                    player_value = 2
                if self.apply_move(column, player_value):
                    self.print_board()
                    if self.check_end_game():
                        if self.winner:
                            print("Player", self.winner, "won!")
                        else:
                            print("It's a tie!")
                    if self.current_player == self.player1:
                        self.current_player = self.player2
                    else:
                        self.current_player = self.player1
            else:
                print("Invalid move. Please try again.")
        print("Game over.")

def get_params():
    """
    Gets the game parameters from the command line arguments.

    Returns:
        tuple: A tuple containing the oponent type, number of rows, number of columns, and the first player.
    """
    if len(sys.argv) != 5:
        print("Usage: python connect_four.py <oponent_type> <rows> <columns> <first_player>")
        print("Example: python connect_four.py human 6 7 human1")
        sys.exit(1)
    try:
        oponent_type = sys.argv[1]
        rows = int(sys.argv[2])
        columns = int(sys.argv[3])
        first_player = sys.argv[4]
    except ValueError:
        print("Invalid parameters. Please provide integer values for rows and columns.")
        sys.exit(1)
    if rows <= 0 or columns <= 0:
        print("Invalid parameters. Please provide positive values for rows and columns.")
        sys.exit(1)

    return oponent_type, rows, columns, first_player

def if_terminal_input():
    """
    Checks if the game parameters are 5.

    Returns:
        bool: True if the number of arguments is 5, False otherwise.
    """
    return len(sys.argv) == 5

if __name__ == "__main__":
    if len(sys.argv) > 1:
        oponent_type, rows, columns, first_player = get_params()
    else:
        oponent_type = "human"
        rows = 6
        columns = 7
        first_player = "human1"
        
    player1 = "human1"
    if oponent_type == "human":
        player2 = "human2"
        if first_player == "human1":
            first_player = player1
        elif first_player == "human2":
            first_player = player2 
        else:
            print("Invalid first player. Please choose human1 or human2.")
            sys.exit(1)

        # Fronend
        from connect_four_front import show_pvp
        show_pvp()
        sys.exit(0)

    elif oponent_type == "computer":
        player2 = AI("easy")
        if first_player == "human":
            first_player = player1
        elif first_player == "computer":
            first_player = player2
        else:
            print("Invalid first player. Please choose human or computer.")
            sys.exit(1)

        # Fronend
        from connect_four_front import show_pvc
        show_pvc()
        sys.exit(0)

    else:
        print("Invalid oponent type. Please choose human or computer.")
        sys.exit(1)
        
    # game = ConnectFour(player1, player2, rows, columns, first_player)
    # game.run_game()