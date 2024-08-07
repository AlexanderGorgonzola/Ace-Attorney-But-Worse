import random
import time
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
        self.info_up = False
        self.objection = False
        self.objection_cooldown = 0
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.character = Character(self)
        self.tag = CharacterTag(self, "Defense", self.objection_cooldown)
        self.buttons = Buttons(self)
        self.stats = GameStats(self)
        self.music = Music(self, self.settings.health)
        self.total_time = pygame.time.get_ticks()
        self.effects = Effects(self, self.stats.ranking)
        self.character_text = CharacterText(self)
        pygame.display.set_caption("Ace Attorney")
        self.page_flip = pygame.mixer.Sound("sounds/page_flip_sound.mp3")
        self.objection_sound = pygame.mixer.Sound("sounds/player_objection_sound.mp3")
        self.hold_it_sound = pygame.mixer.Sound("sounds/player_holdit_sound.mp3")

    def _update_screen(self):
        if self.stats.game_active and not self.stats.game_over:
            if self.character.turn == "witness 2": #yippie, A MESS!
                self.settings.current_bg = "witness"
            else:
                self.settings.current_bg = self.character.turn
            self.settings.update_bg(self.stats.game_over)
            if (self.settings.current_bg == "judge") or (self.settings.current_bg == "prosecutor") or (self.settings.current_bg == "defense"): #decide locations
                self.screen.blit(self.settings.bg, (-120, 0))
            elif (self.settings.current_bg == "witness") or (self.settings.current_bg == "detective") or (self.settings.current_bg == "defendant"):
                self.screen.blit(self.settings.bg, (0, 0))
            self.character.change_image()
            self.character.blitme()
            self.tag = CharacterTag(self, self.character.turn, self.objection_cooldown)
            self.tag._prep_msg(self.character.turn)
            self.tag._prep_textbox(self.character.turn)
            self.tag.prep_cooldown(self.objection_cooldown)
            self.tag.draw_text()
            self.buttons.prep_objection()
            self.buttons.prep_info()
            self.buttons.prep_give_up() #nah what the sigma is this code
            self.buttons.prep_health(self.settings.health)
            self.buttons.show_buttons()
            self.character_text.prep_speech(self.character.turn, self.settings.turn_des)
            self.character_text.draw_speech()
            self.tag.prep_cooldown(self.objection_cooldown)
            if self.info_up == True:
                self.effects.show_autopsy()
            if self.settings.health <= 0:
                self.stats.game_over = True
        elif not self.stats.game_active and not self.stats.game_over:
            self.buttons.prep_startButton()
            self.buttons.prep_title()
            self.buttons.show_intro()
        elif self.stats.game_active and self.stats.game_over:
            self.settings.update_bg(self.stats.game_over)
            self.screen.blit(self.settings.bg, (-120, 0))
            self.effects.prep_final_stats(self.stats.ranking)
            self.effects.show_final_stats()
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
                    self.objection_cooldown -= 1
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
        elif self.settings.turn_des == "Object_detective":
            self.character.turn = "defense"
            self.character.defense = "object"
            self.settings.turn_des = "Object_detective_2"
        elif self.settings.turn_des == "Object_detective_2":
            self.character.turn = "defense"
            self.character.defense = "think"
            self.settings.turn_des = "Object_detective_3"
        elif self.settings.turn_des == "Object_detective_3":
            self.character.turn = "detective"
            self.character.detective = "confused"
            self.settings.turn_des = "Object_detective_4"
        elif self.settings.turn_des == "Object_detective_4":
            self.character.turn = "prosecutor"
            self.character.prosecutor = "happy"
            self.settings.turn_des = "Object_detective_5"
        elif self.settings.turn_des == "Explain_5":
            self.settings.health -= 20
            self.character.turn = "detective"
            self.character.detective = "normal"
            self.settings.turn_des = "Explain_6"
        elif self.settings.turn_des == "Object_detective_5":
            self.character.turn = "detective"
            self.character.detective = "normal"
            self.settings.turn_des = "Explain_6"
        elif self.settings.turn_des == "Explain_6":
            self.character.turn = "prosecutor"
            self.character.prosecutor = "think"
            self.settings.turn_des = "Witness_one"
        elif self.settings.turn_des == "Witness_one":
            self.character.turn = "witness"
            self.character.witness = "normal"
            self.settings.turn_des = "Witness_one_2"
        elif self.settings.turn_des == "Witness_one_2":
            self.character.turn = "prosecutor"
            self.character.prosecutor = "normal"
            self.settings.turn_des = "Witness_one_3"
        elif self.settings.turn_des == "Witness_one_3":
            self.character.turn = "witness"
            self.character.witness = "normal"
            self.settings.turn_des = "Witness_one_4"
        elif self.settings.turn_des == "Witness_one_4":
            self.character.turn = "witness"
            self.character.witness = "upset"
            self.settings.turn_des = "Witness_one_5"
        elif self.settings.turn_des == "Witness_one_5":
            self.character.turn = "witness"
            self.character.witness = "normal"
            self.settings.turn_des = "Witness_one_6"
        elif self.settings.turn_des == "Witness_one_6" and not self.objection:
            self.character.turn = "prosecutor"
            self.character.prosecutor = "happy"
            self.settings.turn_des = "Witness_one_7"
        elif self.settings.turn_des == "Witness_one_7" and not self.objection:
            self.character.turn = "judge"
            self.settings.turn_des = "Witness_one_8"
        elif self.settings.turn_des == "Witness_one_8":
            self.stats.ranking = 0
            self.stats.game_over = True
        elif self.settings.turn_des == "Cross_witness_one":
            self.character.turn = "defense"
            self.character.defense = "normal"
            self.settings.turn_des = "Cross_witness_one_2"
        elif self.settings.turn_des == "Cross_witness_one_2":
            self.character.turn = "witness"
            self.character.witness = "nervous"
            self.settings.turn_des = "Cross_witness_one_3"
        elif self.settings.turn_des == "Cross_witness_one_3":
            self.character.turn = "defense"
            self.character.defense = "object"
            self.settings.turn_des = "Cross_witness_one_4"
        elif self.settings.turn_des == "Cross_witness_one_4":
            self.character.turn = "prosecutor"
            self.character.prosecutor = "object"
            self.settings.turn_des = "Cross_witness_one_5"
        print(self.settings.turn_des)

    def _check_play_button(self, mouse_pos):
        intro_button_clicked = self.buttons.button_rect.collidepoint(mouse_pos)
        if intro_button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True
            self.music.play_audio(self.settings.health)
    def objection_effect(self):
        self.effects.prep_objection()
        self.objection = True
        self.effects.show_objection(self.objection)
        r = random.randint(1,2)
        if r == 1:
            self.objection_sound.play()
        else:
            self.hold_it_sound.play()
        self.objection = False
        self.effects.show_objection(self.objection)
        self.objection_cooldown = 3
    def _check_normal_buttons(self, mouse_pos):
        info_button_clicked = self.buttons.info_rect.collidepoint(mouse_pos)
        objection_button_clicked = self.buttons.objection_rect.collidepoint(mouse_pos)
        give_in_button_clicked = self.buttons.give_image_rect.collidepoint(mouse_pos)
        if info_button_clicked and not self.info_up:
            self.effects.prep_autopsy()
            self.info_up = True
            self.page_flip.play()
        elif info_button_clicked and self.info_up:
            self.effects.hide_autopsy()
            self.info_up = False
            self.page_flip.play()
        elif give_in_button_clicked:
            self.stats.ranking = 0
            self.stats.game_over = True
        elif objection_button_clicked and self.objection_cooldown <= 0:
            if self.settings.turn_des == "Explain_4" or self.settings.turn_des == "Explain_5":
                self.settings.turn_des = "Object_detective"
                self.character.turn = "defense"
                self.character.defense = "object"
                self.objection_effect()
                self.settings.health += 10
                self.stats.ranking += 1
            elif self.settings.turn_des == "Witness_one_7" or self.settings.turn_des == "Witness_one_8":
                self.settings.turn_des = "Cross_witness_one"
                self.character.turn = "defense"
                self.character.defense = "object"
                self.objection_effect()
                self.stats.ranking += 1
            else: #penalty sucker
                self.objection_effect()
                self.settings.health -= 20
                self.stats.ranking -= 1
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

if __name__ == "__main__":
    at = AceAttorney()
    at.run_game()