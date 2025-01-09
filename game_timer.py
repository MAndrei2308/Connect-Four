import pygame


class GameTimer:
    """
    A class to represent a game timer.

    This timer traks the elapsed time in a game, supports pausing, resuming and resetting.

    Attributes
        start_time(int): The time when the timer was started.
        paused_time(int): The time when the timer was paused.
        is_paused(bool): A flag to indicate if the timer is currently paused.
    """
    def __init__(self):
        """
        Initializes the GameTimer with the current time as the start time.
        """
        self.start_time = pygame.time.get_ticks()
        self.paused_time = 0
        self.is_paused = False

    def get_time(self):
        """
        Calculates the elapsed time in minutes and seconds.

        Returns:
            tuple(int, int): A tuple of two integers (minutes, seconds) representing the elapsed time.
        """

        if self.is_paused:
            time = self.paused_time
        else:
            time = pygame.time.get_ticks() - self.start_time

        time = time // 1000
        minutes = time // 60
        seconds = time % 60
        return minutes, seconds
    
    def pause(self):
        """
        Pauses the timer by saving the current time and setting the is_paused flag to True.
        """
        if not self.is_paused:
            self.paused_time = pygame.time.get_ticks() - self.start_time
            self.is_paused = True

    def resume(self):
        """
        Resumes the timer by updating the start time based on the time when the timer was paused.
        """
        if self.is_paused:
            self.start_time = pygame.time.get_ticks() - self.paused_time
            self.is_paused = False

    def reset(self):
        """
        Resets the timer by setting the start time to the current time and clearing the paused time.
        """
        self.start_time = pygame.time.get_ticks()
        self.paused_time = 0
        self.is_paused = False