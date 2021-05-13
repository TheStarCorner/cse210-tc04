import random

class Dealer:


    def __init__(self):
        # self.guess_card.clear()
        # for i in range(1):
            # result = random.randint[1,13]
            # self.guess_card.append(result)
        self.points = 300
        self.place_in_deck = 1
        self.card = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        for x in range(13):
            i = random.randint(1,13)
            while self.card.__contains__(i):
                i = random.randint(1,13)
            self.card[x] = i



    def take_turn(self, guess_card):
        current = self.card[self.place_in_deck]
        if guess_card: #if the user guess_carded that the card will be higher than the last card
            if current > self.card[self.place_in_deck - 1]: #if the current card is higher than the last card (if the user was right)
                self.points += 100
            else: #if the user is wrong
                self.points -= 75
        else: #if the user guess_carded that the card will be lower than the last card
            if current < self.card[self.place_in_deck - 1]: #if the current card is lower than the last card (if the user is right)
                self.points += 100 
            else: #if the user is wrong
                self.points -= 75
        self.place_in_deck +=1



    def get_points(self):
        

        # # """Computes the total number of points for the player.
        # # The player starts the game with 300 points.
        # # The player earns 100 points if they guess_carded correctly.
        # # The player loses 75 points if they guess_carded incorrectly.    
        # # Returns:
        # #     points (total score of the player)
        # #     If a player reaches 0 points the game is over,
        # #     otherwise, the player decides whether or not
        # #     to play again.
        # # """
        # points = 300
   
        # if take_turn > guess_card:
        #     points += 100
        #     points -= 75
       
        # if point = 0:
        #     print ("Game over")   
        return self.points