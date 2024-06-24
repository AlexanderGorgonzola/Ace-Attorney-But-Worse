import pygame
import pygame.font
class Effects:
    def __init__(self, at_game, result):
        self.settings = at_game.settings
        self.screen = at_game.screen
        self.screen_rect = self.screen.get_rect()
        self.prep_autopsy()
        self.prep_objection()
        self.prep_final_stats(result)
    def prep_autopsy(self):
        self.autopsy = pygame.image.load("images/Autopsy_Report.png")
        self.autopsy_rect = self.autopsy.get_rect()
        self.autopsy_rect.center = self.screen_rect.center
    def show_autopsy(self):
        self.screen.blit(self.autopsy, self.autopsy_rect)
    def hide_autopsy(self):
        self.screen.blit(self.autopsy, self.autopsy_rect)
    def prep_objection(self):
        self.objection_image = pygame.image.load("images/Objection!.png")
        self.objection_image_rect = self.objection_image.get_rect()
        self.objection_image_rect.center = self.screen_rect.center
    def prep_final_stats(self, result):
        self.font = pygame.font.SysFont(None, 200)
        self.stats_title = self.font.render("RANKING:", True, (0,0,0))
        self.stats_result = "PLACEHOLDER"
        if result >= 9:
            self.stats_result = self.font.render("A+", True, (255,0,0))
        elif result == 8:
            self.stats_result = self.font.render("B", True, (200,0,0))
        elif result == 7:
            self.stats_result = self.font.render("C", True, (155,0,0))
        elif result == 6:
            self.stats_result = self.font.render("D", True, (100,0,0))
        else:
            self.stats_result = self.font.render("F", True, (50,0,0))
        self.stats_title_rect = self.stats_title.get_rect()
        self.stats_result_rect = self.stats_result.get_rect()
        self.stats_title_rect.midtop = self.screen_rect.midtop
        self.stats_result_rect.center = self.screen_rect.center
    def show_objection(self, object):
        if object:
            self.screen.blit(self.objection_image, self.objection_image_rect)
        else:
            self.objection_image_rect.bottom = self.screen_rect.bottom + 1000
            self.screen.blit(self.objection_image, self.objection_image_rect)
    def show_final_stats(self):
        self.screen.blit(self.stats_result, self.stats_result_rect)
        self.screen.blit(self.stats_title, self.stats_title_rect)