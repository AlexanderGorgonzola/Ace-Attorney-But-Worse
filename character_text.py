import pygame.font
import pygame
import textwrap
from characters import Character
class CharacterText:
    def __init__(self, at_game):
        self.settings = at_game.settings
        self.screen = at_game.screen
        self.screen_rect = self.screen.get_rect()
        self.character = Character(self)
        self.judge_lines = ["Court is now in Session.", "Is everyone ready?", "What do you mean by that?", "Interesting...",
                            "Who would have known?", "I pass the verdict: Guilty", "I pass the verdict: Not Guilty"]
        self.defense_lines = ["Yes your honor.", "I don't think you get it Edgeworth."]
        self.prosecutor_lines = ["Of course, your honor."]
        self.font = pygame.font.SysFont("lucidaconsole", 25)
        self.text_1 = "PLACEHOLDER :)"
        self.text_1_rect = "OTHER PLACEHOLDER :)"
        self.text_2 = "PLACEHOLDER :)"
        self.text_2_rect = "OTHER PLACEHOLDER :)"
        self.text_color = (0,0,0)
    def prep_speech(self, turn, moves):
        if turn == "judge":
            if moves == "Start":
                self.text_1 = self.font.render(self.judge_lines[0], True, self.text_color)
                self.text_2 = self.font.render(self.judge_lines[1], True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.right = self.screen_rect.right - 240
                self.text_1_rect.bottom = self.screen_rect.bottom - 120
                self.text_2_rect.right = self.screen_rect.right - 330
            self.text_2_rect.bottom = self.screen_rect.bottom - 90
        elif turn == "defense":
            if moves == "Start_2":
                self.text_1 = self.font.render(self.defense_lines[0], True, self.text_color)
                self.text_2 = self.font.render("", True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.right = self.screen_rect.right - 370
            self.text_1_rect.bottom = self.screen_rect.bottom - 120
        elif turn == "prosecutor":
            if moves == "Start_3":
                self.text_1 = self.font.render(self.prosecutor_lines[0], True, self.text_color)
                self.text_2 = self.font.render("", True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.left = self.screen_rect.left + 310
            self.text_1_rect.bottom = self.screen_rect.bottom - 110
    def draw_speech(self):
        self.screen.blit(self.text_1, self.text_1_rect)
        self.screen.blit(self.text_2, self.text_2_rect)