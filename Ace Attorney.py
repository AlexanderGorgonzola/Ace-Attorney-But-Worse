import pygame
import sys
from settings import Settings
from characters import Character
from CharacterTag import CharacterTag
from buttons import Buttons
from game_stats import GameStats
from music_player import Music
from effects_and_more import Effects
class AceAttorney:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.character = Character(self)
        self.tag = CharacterTag(self, "Defense")
        self.buttons = Buttons(self)
        self.stats = GameStats(self)
        self.music = Music(self, self.settings.health)
        self.total_time = pygame.time.get_ticks()
        self.effects = Effects(self)
        pygame.display.set_caption("Ace Attorney")
        self.info_up = False

    def _update_screen(self):
        if self.stats.game_active:
            if self.character.turn == "witness_2": #yippie, A MESS!
                self.settings.current_bg = "witness"
            else:
                self.settings.current_bg = self.character.turn
            self.settings.update_bg()
            if (self.settings.current_bg == "judge") or (self.settings.current_bg == "prosecutor") or (self.settings.current_bg == "defense"): #decide locations
                self.screen.blit(self.settings.bg, (-120, 0))
            elif (self.settings.current_bg == "witness") or (self.settings.current_bg == "detective") or (self.settings.current_bg == "victim"):
                self.screen.blit(self.settings.bg, (0, 0))
            self.character.change_image()
            self.character.blitme()
            self.tag = CharacterTag(self, self.character.turn)
            self.tag._prep_msg(self.character.turn)
            self.tag._prep_textbox(self.character.turn)
            self.tag.draw_text()
            self.buttons.prep_objection()
            self.buttons.prep_info()
            self.buttons.prep_give_up() #nah what the sigma is this code
            self.buttons.prep_health(self.settings.health)
            self.buttons.show_buttons()
        else:
            self.buttons.prep_startButton()
            self.buttons.prep_title()
            self.buttons.show_intro()

        pygame.display.flip()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_normal_buttons(mouse_pos)
    def _check_play_button(self, mouse_pos):
        intro_button_clicked = self.buttons.button_rect.collidepoint(mouse_pos)
        if intro_button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True
            self.music.play_audio(self.settings.health)

    def _check_normal_buttons(self, mouse_pos):
        info_button_clicked = self.buttons.info_rect.collidepoint(mouse_pos)
        if info_button_clicked and not self.info_up:
            self.effects.prep_autopsy()
            self.effects.show_autopsy()
            print("Whats up")
            self.info_up = True
        elif info_button_clicked and self.info_up:
            self.effects.hide_autopsy()
            print("whats down")
            self.info_up = False
    def run_game(self):
        while True:
            self._update_screen()
            self._check_events()

if __name__ == "__main__":
    at = AceAttorney()
    at.run_game()