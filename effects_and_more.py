import pygame

class Effects:
    def __init__(self, at_game):
        self.settings = at_game.settings
        self.screen = at_game.screen
        self.screen_rect = self.screen.get_rect()
        self.prep_autopsy()
    def prep_autopsy(self):
        self.autopsy = pygame.image.load("images/Autopsy_Report.png")
        self.autopsy_rect = self.autopsy.get_rect()
        self.autopsy_rect.center = self.screen_rect.center
    def show_autopsy(self):
        self.screen.blit(self.autopsy, self.autopsy_rect)
    def hide_autopsy(self):
        self.autopsy_rect.bottom = self.screen_rect.bottom + 1000
        self.screen.blit(self.autopsy, self.autopsy_rect)