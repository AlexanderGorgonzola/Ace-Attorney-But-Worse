import pygame.font
class CharacterTag:
    def __init__(self, at_game, msg, cooldown):
        self.screen = at_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 100, 25
        self.box_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 50)
        self._prep_msg(msg)
        self.prep_cooldown(cooldown)
    def _prep_msg(self, msg):
        self.msg_image = self.font.render("Turn: " + str(msg).title(), True, self.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.left = self.screen_rect.left
    def _prep_textbox(self, turn):
        if turn == "defense":
            self.textbox_image = pygame.image.load("images/player_Textbox.png")
        elif turn == "prosecutor":
            self.textbox_image = pygame.image.load("images/enemy_Textbox.png")
        elif turn == "detective":
            self.textbox_image = pygame.image.load("images/detective_Textbox.png")
        elif turn == "defendant":
            self.textbox_image = pygame.image.load("images/victim_Textbox.png")
        elif turn == "witness":
            self.textbox_image = pygame.image.load("images/witness_Textbox.png")
        elif turn == "witness 2":
            self.textbox_image = pygame.image.load("images/witness2_Textbox.png")
        elif turn == "judge":
            self.textbox_image = pygame.image.load("images/judge_Textbox.png")
        self.textbox_image_rect = self.textbox_image.get_rect()
        if turn == "prosecutor":
            self.textbox_image_rect.right = self.screen_rect.right
            self.textbox_image_rect.bottom = self.screen_rect.bottom + 50
        else:
            self.textbox_image_rect.right = self.screen_rect.right
            self.textbox_image_rect.bottom = self.screen_rect.bottom
    def prep_cooldown(self, cooldown):
        if cooldown <= 0:
            self.cooldown_image = self.font.render("Objection: READY!", True, self.text_color, None)
        else:
            self.cooldown_image = self.font.render("Objection: " + str(cooldown), True, self.text_color, None)
        self.cooldown_image_rect = self.cooldown_image.get_rect()
        self.cooldown_image_rect.midleft = self.screen_rect.midleft
        self.cooldown_image_rect.top = self.screen_rect.top + 150
    def draw_text(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.textbox_image, self.textbox_image_rect)
        self.screen.blit(self.cooldown_image, self.cooldown_image_rect)