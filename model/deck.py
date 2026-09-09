import random
from card import Card
from player import Player
from bigTwo import BigTwo
class Deck():

    def __init__(self):
        self.deck = self.createDeck()
        self.shuffle()
        self.deal()
    
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
        return deck
    
    def getPlayer1Hand(self):
        return self.player1Hand
    
    def getPlayer2Hand(self):
        return self.player2Hand
    
    def getPlayer3Hand(self):
        return self.player3Hand
    
    def getPlayer4Hand(self):
        return self.player4Hand

    def getDeck(self):
        return self.deck
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        self.player1Hand = []
        self.player2Hand = []
        self.player3Hand = []
        self.player4Hand = []
        playerIndex = 0
        for card in self.deck:
            if playerIndex == 0:
                self.player1Hand.append(card)
            elif playerIndex == 1:
                self.player2Hand.append(card)
            elif playerIndex == 2:
                self.player3Hand.append(card)
            elif playerIndex == 3:
                self.player4Hand.append(card)
                playerIndex = -1
            playerIndex += 1
    