from player import Player

class AI(Player): 
    def __init__(self):
        super().__init__(random.choice(['Bender', 'R2-D2', 'Johnny 5', 'VIKI', 'Data']))
