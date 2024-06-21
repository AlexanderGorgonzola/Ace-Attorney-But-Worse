import pygame
import sys
from pygame import mixer
from settings import Settings
from characters import Character
from CharacterTag import CharacterTag
from buttons import Buttons
from game_stats import GameStats
from music_player import Music
from effects_and_more import Effects
from character_text import CharacterText
class AceAttorney:
    def __init__(self):
        pygame.init()
        mixer.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.character = Character(self)
        self.tag = CharacterTag(self, "Defense")
        self.buttons = Buttons(self)
        self.stats = GameStats(self)
        self.music = Music(self, self.settings.health)
        self.total_time = pygame.time.get_ticks()
        self.effects = Effects(self)
        self.character_text = CharacterText(self)
        pygame.display.set_caption("Ace Attorney")
        self.info_up = False
        self.objection = False
        self.page_flip = pygame.mixer.Sound("sounds/page_flip_sound.mp3")

    def _update_screen(self):
        if self.stats.game_active:
            if self.character.turn == "witness 2": #yippie, A MESS!
                self.settings.current_bg = "witness"
            else:
                self.settings.current_bg = self.character.turn
            self.settings.update_bg()
            if (self.settings.current_bg == "judge") or (self.settings.current_bg == "prosecutor") or (self.settings.current_bg == "defense"): #decide locations
                self.screen.blit(self.settings.bg, (-120, 0))
            elif (self.settings.current_bg == "witness") or (self.settings.current_bg == "detective") or (self.settings.current_bg == "defendant"):
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
            self.character_text.prep_speech(self.character.turn, self.settings.turn_des)
            self.character_text.draw_speech()
            if self.info_up == True:
                self.effects.show_autopsy()
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
                pygame.display.flip()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #basically gameplay?
                    self.check_space()
    def check_space(self):
        if self.settings.turn_des == "Start":
            self.character.turn = "defense"
            self.character.defense = "normal"
            self.settings.turn_des = "Start_2"
        elif self.settings.turn_des == "Start_2":
            self.character.turn = "prosecutor"
            self.character.prosecutor = "normal"
            self.settings.turn_des = "Start_3"
        elif self.settings.turn_des == "Start_3":
            self.character.turn = "judge"
            self.settings.turn_des = "Start_4"
        elif self.settings.turn_des == "Start_4":
            self.character.turn = "prosecutor"
            self.character.prosecutor = "happy"
            self.settings.turn_des = "Explain"
        elif self.settings.turn_des == "Explain":
            self.character.turn = "prosecutor"
            self.settings.turn_des = "Explain_2"
        elif self.settings.turn_des == "Explain_2":
            self.character.turn = "defendant"
            self.character.defendant = "shocked"
            self.settings.turn_des = "Explain_interference"
        elif self.settings.turn_des == "Explain_interference":
            self.character.turn = "judge"
            self.settings.turn_des = "Explain_interference_2"
        elif self.settings.turn_des == "Explain_interference_2":
            self.character.turn = "defense"
            self.character.defense = "stressed"
            self.settings.turn_des = "Explain_interference_3"
        elif self.settings.turn_des == "Explain_interference_3":
            self.character.turn = "prosecutor"
            self.character.prosecutor = "happy"
            self.settings.turn_des = "Explain_3"
        elif self.settings.turn_des == "Explain_3" and not self.objection:
            self.character.turn = "detective"
            self.character.detective = "normal"
            self.settings.turn_des = "Explain_4"
        elif self.settings.turn_des == "Explain_4" and not self.objection:
            self.character.turn = "detective"
            self.character.detective = "normal"
            self.settings.turn_des = "Explain_5"

    def _check_play_button(self, mouse_pos):
        intro_button_clicked = self.buttons.button_rect.collidepoint(mouse_pos)
        if intro_button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True
            self.music.play_audio(self.settings.health)

    def _check_normal_buttons(self, mouse_pos):
        info_button_clicked = self.buttons.info_rect.collidepoint(mouse_pos)
        objection_button_clicked = self.buttons.info_rect.collidepoint(mouse_pos)
        if info_button_clicked and not self.info_up:
            self.effects.prep_autopsy()
            self.info_up = True
            self.page_flip.play()
        elif info_button_clicked and self.info_up:
            self.effects.hide_autopsy()
            self.info_up = False
            self.page_flip.play()
        #elif objection_button_clicked:
            #if self.settings.turn_des == "detective_2"
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

if __name__ == "__main__":
    at = AceAttorney()
    at.run_game()