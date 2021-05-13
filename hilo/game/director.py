from game.dealer import Dealer
#ignore this comment. Attempt 3
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
        self.Dealer = Dealer()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        print(self.Dealer.card) # for testing purposes only
        while self.keep_playing:
            self.do_updates(self.get_inputs())
            self.do_outputs()
            
    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means dealing the card.

        Args:
            self (Director): An instance of Director.
        """
        print("The current card is", self.Dealer.card[self.Dealer.get_place_in_deck()])
        return input("Do you think the card will be higher or lower? (h/l): ")

    def do_updates(self, guess_card):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        if(self.Dealer.get_place_in_deck() < 12):
            if guess_card == 'h':
                self.Dealer.take_turn(True)
            else:
                self.Dealer.take_turn(False)
        if(self.Dealer.points <= 0):
            self.keep_playing = False
            
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the cardthat were rolled and the score.

        Args:
            self (Director): An instance of Director.
        """
        place = self.Dealer.get_place_in_deck()
        
        print(f"\nThe next card was: {self.Dealer.card[place]}")
        print(f"Your current score is: {self.Dealer.get_points()}")
        if(place > 11):
            if self.Dealer.keep_playing():
                choice = input("Do you want to play again? [y/n] ")
                self.keep_playing = (choice == "y")
            elif not self.Dealer.keep_playing():
                self.keep_playing = False
            