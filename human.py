from player import Player

class Human(Player):
    def __init__(self):
        super().__init__(input('Enter Name: '))

    def choose_gesture(self):
        print("Choose 0 for rock, 1 for paper, 2 for scissors, 3 for lizard, 4 for Spock")
        self.chosen_gesture = self.gestures[0:4]
        user_input = (input(f'{self.name} choose your gesture: '))
        
        if user_input == '0':
            print(f'{self.name} chose rock!')
            self.chosen_gesture = self.gestures[0]
        
        elif user_input == '1':
            print(f'{self.name} chose paper!')
            self.chosen_gesture = self.gestures[1]

        elif user_input == '2':
            print(f'{self.name} chose scissors')
            self.chosen_gesture = self.gestures[2]

        elif user_input == '3':
            print (f'{self.name} chose lizard!')
            self.chosen_gesture = self.gestures[3]

        elif user_input == '4':
            print (f'{self.name} chose spock!')
            self.chosen_gesture = self.gestures[4]

        else:
            print('not a valid option try again')
