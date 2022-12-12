from player import Player
from human import Human
from ai import AI
import time

class Game():

    def welcome(self):
        print('Welcome to ROCK, PAPER, SCISSORS, LIZARD, SPOCK!')
        time.sleep(3)
        print('Each player picks a gesture and reveals it at the same time. Player with the winning gesture wins the round.')
        time.sleep(3)
        print('If both players use the same gesture, that is a tie. The round will be replayed.')
        time.sleep(3)
        print('First player to get two wins is crowned the winner.')
        time.sleep(3)
        print('You can choose between Rock, Paper, Scissors, Lizard or Spock')
        time.sleep(3)
        print('Rock crushes Scissors')
        time.sleep(3)
        print('Scissors cuts Paper')
        time.sleep(3)
        print('Paper covers Rock')
        time.sleep(3)
        print('Rock crushes Lizard')
        time.sleep(3)
        print('Lizard poisons Spock')
        time.sleep(3)
        print('Spock smashes Scissors')
        time.sleep(3)
        print('Scissors decapitates Lizard')
        time.sleep(3)
        print('Lizard eats Paper')
        time.sleep(3)
        print('Paper disproves Spock')
        time.sleep(3)
        print('Spock vaporizes Rock')
        time.sleep(3)
        print('May the best player win!!!')
        time.sleep(3)
        

    def player_select(self):
        print('Enter 1 for Single Player. Enter 2 for Versus Mode')
        self.game_mode = input('')
        # if statement needs to go here for player selection
        if self.game_mode == '1':
            print('You have selected Single Player mode.')
            self.player_one = Human()
            self.player_two = AI()
            print(f'{self.player_one.name} vs. {self.player_two.name}')
            print('Get ready for battle...')
            time.sleep(5)

        elif self.game_mode == '2':
            print('You have selected Versus Mode')
            self.player_one = Human()
            self.player_two = Human()
            print(f'{self.player_one.name} vs. {self.player_two.name}')
            print('Get ready for battle...')
            time.sleep(5)

    def gesture_selection(self):
        while self.player_one.player_score < 2 and self.player_two.player_score < 2:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            self.compare_gesture()

        
        # Want player to pick own name. Does this need it's own function

    def compare_gesture(self):
        
        if self.player_one.chosen_gesture == 'rock':
            if self.player_two.chosen_gesture == 'rock':
                print('It is a tie.')
            
            elif self.player_two.chosen_gesture == 'paper':
                self.player_two.player_score += 1
                print(f'Paper covers rock, {self.player_two.name} wins!')
            
            elif self.player_two.chosen_gesture == 'scissors':
                self.player_one.player_score += 1
                print(f'Rock crushes scissors, {self.player_one.name} wins!')

            elif self.player_two.chosen_gesture == 'lizard':
                self.player_one.player_score += 1
                print(f'Rock crushes lizard, {self.player_one.name} wins!')
            
            elif self.player_two.chosen_gesture == 'spock':
                self.player_two.player_score +=1
                print(f'spock vaporizes rock {self.player_two.name} wins!')
         
        if self.player_one.chosen_gesture == 'paper':
            if self.player_two.chosen_gesture == 'rock':
                self.player_one.player_score += 1
                print(f'Paper covers rock {self.player_one.name} wins!')
            
            elif self.player_two.chosen_gesture == 'paper':
                print('Its a tie!') 

            elif self.player_two.chosen_gesture == 'scissors':
                self.player_two.player_score += 1
                print(f'Scissors cut paper, {self.player_two.name} wins!')

            elif self.player_two.chosen_gesture == 'lizard':
                self.player_two.player_score += 1
                print(f'Lizard eats paper, {self.player_two.name} wins!')
            
            elif self.player_two.chosen_gesture == 'spock':
                self.player_one.player_score += 1
                print(f'Paper disproves Spock, {self.player_one.name} wins!')
        
        # 3rd line
        if self.player_one.chosen_gesture == 'scissors':
            if self.player_two.chosen_gesture == 'rock':
                self.player_two.player_score += 1
                print(f'Rock crushes scissors, {self.player_two.name} wins!')
            
            elif self.player_two.chosen_gesture == 'scissors':
                print('Its a tie') 

            elif self.player_two.chosen_gesture == 'paper':
                self.player_one.player_score += 1
                print(f'Scissors cut paper {self.player_one.name} wins!')

            elif self.player_two.chosen_gesture == 'lizard':
                self.player_one.player_score += 1
                print(f'Scissors decapitates lizard, {self.player_one.name} wins!')
            
            elif self.player_two.chosen_gesture == 'spock':
                self.player_two.player_score += 1
                print(f'Spock smashes scissors, {self.player_two.name} wins!')
        
        # 4th line
        if self.player_one.chosen_gesture == 'lizard':
            if self.player_two.chosen_gesture == 'rock':
                self.player_two.player_score += 1
                print(f'Rock crushes lizard, {self.player_two.name} wins!')
            
            elif self.player_two.chosen_gesture == 'lizard':
                print('Its a tie') 

            elif self.player_two.chosen_gesture == 'scissors':
                self.player_two.player_score += 1
                print(f'Scissors decapitates lizard, {self.player_two.name} wins!')

            elif self.player_two.chosen_gesture == 'paper':
                self.player_one.player_score += 1
                print(f'Lizard eats paper {self.player_one.name} wins!')
            
            elif self.player_two.chosen_gesture == 'spock':
                self.player_one.player_score += 1
                print(f'lizard poisons spock {self.player_one.name} wins')
        
        # 5th line
        if self.player_one.chosen_gesture == 'Spock':
            if self.player_two.chosen_gesture == 'rock':
                self.player_one.player_score += 1
                print(f'Spock vaporizes rock, {self.player_one.name} wins!')
            
            elif self.player_two.chosen_gesture == 'Spock':
                print('Its a tie') 

            elif self.player_two.chosen_gesture == 'paper':
                self.player_two.player_score += 1
                print(f'Paper disproves Spock, {self.player_two.name} wins!')

            elif self.player_two.chosen_gesture == 'scissors':
                self.player_one.player_score += 1
                print(f'Spock smashes scissors, {self.player_one.name} wins!')
            
            elif self.player_two.chosen_gesture == 'lizard':
                self.player_two.player_score += 1
                print(f'Lizard poisons spock, {self.player_two.name} wins!')

        #If and elif statements for all possible outcomes
    def display_winner(self):
        if self.player_one.player_score == 2:
            print(f'{self.player_one.name} wins the game!')

        elif self.player_two.player_score == 2:
            print(f'{self.player_two.name} wins the game!')

    def run_game(self):
        self.welcome()
        self.player_select()
        self.gesture_selection()
        self.display_winner()

        