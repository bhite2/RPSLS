from player import Player
from player import Human
from player import AI


class Game():

    def welcome(self):
        print('Welcome to ROCK, PAPER, SCISSORS, LIZARD, SPOCK!')
        print('Each player picks a gesture and reveals it at the same time. Player with the winning gesture wins the round.')
        print('If both players use the same gesture, that is a tie. The round will be replayed.')
        print('First player to get two wins is crowned the winner.')
        print('You can choose between Rock, Paper, Scissors, Lizard or Spock')
        print('Rock crushes Scissors')
        print('Scissors cuts Paper')
        print('Paper covers Rock')
        print('Rock crushes Lizard')
        print('Lizard poisons Spock')
        print('Spock smashes Scissors')
        print('Scissors decapitates Lizard')
        print('Lizard eats Paper')
        print('Paper disproves Spock')
        print('Spock vaporizes Rock')
        print('May the best player win')

    def player_select(self):
        print('Enter 1 for Single Player. Enter 2 for Versus Mode')
        self.game_mode = input('')
        # if statement needs to go here for player selection
        if self.game_mode == '1':
            print('You have selected Single Player mode.')
            self.player_one = Human()
            self.player_two = AI()

        elif self.game_mode == '2':
            print('You have selected Versus Mode')
            self.player_one = Human()
            self.player_two = Human()

        
        # Want player to pick own name. Does this need it's own function

    def choose_gesture(self):
        print("Choose 0 for rock")
        print('Choose 1 for paper')
        print('Choose 2 for scissors')
        print('Choose 3 for lizard')
        print('Choose 4 for Spock')

        if self.player_one.chosen_gesture == 'rock':
            if self.player_two.chosen_gesture == 'rock':
                print('It is a tie.')
            
            elif self.player_two.chosen_gesture == 'paper':
                self.player_two.player_score += 1
                print(f'paper covers rock {self.player_two.name} wins')
            
            elif self.player_two.chosen_gesture == 'scissors':
                self.player_one.player_score += 1
                print(f'rock crushes scissors {self.player_one.name} wins')

            elif self.player_two.chosen_gesture == 'lizard':
                self.player_one.player_score += 1
                print(f'rock crushes lizard {self.player_one.name} wins')
            
            elif self.player_two.chosen_gesture == 'spock':
                self.player_two.player_score +=1
                print(f'spock vaporizes rock {self.player_two.name} wins')
         
        if self.player_one.chosen_gesture == 'paper':
            if self.player_two.chosen_gesture == 'rock':
                self.player_one.player_score += 1
                print(f'paper covers rock {self.player_one.name} wins')
            
            elif self.player_two.chosen_gesture == 'paper':
                print('Its a tie') 

            elif self.player_two.chosen_gesture == 'scissors':
                self.player_two.player_score += 1
                print(f'scissors cut paper {self.player_two.name} wins')

            elif self.player_two.chosen_gesture == 'lizard':
                self.player_two.player_score += 1
                print(f'lizard eats paper {self.player_two.name} wins')
            
            elif self.player_two.chosen_gesture == 'spock':
                self.player_one.player_score += 1
                print(f'paper disproves spock {self.player_one.name} wins')
        
        # 3rd line
        if self.player_one.chosen_gesture == 'scissors':
            if self.player_two.chosen_gesture == 'rock':
                self.player_two.player_score += 1
                print(f'rock crushes scissors {self.player_two.name} wins')
            
            elif self.player_two.chosen_gesture == 'scissors':
                print('Its a tie') 

            elif self.player_two.chosen_gesture == 'paper':
                self.player_one.player_score += 1
                print(f'scissors cut paper {self.player_one.name} wins')

            elif self.player_two.chosen_gesture == 'lizard':
                self.player_one.player_score += 1
                print(f'scissors decapitates lizard {self.player_one.name} wins')
            
            elif self.player_two.chosen_gesture == 'spock':
                self.player_two.player_score += 1
                print(f'spock smashes scissors {self.player_two.name} wins')
        
        # 4th line
        if self.player_one.chosen_gesture == 'lizard':
            if self.player_two.chosen_gesture == 'rock':
                self.player_two.player_score += 1
                print(f'rock crushes lizard {self.player_two.name} wins')
            
            elif self.player_two.chosen_gesture == 'lizard':
                print('Its a tie') 

            elif self.player_two.chosen_gesture == 'scissors':
                self.player_two.player_score += 1
                print(f'scissors decapitates lizard {self.player_two.name} wins')

            elif self.player_two.chosen_gesture == 'paper':
                self.player_one.player_score += 1
                print(f'lizard eats paper {self.player_one.name} wins')
            
            elif self.player_two.chosen_gesture == 'spock':
                self.player_one.player_score += 1
                print(f'lizard poisons spock {self.player_one.name} wins')
        
        # 5th line
        if self.player_one.chosen_gesture == 'spock':
            if self.player_two.chosen_gesture == 'rock':
                self.player_one.player_score += 1
                print(f'spock vaporizes rock {self.player_one.name} wins')
            
            elif self.player_two.chosen_gesture == 'spock':
                print('Its a tie') 

            elif self.player_two.chosen_gesture == 'paper':
                self.player_two.player_score += 1
                print(f'paper disproves spock {self.player_two.name} wins')

            elif self.player_two.chosen_gesture == 'scissors':
                self.player_one.player_score += 1
                print(f'spock smashes scissors {self.player_one.name} wins')
            
            elif self.player_two.chosen_gesture == 'lizard':
                self.player_two.player_score += 1
                print(f'lizard poisons spock {self.player_two.name} wins')

        #If and elif statements for all possible outcomes
    def display_winner():
        pass

    def run_game(self):
        self.welcome()
        self.player_select()
        self.choose_gesture()
        self.display_winner()