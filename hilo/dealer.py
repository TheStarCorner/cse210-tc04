import random

class Dealer:


    def __init__(self):
        self.points = 300
        self.place_in_deck = 1
        self.cards = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        for x in range(13):
            i = random.randint(1,13)
            while self.cards.__contains__(i):
                i = random.randint(1,13)
            self.cards[x] = i



    def take_turn(self, guess):
        current = self.cards[self.place_in_deck]
        if guess: #if the user guessed that the card will be higher than the last card
            if current > self.cards[self.place_in_deck - 1]: #if the current card is higher than the last card (if the user was right)
                self.points += 100
            else: #if the user is wrong
                self.points -= 75
        else: #if the user guessed that the card will be lower than the last card
            if current < self.cards[self.place_in_deck - 1]: #if the current card is lower than the last card (if the user is right)
                self.points += 100 
            else: #if the user is wrong
                self.points -= 75
        self.place_in_deck +=1



    def get_points(self):
        

        # # """Computes the total number of points for the player.
        # # The player starts the game with 300 points.
        # # The player earns 100 points if they guessed correctly.
        # # The player loses 75 points if they guessed incorrectly.    
        # # Returns:
        # #     points (total score of the player)
        # #     If a player reaches 0 points the game is over,
        # #     otherwise, the player decides whether or not
        # #     to play again.
        # # """
        # points = 300
   
        # if take_turn > guess:
        #     points += 100
        #     points -= 75
       
        # if point = 0:
        #     print ("Game over")   
        return self.points