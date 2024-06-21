import pygame

class Character:
    def __init__(self, at_game):
        self.screen = at_game.screen
        self.screen_rect = at_game.screen.get_rect()
        self.turn = "judge"
        self.defense = "object"
        self.prosecutor = "normal"
        self.witness = "angry"
        self.detective = "confused"
        self.defendant = "normal"
        self.witness_2 = "normal"
    def change_image(self):
        if self.turn == "defense":
            if self.defense == "normal":
                self.image = pygame.image.load("images/player_talk.png")
            elif self.defense == "think":
                self.image = pygame.image.load("images/player_think.png")
            elif self.defense == "stressed":
                self.image = pygame.image.load("images/player_stressed.png")
            elif self.defense == "object":
                self.image = pygame.image.load("images/player_objection.png")
        elif self.turn == "prosecutor":
            if self.prosecutor == "normal":
                self.image = pygame.image.load("images/enemy_stand.png")
            elif self.prosecutor == "think":
                self.image = pygame.image.load("images/enemy_think.png")
            elif self.prosecutor == "stressed":
                self.image = pygame.image.load("images/enemy_stress.png")
            elif self.prosecutor == "object":
                self.image = pygame.image.load("images/enemy_objection.png")
            elif self.prosecutor == "happy":
                self.image = pygame.image.load("images/enemy_talk.png")
        elif self.turn == "judge":
            self.image = pygame.image.load("images/judge.png")
        elif self.turn == "witness":
            if self.witness == "normal":
                self.image = pygame.image.load("images/witness_talk.png")
            elif self.witness == "nervous":
                self.image = pygame.image.load("images/witness_talk2.png")
            elif self.witness == "angry":
                self.image = pygame.image.load("images/witness_angry.png")
            elif self.witness == "upset":
                self.image = pygame.image.load("images/witness_upset.png")
        elif self.turn == "detective":
            if self.detective == "normal":
                self.image = pygame.image.load("images/detective_talk.png")
            elif self.detective == "confused":
                self.image = pygame.image.load("images/detective_confused.png")
        elif self.turn == "defendant":
            if self.defendant == "normal":
                self.image = pygame.image.load("images/victim_talk.png")
            elif self.defendant == "shocked":
                self.image = pygame.image.load("images/victim_shocked.png")
            elif self.defendant == "angry":
                self.image = pygame.image.load("images/victim_angry.png")
            elif self.defendant == "sad":
                self.image = pygame.image.load("images/victim_sad.png")
        elif self.turn == "witness 2":
            if self.witness_2 == "normal":
                self.image = pygame.image.load("images/witness2_talk.png")
            elif self.witness_2 == "nervous":
                self.image = pygame.image.load("images/witness2_talk2.png")
            elif self.witness_2 == "angry":
                self.image = pygame.image.load("images/witness2_caught.png")
            elif self.witness_2 == "upset":
                self.image = pygame.image.load("images/witness2_upset.png")
        self.rect = self.image.get_rect()
        if self.turn == "judge":
            self.rect.center = self.screen_rect.center
            self.rect.top = self.screen_rect.top - 10
        elif self.turn == "witness" or self.turn == "witness 2":
            self.rect.right = self.screen_rect.right - 90
            self.rect.bottom = self.screen_rect.bottom
        elif self.turn == "defense":
            self.rect.right = self.screen_rect.right - 50
            self.rect.bottom = self.screen_rect.bottom
        else:
            self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)