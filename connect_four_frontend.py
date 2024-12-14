import pygame


# Dimensiuni fereastra
WIDTH = 700
HEIGHT = 700
COLLUMNS = 7
ROWS = 6
CELL_SIZE = min(WIDTH // COLLUMNS, HEIGHT // ROWS, 100)
RADIUS = CELL_SIZE // 2 - 5

# Culori
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (169, 169, 169)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Initializare pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect Four")

# Meniu joc (quit, restart)
def menu():
    pygame.draw.rect(screen, RED, (20,20, WIDTH//2-50, 60), border_top_left_radius=10, border_bottom_left_radius=10, border_top_right_radius=10, border_bottom_right_radius=10)
    pygame.draw.rect(screen, YELLOW, (WIDTH//2+20, 20, WIDTH-400, 60), border_top_right_radius=10, border_bottom_right_radius=10, border_top_left_radius=10, border_bottom_left_radius=10)
    font = pygame.font.Font(None, 36)
    text1 = font.render("Quit", True, BLACK)
    text2 = font.render("Restart", True, BLACK)
    screen.blit(text1, (WIDTH//4-20, 40))
    screen.blit(text2, (WIDTH//4*3-20, 40))
    pygame.display.update()


# Desenare tabla de joc
def draw_board(board):
    screen.fill(GRAY)
    for row in range(ROWS):
        for column in range(COLLUMNS):
            pygame.draw.rect(screen, BLUE, (column * CELL_SIZE, row * CELL_SIZE + CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.circle(screen, BLACK, (column * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE + CELL_SIZE // 2), RADIUS)

    for row in range(ROWS):
        for column in range(COLLUMNS):
            if board[row][column] == 1:
                pygame.draw.circle(screen, RED, (column * CELL_SIZE + CELL_SIZE // 2, HEIGHT - row * CELL_SIZE - CELL_SIZE // 2), RADIUS)
            elif board[row][column] == 2:
                pygame.draw.circle(screen, YELLOW, (column * CELL_SIZE + CELL_SIZE // 2, HEIGHT - row * CELL_SIZE - CELL_SIZE // 2), RADIUS)
    pygame.display.update()

board = []

for i in range(ROWS):
    board.append([])
    for j in range(COLLUMNS):
        board[i].append(0)

# desenare tabla de joc in centru
draw_board(board)

# desenare meniu
menu()

end = 0
while end == 0:
    if end == 1:
        print("Player 1 has won!")