import pygame

class Character:
    def __init__(self, at_game):
        self.screen = at_game.screen
        self.screen_rect = at_game.screen.get_rect()
        self.turn = "witness"
        self.defense = "normal"
        self.prosecutor = "normal"
        self.witness = "normal"
        self.detective = "confused"
        self.victim = "normal"
    def change_image(self):
        if self.turn == "defense":
            if self.defense == "normal":
                self.image = pygame.image.load("images/player_talk.png")
            elif self.defense == "think":
                self.image = pygame.image.load("images/player_think.png")
            elif self.defense == "stressed":
                self.image = pygame.image.load("images/player_stressed.png")
        elif self.turn == "prosecutor":
            if self.prosecutor == "normal":
                self.image = pygame.image.load("images/enemy_stand.png")
            elif self.prosecutor == "think":
                self.image = pygame.image.load("images/enemy_think.png")
            elif self.prosecutor == "stressed":
                self.image = pygame.image.load("images/enemy_stress.png")
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
        elif self.turn == "victim":
            if self.victim == "normal":
                self.image = pygame.image.load("images/victim_talk.png")
            elif self.victim == "shocked":
                self.image = pygame.image.load("images/victim_shocked.png")
            elif self.victim == "angry":
                self.image = pygame.image.load("images/victim_angry.png")
            elif self.victim == "sad":
                self.image = pygame.image.load("images/victim_sad.png")

        self.rect = self.image.get_rect()
        if self.turn == "judge":
            self.rect.midtop = self.screen_rect.midtop
        else:
            self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)