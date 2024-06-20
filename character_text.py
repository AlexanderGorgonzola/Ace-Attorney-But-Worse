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
        self.judge_lines = ["Court is now in Session", "What do you mean by that?", "Interesting...",
                            "Who would have known?", "I pass the verdict: Guilty", "I pass the verdict: Not Guilty"]
        self.font = pygame.font.SysFont("monospace", 30)
        self.text = "PLACEHOLDER :)"
        self.text_rect = "OTHER PLACEHOLDER :)"
    def prep_speech(self, turn, moves):
        if turn == "judge":
            if moves == "Start":
                wrapped_text = textwrap.fill(self.judge_lines[0], width=500)

        self.text = self.font.render(wrapped_text, True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.midbottom = self.screen_rect.midbottom
    def draw_speech(self):
        self.screen.blit(self.text, self.text_rect)