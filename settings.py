import pygame
class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.current_bg = "defendant"
        self.bg = pygame.image.load("images/judge_bg.png")
        self.health = 100
        self.turn_des = "Start"
    def update_bg(self, Lost):
        if self.current_bg == "judge":
            self.bg = pygame.image.load("images/judge_bg.png")
        elif self.current_bg == "witness":
            self.bg = pygame.image.load("images/witness_bg.png")
        elif self.current_bg == "prosecutor":
            self.bg = pygame.image.load("images/prosecutor_bg.png")
        elif self.current_bg == "defense":
            self.bg = pygame.image.load("images/defense_bg.png")
        elif self.current_bg == "detective":
            self.bg = pygame.image.load("images/detective_bg.png")
        elif self.current_bg == "defendant":
            self.bg = pygame.image.load("images/victim_bg.png")
        if Lost:
            self.bg = pygame.image.load("images/judge_bg.png")