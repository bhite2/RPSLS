class Player():
    def __init__(self, name):
        self.name = name
        self.gesture = ()
        self.player_score = 0

class Human(Player):
    def __init__(self):
        super().__init__()

class AI(Player):
    def __init__(self):
        super().__init__()
