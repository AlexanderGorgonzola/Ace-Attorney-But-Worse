class GameStats:
    def __init__(self, at_game):
        self.settings = at_game.settings
        self.game_active = False
        self.reset_stats()
    def reset_stats(self):
        self.game_active = False