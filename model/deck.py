import random

class Deck():

    def __init__(self):
        self.deck = self.createDeck()
        player1Name = input("What's player 1's name: ")
        player2Name = input("What's player 2's name: ")
        player3Name = input("What's player 3's name: ")
        player4Name = input("What's player 4's name: ")
        player1 = Player(player1Name)
        player2 = Player(player2Name)
        player3 = Player(player3Name)
        player4 = Player(player4Name)
        self.game = BigTwo(self.deck, player1, player2, player3, player4)
        
    
    def createDeck(self):
        cards = {
        "two_of_diamonds": Card(2, "diamonds"),
        "two_of_clover": Card(2, "clover"),
        "two_of_heart": Card(2, "heart"),
        "two_of_spade": Card(2, "spade"),
        
        "three_of_diamonds": Card(3, "diamonds"),
        "three_of_clover": Card(3, "clover"),
        "three_of_heart": Card(3, "heart"),
        "three_of_spade": Card(3, "spade"),

        "four_of_diamonds": Card(4, "diamonds"),
        "four_of_clover": Card(4, "clover"),
        "four_of_heart": Card(4, "heart"),
        "four_of_spade": Card(4, "spade"),

        "five_of_diamonds": Card(5, "diamonds"),
        "five_of_clover": Card(5, "clover"),
        "five_of_heart": Card(5, "heart"),
        "five_of_spade": Card(5, "spade"),

        "six_of_diamonds": Card(6, "diamonds"),
        "six_of_clover": Card(6, "clover"),
        "six_of_heart": Card(6, "heart"),
        "six_of_spade": Card(6, "spade"),

        "seven_of_diamonds": Card(7, "diamonds"),
        "seven_of_clover": Card(7, "clover"),
        "seven_of_heart": Card(7, "heart"),
        "seven_of_spade": Card(7, "spade"),

        "eight_of_diamonds": Card(8, "diamonds"),
        "eight_of_clover": Card(8, "clover"),
        "eight_of_heart": Card(8, "heart"),
        "eight_of_spade": Card(8, "spade"),

        "nine_of_diamonds": Card(9, "diamonds"),
        "nine_of_clover": Card(9, "clover"),
        "nine_of_heart": Card(9, "heart"),
        "nine_of_spade": Card(9, "spade"),

        "ten_of_diamonds": Card(10, "diamonds"),
        "ten_of_clover": Card(10, "clover"),
        "ten_of_heart": Card(10, "heart"),
        "ten_of_spade": Card(10, "spade"),

        "jack_of_diamonds": Card(11, "diamonds"),
        "jack_of_clover": Card(11, "clover"),
        "jack_of_heart": Card(11, "heart"),
        "jack_of_spade": Card(11, "spade"),

        "queen_of_diamonds": Card(12, "diamonds"),
        "queen_of_clover": Card(12, "clover"),
        "queen_of_heart": Card(12, "heart"),
        "queen_of_spade": Card(12, "spade"),

        "king_of_diamonds": Card(13, "diamonds"),
        "king_of_clover": Card(13, "clover"),
        "king_of_heart": Card(13, "heart"),
        "king_of_spade": Card(13, "spade"),

        "ace_of_diamonds": Card(14, "diamonds"),
        "ace_of_clover": Card(14, "clover"),
        "ace_of_heart": Card(14, "heart"),
        "ace_of_spade": Card(14, "spade"),
       
        }
        deck = []
        for card in cards.keys():
            deck.append(cards[card])
    
    def getDeck():
        return self.deck
    
    def shuffle():
        self.deck = random.shuffle(self.deck)