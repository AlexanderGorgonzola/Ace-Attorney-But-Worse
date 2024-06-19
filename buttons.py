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
        self.prep_info()
        self.prep_give_up()
        self.prep_objection()
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
        self.objection_image = pygame.image.load("images/object_button.png")
        self.objection_rect = self.objection_image.get_rect()
        self.objection_rect.bottomleft = self.screen_rect.bottomleft

    def prep_info(self):
        self.info_image = pygame.image.load("images/info_button.png")
        self.info_rect = self.info_image.get_rect()
        self.info_rect.left = self.screen_rect.left
        self.info_rect.bottom = self.screen_rect.bottom - 70
    def prep_give_up(self):
        self.give_image = pygame.image.load("images/give_up_button.png")
        self.give_image_rect = self.give_image.get_rect()
        self.give_image_rect.left = self.screen_rect.left + 160
        self.give_image_rect.bottom = self.screen_rect.bottom - 35
    def prep_health(self, hp):
        self.font = pygame.font.SysFont("Comic Sans MS", 35)
        self.health_rect = pygame.Rect(0, 0, (hp * 2), 50)
        self.health_msg = self.font.render("Health:", True, self.text_color, None)
        self.health_msg_rect = self.health_msg.get_rect()
        self.health_msg_rect.top = self.screen_rect.top + 40
        self.health_msg_rect.left = self.screen_rect.left
        self.health_rect.top = self.screen_rect.top + 100
        self.health_rect.left = self.screen_rect.left

    def show_buttons(self):
        self.screen.blit(self.info_image, self.info_rect)
        self.screen.blit(self.objection_image, self.objection_rect)
        self.screen.blit(self.give_image, self.give_image_rect)
        self.screen.fill((0, 255, 0), self.health_rect)
        self.screen.blit(self.health_msg, self.health_msg_rect)
    def show_intro(self):
        self.screen.fill((255, 255, 0), self.button_rect)
        self.screen.blit(self.msg, self.msg_rect)
        self.screen.blit(self.title, self.title_rect)