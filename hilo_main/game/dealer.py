from game.card import DisplayCard
from time import sleep
import random
	

	

class Dealer:
    """A person who directs the game.

    The dealer's responsability is to control the sequence of the game

    Attributes:
        card(int): The value of the card drawn
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """


    def _init_(self):
        """Constructor a new Dealer.

        Args:
            self (Dealer): an instance of Dealer.
        """
        self.is_playing = ''
        self.card = 0
        self.card_text = ''
        self.guess_card = 0
        self.guess = ''
        self.points = 0
        self.new_points = 0
        self.stop_card = 0
        self.number_times = 0


    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Dealer): an instance of Dealer.
        """
        self.points = 300
        self.is_playing = True
        self.number_times = 0


        print(f'\n··········· \033[31mWELCOME TO THE HI-LO GAME!\033[0m ···········')
        


        while self.is_playing:
            display_card = DisplayCard()
            self.card = display_card.drawn()


            self.stop_card = self.card
            self.print_numbers()


            self.get_input()
            self.output()
            self.update_points()


            if self.is_playing == False:
                break


            self.play_again()


    def print_numbers(self):
        """This function prints a list of numbers and stops at the selected card..

        Args:
            self (Dealer): an instance of Dealer.
        """
        print()
        print()
        print(f'\nThe card is:')
        for i in range(14):
            if i != 0 and i < self.stop_card:
                print(i, sep=' ', end=' ', flush=True)
                sleep(0.1)


        print(f'\033[31m{self.stop_card}\033[0m')


    def get_input(self):
        """Ask the user to guess if the next card is higher or lower, and confirm the input is entered correctly (either "h" or "l" only).
        After the input is validated, call the function draw(self) and display a new card.

        Args:
            self (Dealer): an instance of Dealer.
        """


        while True:
            print()
            self.guess = input('Higher or Lower [h/l]: ').lower()


            if self.guess == 'l' or self.guess == 'h':


                while True:
                    display_card = DisplayCard()
                    self.guess_card = display_card.drawn()
                    if self.guess_card == self.card:
                        continue
                    else:
                        break


                print(f'Next card was: {self.guess_card}')
                break


            else:
                print('Wrong letter')
                continue


    def update_points(self):
        """A method that determines the score for the entire game

        Args:
            self (Dealer): an instance of Dealer.
        """


        self.points += self.new_points
        self.number_times += 1


        if self.points > 0:
            if (self.card < self.guess_card and self.guess == 'l') or (self.card > self.guess_card and self.guess == 'h'):
                print('\n\033[32mYou lost 75 points!\033[0m')
                print()
            else:
                print('\n\033[032mYou just won 100 points!\033[0m')
                print()
            print(f'Your new score is: {self.points}')


        else:
            self.is_playing = False
            print(f'\n\tCONGRATULATIONS - You play {self.number_times} times')
            print('\n\tYou do not have enough points at this time\n\n')
            self.final()
            print()


    def final(self):
        """Print game over to finish the game

        Args:
            self (Dealer): an instance of Dealer.
        """
        print('Game Over')


    def output(self):
        """A method that determines the score for one round of play

        Args:
            self (Dealer): an instance of Dealer.
        """


        if (self.card < self.guess_card and self.guess == 'l') or (self.card > self.guess_card and self.guess == 'h'):
            self.new_points = -75
        else:
            self.new_points = 100


    def play_again(self):
        """Ask the user if he wants to play another round.

        Args:
            self (Dealer): an instance of Dealer.
        """


        play = input('Play again [y/n]: ')


        if play == 'y':
            self.is_playing = True
        else:
            print('\n\tThanks for playing!\n')
            self.final()
            self.is_playing = False
