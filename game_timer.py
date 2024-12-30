import pygame


class GameTimer:
    def __init__(self):
        self.start_time = pygame.time.get_ticks()
        self.paused_time = 0
        self.is_paused = False

    def get_time(self):

        if self.is_paused:
            time = self.paused_time
        else:
            time = pygame.time.get_ticks() - self.start_time

        time = time // 1000
        minutes = time // 60
        seconds = time % 60
        return minutes, seconds
    
    def pause(self):
        if not self.is_paused:
            self.paused_time = pygame.time.get_ticks() - self.start_time
            self.is_paused = True

    def resume(self):
        if self.is_paused:
            self.start_time = pygame.time.get_ticks() - self.paused_time
            self.is_paused = False

    def reset(self):
        self.start_time = pygame.time.get_ticks()
        self.paused_time = 0
        self.is_paused = False