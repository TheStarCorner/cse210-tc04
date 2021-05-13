from game.dealer import Dealer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        Dealer (Dealer): An instance of the class of objects known as Dealer.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 300
        self.Dealer = Dealer()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

            # self.do_outputs()
            # self.get_inputs()
            # self.do_updates()
            
    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means dealing the card.

        Args:
            self (Director): An instance of Director.
        """
        guess_card = input("Do you think the card will be higher or lower? (h/l): ")

        # self.Dealer.take_turn()

    def do_updates(self, take_turn, guess_card):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        # if guess_card == "h":
        #    if prev_card < current_card:
        #        score + 100
        # else:
        #     score - 75
        # if guess_card == "l":
        #    if prev_card < current_card:
        #        score + 100
        # else:
        #     score - 75
        if self.Dealer.guess_card == 'h':
            self.Dealer.take_turn(True)
        else:
            self.Dealer.take_turn(False)
            # self.Dealer.take_turn()
        # self.score += points
            
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the cardthat were rolled and the score.

        Args:
            self (Director): An instance of Director.
        """
        print(f"\nThe current card is: {self.Dealer.card}")
        guess_card = input("Do you think the card will be higher or lower? (h/l): ")
        print(f"\nThe next card was: {self.Dealer.card}")
        print(f"Your current score is: {self.score}")
        if self.Dealer.keep_playing():
            choice = input("Do you want to play again? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False