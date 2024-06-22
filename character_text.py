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
        self.judge_lines = ["Court is now in Session.", "Is everyone ready?", "Edgeworth, please introduce the jury.", "Order!", "Anyways, Continue.",
                            "What do you mean by that?","Interesting...", "Who would have known?", "I pass the verdict: Guilty",
                            "I pass the verdict: Not Guilty"]
        
        self.defense_lines = ["Yes your honor.", "(Why did he come dressed like that?)","I don't think you get it Edgeworth.",
                              "Hold on a minute!", "This doesn't make any sense!", "The autopsy states she died", "10 minutes later!",
                              "Cyanide kills really quick,", "so it doesn't mean anything!"]

        self.prosecutor_lines = ["Of course, your honor.", "Understand. The victim is a young", "woman who won a large sum of money.",
                                 "Her husband, a clown, poisoned", "her lunch resulting in a quick dea-", "Now I call up the detective,", "Dick Gumshoe.",
                                 "Well, that doesn't mean anything,", "so please continue detective.", "Anyways, I would like to call on", "my first witness."]
        self.defendant_lines = ["Thats a lie! I'd never do that!"]
        self.detective_lines = ["The defendant was caught carrying", "cyanide in there pocket,", "Showing how he is indeed guilty.", "Well uhh...",
                                "Also, the defendant was in the same", "location during the victims death."]
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
                self.text_2_rect.right = self.screen_rect.right - 330
            elif moves == "Start_4":
                self.text_1 = self.font.render(self.judge_lines[2], True, self.text_color)
                self.text_2 = self.font.render("", True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.right = self.screen_rect.right - 60
                self.text_2_rect.right = self.screen_rect.right - 330
            elif moves == "Explain_interference_2":
                self.text_1 = self.font.render(self.judge_lines[3], True, self.text_color)
                self.text_2 = self.font.render(self.judge_lines[4], True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.right = self.screen_rect.right - 510
                self.text_2_rect.right = self.screen_rect.right - 330
            self.text_2_rect.bottom = self.screen_rect.bottom - 90
            self.text_1_rect.bottom = self.screen_rect.bottom - 120
        elif turn == "defendant":
            if moves == "Explain_interference":
                self.text_1 = self.font.render(self.defendant_lines[0], True, self.text_color)
                self.text_2 = self.font.render("", True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.right = self.screen_rect.right - 150
                self.text_2_rect.right = self.screen_rect.right - 330
            self.text_2_rect.bottom = self.screen_rect.bottom - 90
            self.text_1_rect.bottom = self.screen_rect.bottom - 120
        elif turn == "defense":
            if moves == "Start_2":
                self.text_1 = self.font.render(self.defense_lines[0], True, self.text_color)
                self.text_2 = self.font.render("", True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.right = self.screen_rect.right - 370
            elif moves == "Explain_interference_3":
                self.text_1 = self.font.render(self.defense_lines[1], True, self.text_color)
                self.text_2 = self.font.render("", True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.right = self.screen_rect.right - 80
            elif moves == "Object_detective":
                self.text_1 = self.font.render(self.defense_lines[3], True, self.text_color)
                self.text_2 = self.font.render(self.defense_lines[4], True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.right = self.screen_rect.right - 360
                self.text_2_rect.right = self.screen_rect.right - 195
            elif moves == "Object_detective_2":
                self.text_1 = self.font.render(self.defense_lines[5], True, self.text_color)
                self.text_2 = self.font.render(self.defense_lines[6], True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.right = self.screen_rect.right - 200
                self.text_2_rect.right = self.screen_rect.right - 340
            elif moves == "Object_detective_3":
                self.text_1 = self.font.render(self.defense_lines[7], True, self.text_color)
                self.text_2 = self.font.render(self.defense_lines[8], True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.right = self.screen_rect.right - 200
                self.text_2_rect.right = self.screen_rect.right - 170
            self.text_1_rect.bottom = self.screen_rect.bottom - 120
            self.text_2_rect.bottom = self.screen_rect.bottom - 90
        elif turn == "prosecutor":
            if moves == "Start_3":
                self.text_1 = self.font.render(self.prosecutor_lines[0], True, self.text_color)
                self.text_2 = self.font.render("", True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.left = self.screen_rect.left + 310
            elif moves == "Explain":
                self.text_1 = self.font.render(self.prosecutor_lines[1], True, self.text_color)
                self.text_2 = self.font.render(self.prosecutor_lines[2], True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.left = self.screen_rect.left + 310
                self.text_2_rect.left = self.screen_rect.left + 310
            elif moves == "Explain_2":
                self.text_1 = self.font.render(self.prosecutor_lines[3], True, self.text_color)
                self.text_2 = self.font.render(self.prosecutor_lines[4], True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.left = self.screen_rect.left + 310
                self.text_2_rect.left = self.screen_rect.left + 310
            elif moves == "Explain_3":
                self.text_1 = self.font.render(self.prosecutor_lines[5], True, self.text_color)
                self.text_2 = self.font.render(self.prosecutor_lines[6], True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.left = self.screen_rect.left + 310
                self.text_2_rect.left = self.screen_rect.left + 310
            elif moves == "Object_detective_5":
                self.text_1 = self.font.render(self.prosecutor_lines[7], True, self.text_color)
                self.text_2 = self.font.render(self.prosecutor_lines[8], True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.left = self.screen_rect.left + 310
                self.text_2_rect.left = self.screen_rect.left + 310
            elif moves == "Witness_one":
                self.text_1 = self.font.render(self.prosecutor_lines[9], True, self.text_color)
                self.text_2 = self.font.render(self.prosecutor_lines[10], True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.left = self.screen_rect.left + 315
                self.text_2_rect.left = self.screen_rect.left + 310
            self.text_1_rect.bottom = self.screen_rect.bottom - 110
            self.text_2_rect.bottom = self.screen_rect.bottom - 85
        elif turn == "detective":
            if moves == "Explain_4":
                self.text_1 = self.font.render(self.detective_lines[0], True, self.text_color)
                self.text_2 = self.font.render(self.detective_lines[1], True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.right = self.screen_rect.right - 120
                self.text_2_rect.right = self.screen_rect.right - 250
            elif moves == "Explain_5":
                self.text_1 = self.font.render(self.detective_lines[2], True, self.text_color)
                self.text_2 = self.font.render("", True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.right = self.screen_rect.right - 110
            elif moves == "Object_detective_4":
                self.text_1 = self.font.render(self.detective_lines[3], True, self.text_color)
                self.text_2 = self.font.render("", True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.right = self.screen_rect.right - 430
            elif moves == "Explain_6":
                self.text_1 = self.font.render(self.detective_lines[4], True, self.text_color)
                self.text_2 = self.font.render(self.detective_lines[5], True, self.text_color)
                self.text_1_rect = self.text_1.get_rect()
                self.text_2_rect = self.text_2.get_rect()
                self.text_1_rect.right = self.screen_rect.right - 90
                self.text_2_rect.right = self.screen_rect.right - 100
            self.text_1_rect.bottom = self.screen_rect.bottom - 110
            self.text_2_rect.bottom = self.screen_rect.bottom - 80
    def draw_speech(self):
        self.screen.blit(self.text_1, self.text_1_rect)
        self.screen.blit(self.text_2, self.text_2_rect)