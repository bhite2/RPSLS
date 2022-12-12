from player import Player
import random


class AI(Player): 
    def __init__(self):
        super().__init__(random.choice(['Bender', 'R2-D2', 'Johnny 5', 'VIKI', 'Data']))

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gestures)
        print(f'{self.name} chose {self.chosen_gesture}')
        return self.chosen_gesture