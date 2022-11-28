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
        print('Enter 1 for 1 Player. Enter 2 for 2 players')
        self.game_mode = input('')

        if self.game_mode == 1:
            self.player_one = Human()
            self.player_two = AI()

        elif self.game_mode == 2:
            self.player_one = Human()
            self.player_two = Human()

        # if statement needs to go here for player selection
        # An input needs to be placed here for selection

    def choose_gesture(self):
        print("Choose 0 for rock")
        print('Choose 1 for paper')
        print('Choose 2 for scissors')
        print('Choose 3 for lizard')
        print('Choose 4 for Spock')



    def display_winner():
        pass

    def run_game(self):
        self.welcome()
        self.player_select()
        self.choose_gesture()
        self.display_winner()