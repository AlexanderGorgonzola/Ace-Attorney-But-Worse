import pygame.font
import pygame
class Buttons:
    def __init__(self, at_game):
        self.screen = at_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = at_game.settings
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 45)
        self.prep_title()
        self.prep_startButton()
    def prep_title(self):
        self.title = pygame.image.load("images/title.png")
        self.title_rect = self.title.get_rect()
        self.title_rect.midtop = self.screen_rect.midtop

    def prep_startButton(self):
        self.font = pygame.font.SysFont(None, 200)
        self.button_rect = pygame.Rect(0, 0, 1200, 800)
        self.button_rect.center = self.screen_rect.center
        self.button_rect.bottom = self.screen_rect.bottom - 100
        self.msg = self.font.render("Start", True, self.text_color, (255, 255, 0))
        self.msg_rect = self.msg.get_rect()
        self.msg_rect.midbottom = self.button_rect.midbottom

    def prep_objection(self):
        self.font = pygame.font.SysFont(None, 45)
        self.objection_image = self.font.render("Object", True, self.text_color, (255, 255, 0))
        self.objection_rect = self.objection_image.get_rect()
        self.objection_rect.bottomleft = self.screen_rect.bottomleft

    def prep_info(self):
        self.font = pygame.font.SysFont(None, 45)
        self.info_image = self.font.render("Info", True, self.text_color, (255, 255, 0))
        self.info_rect = self.info_image.get_rect()
        self.info_rect.left = self.screen_rect.left
        self.info_rect.bottom = self.screen_rect.bottom - 40

    def show_buttons(self):
        self.screen.blit(self.info_image, self.info_rect)
        self.screen.blit(self.objection_image, self.objection_rect)

    def show_intro(self):
        self.screen.fill((255, 255, 0), self.button_rect)
        self.screen.blit(self.msg, self.msg_rect)
        self.screen.blit(self.title, self.title_rect)