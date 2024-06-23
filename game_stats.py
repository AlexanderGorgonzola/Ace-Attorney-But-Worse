class GameStats:
    def __init__(self, at_game):
        self.settings = at_game.settings
        self.game_active = False
        self.game_over = False
        self.max_health = 100
        self.reset_stats()
    def reset_stats(self):
        self.game_active = False
        self.game_over = False