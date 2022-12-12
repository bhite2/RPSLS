import random

class Player():
    def __init__(self, name):
        self.name = name
        self.gestures = ['rock', 'paper', 'scissors', 'lizard', 'Spock']
        self.player_score = 0