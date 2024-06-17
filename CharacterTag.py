import pygame.font
class CharacterTag:
    def __init__(self, at_game, msg):
        self.screen = at_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 100, 25
        self.box_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 50)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.left = self.screen_rect.left
        self._prep_msg(msg)
    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.box_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.left = self.rect.left
    def _prep_textbox(self, turn):
        if turn == "defense":
            self.textbox_image = pygame.image.load("images/player_Textbox.png")
        elif turn == "prosecutor":
            self.textbox_image = pygame.image.load("images/enemy_Textbox.png")
        elif turn == "detective":
            self.textbox_image = pygame.image.load("images/detective_Textbox.png")
        elif turn == "victim":
            self.textbox_image = pygame.image.load("images/victim_Textbox.png")
        elif turn == "witness":
            self.textbox_image = pygame.image.load("images/witness_Textbox.png")
        self.textbox_image_rect = self.textbox_image.get_rect()
        self.textbox_image_rect.right = self.screen_rect.right
        self.textbox_image_rect.bottom = self.screen_rect.bottom
    def draw_text(self):
        self.screen.fill(self.box_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.blit(self.textbox_image, self.textbox_image_rect)