import pygame
import sys

from constants import Constants



pygame.init()

# Dimensiuni fereastra si afisare
WIDTH = 700
HEIGHT = 700
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
        screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 3))

        back_button = draw_button("Back", BLACK, FONT_SMALL, WIDTH // 2 - 100, HEIGHT // 2, 200, 50, GRAY, BLUE)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if back_button:
                running = False

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
            if about_button:
                print("About button pressed")
                show_about()
            if exit_button:
                pygame.quit()
                sys.exit()

show_menu()