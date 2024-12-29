import pygame
import sys

from ai import AI
from connect_four import ConnectFour, get_params
from constants import Constants



pygame.init()

# _, ROWS, COLUMNS, first_player = get_params()
ROWS = 6
COLUMNS = 7
first_player = "human1"

# Dimensiuni fereastra si afisare
WIDTH = 700
HEIGHT = 700

CELL_SIZE = WIDTH // COLUMNS
RADIUS = CELL_SIZE // 2 - 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect Four")

# Culori
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (169, 169, 169)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Fonturi
FONT_LARGE = pygame.font.Font(None, 74)
FONT_MEDIUM = pygame.font.Font(None, 50)
FONT_SMALL = pygame.font.Font(None, 36)


def draw_button(text, text_color, text_font, x, y, width, height, color, hover_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Verificare daca mouse-ul este pe buton
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))

    # Desenare text pe buton
    text_surface = text_font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center = (x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)
    return False

def show_about():
    running = True
    while running:
        screen.fill(WHITE)
        text_surface = FONT_MEDIUM.render("About", True, BLACK)
        screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 6))

        about_text = [
            "Connect Four is a two-player connection game.",
            "Players take turns dropping colored discs into a column.",
            "The first to align four discs horizontally, vertically,",
            "or diagonally wins the game!",
            "Challenge yourself or play against AI!"
        ]

        for i, line in enumerate(about_text):
            line_surface = FONT_SMALL.render(line, True, BLACK)
            screen.blit(line_surface, (WIDTH // 2 - line_surface.get_width() // 2, HEIGHT // 3 + i * 40))

        back_button = draw_button("Back", BLACK, FONT_SMALL, WIDTH // 2 - 100, HEIGHT - 200, 200, 50, GRAY, BLUE)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if back_button:
                running = False

def show_play():
    running = True
    while running:
        screen.fill(WHITE)
        text_surface = FONT_LARGE.render("Play", True, BLACK)
        screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 6))

        pvp_button = draw_button("Player vs Player", BLACK, FONT_SMALL, WIDTH // 2 - 125, HEIGHT // 3, 250, 50, GRAY, BLUE)
        pvc_button = draw_button("Player vs Computer", BLACK, FONT_SMALL, WIDTH // 2 - 125, HEIGHT // 3 + 100, 250, 50, GRAY, BLUE)
        back_button = draw_button("Back", BLACK, FONT_SMALL, WIDTH // 2 - 125, HEIGHT // 3 + 200, 250, 50, GRAY, BLUE)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pvp_button:
                print("Player vs Player button pressed")
                show_pvp()
            if pvc_button:
                print("Player vs Computer button pressed")
                show_pvc()
            if back_button:
                running = False

def show_pvc():
    running = True
    while running:
        screen.fill(WHITE)
        text_surface = FONT_LARGE.render("Player vs Computer", True, BLACK)
        screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 6))

        easy_button = draw_button("Easy", BLACK, FONT_SMALL, WIDTH // 2 - 125, HEIGHT // 3, 250, 50, GRAY, BLUE)
        medium_button = draw_button("Medium", BLACK, FONT_SMALL, WIDTH // 2 - 125, HEIGHT // 3 + 100, 250, 50, GRAY, BLUE)
        hard_button = draw_button("Hard", BLACK, FONT_SMALL, WIDTH // 2 - 125, HEIGHT // 3 + 200, 250, 50, GRAY, BLUE)
        back_button = draw_button("Back", BLACK, FONT_SMALL, WIDTH // 2 - 125, HEIGHT // 3 + 300, 250, 50, GRAY, BLUE)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if easy_button:
                print("Easy button pressed")
                start_pvc_game("easy")
            if medium_button:
                print("Medium button pressed")
                start_pvc_game("medium")
            if hard_button:
                print("Hard button pressed")
                start_pvc_game("hard")
            if back_button:
                running = False

def start_pvc_game(difficulty):
    ai_player = AI(difficulty)
    game = ConnectFour("Player", f"Computer {difficulty}", ROWS, COLUMNS, 1)
    running = True
    if first_player == "human":
        turn = 1
    else:
        turn = 2

    while running:
        draw_board(game.board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if turn == 1 and event.type == pygame.MOUSEBUTTONDOWN:
                column = get_column(event.pos[0])
                if game.if_valid_move(column):
                    game.apply_move(column, turn)

                    if game.check_end_game():
                        print("Game ended")
                        if game.winner:
                            winner_text = f"{game.winner}, wins!"
                        else:
                            winner_text = "It's a tie!"
                        display_end_message(winner_text)
                        running = False
                        break
                    turn = 2
        if turn == 2:
            pygame.time.wait(200)
            column = ai_player.get_move(game.board)
            if game.if_valid_move(column):
                game.apply_move(column, turn)

                if game.check_end_game():
                    print("Game ended")
                    if game.winner:
                        winner_text = f"{game.winner}, wins!"
                    else:
                        winner_text = "It's a tie!"
                    display_end_message(winner_text)
                    running = False
                    break
                turn = 1
                
def draw_board(board):
    for row in range(ROWS):
        for col in range(COLUMNS):
            pygame.draw.rect(screen, BLUE, (col * CELL_SIZE, row * CELL_SIZE + CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.circle(screen, WHITE, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE + CELL_SIZE // 2), RADIUS)
    for row in range(ROWS):
        for col in range(COLUMNS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE + CELL_SIZE // 2), RADIUS)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, YELLOW, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE + CELL_SIZE // 2), RADIUS)
    pygame.display.update()

def get_column(mouse_x):
    return mouse_x // CELL_SIZE

def show_pvp():
    print(f"Starting in PvP mode with {ROWS} rows and {COLUMNS} columns")
    if first_player == "human1":
        turn = 1
    elif first_player == "human2":
        turn = 2 
    game = ConnectFour("Player1", "Player2", ROWS, COLUMNS, first_player)
    running = True

    while running:
        draw_board(game.board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                column = get_column(event.pos[0])
                if game.if_valid_move(column):
                    game.apply_move(column, turn)

                    if game.check_end_game():
                        print("Game ended")
                        if game.winner:
                            winner_text = f"{game.winner}, wins!"
                        else:
                            winner_text = "It's a tie!"
                        display_end_message(winner_text)
                        running = False
                        break
                
                if turn == 1:
                    turn = 2
                else:
                    turn = 1

def display_end_message(message):
    screen.fill(WHITE)
    text_surface = FONT_MEDIUM.render(message, True, BLACK)
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

def show_menu():
    running = True
    while running:
        screen.fill(WHITE)

        # Titlul
        text_surface = FONT_LARGE.render("Connect Four", True, BLACK)
        screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 4))

        # Butoane
        play_button = draw_button("Play", BLACK, FONT_MEDIUM, WIDTH // 2 - 100, HEIGHT // 2, 200, 50, GRAY, BLUE)
        about_button = draw_button("About", BLACK, FONT_MEDIUM, WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 50, GRAY, BLUE)
        exit_button = draw_button("Exit", BLACK, FONT_MEDIUM, WIDTH // 2 - 100, HEIGHT // 2 + 200, 200, 50, GRAY, BLUE)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if play_button:
                print("Play button pressed")
                show_play()
            if about_button:
                print("About button pressed")
                show_about()
            if exit_button:
                pygame.quit()
                sys.exit()

show_menu()