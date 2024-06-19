import random
from pygame import mixer
import pygame
class Music:
    def __init__(self, at_game, hp):
        pygame.init()
        pygame.mixer.init()
        self.settings = at_game.settings
        self.track = (pygame.mixer.Sound("sounds/main.mp3")).get_length()
        pygame.mixer.music.load("sounds/main.mp3")
        self.update_audio(hp)
    def update_audio(self, hp):
        self.music_id = random.randint(1, 3)
        pygame.mixer.music.set_volume(0.7)
        if self.music_id == 1:
            pygame.mixer.music.load("sounds/main.mp3")
            self.track = (pygame.mixer.Sound("sounds/main.mp3")).get_length()
        elif self.music_id == 2:
            pygame.mixer.music.load("sounds/losing.mp3")
            self.track = (pygame.mixer.Sound("sounds/losing.mp3")).get_length()
        else:
            pygame.mixer.music.load("sounds/onto_something.mp3")
            self.track = (pygame.mixer.Sound("sounds/onto_something.mp3")).get_length()

    def play_audio(self, hp):
        self.update_audio(hp)
        pygame.mixer.music.play(-1)
