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
        "two_of_diamonds": Card("Two of diamonds", 2, "diamonds"),
        "two_of_clover": Card("Two of clover", 2, "clovers"),
        "two_of_heart": Card("Two of hearts", 2, "hearts"),
        "two_of_spade": Card("Two of spade", 2, "spades"),
        
        "three_of_diamonds": Card("Three of diamonds", 3, "diamonds"),
        "three_of_clover": Card("Three of clovers", 3, "clovers"),
        "three_of_heart": Card("Three of hearts", 3, "hearts"),
        "three_of_spade": Card("Three of spades", 3, "spades"),

        "four_of_diamonds": Card("Four of diamonds", 4, "diamonds"),
        "four_of_clover": Card("Four of clovers", 4, "clovers"),
        "four_of_heart": Card("Four of hearts", 4, "hearts"),
        "four_of_spade": Card("Four of spades", 4, "spades"),

        "five_of_diamonds": Card("Five of diamonds", 5, "diamonds"),
        "five_of_clover": Card("Five of clovers", 5, "clovers"),
        "five_of_heart": Card("Five of hearts", 5, "hearts"),
        "five_of_spade": Card("Five of spades", 5, "spades"),

        "six_of_diamonds": Card("Six of diamonds", 6, "diamonds"),
        "six_of_clover": Card("Six of clovers", 6, "clovers"),
        "six_of_heart": Card("Six of hearts", 6, "hearts"),
        "six_of_spade": Card("Six of spades", 6, "spades"),

        "seven_of_diamonds": Card("Seven of diamonds", 7, "diamonds"),
        "seven_of_clover": Card("Seven of clovers", 7, "clovers"),
        "seven_of_heart": Card("Seven of hearts", 7, "hearts"),
        "seven_of_spade": Card("Seven of spades", 7, "spades"),

        "eight_of_diamonds": Card("Eight of diamonds",8, "diamonds"),
        "eight_of_clover": Card("Eight of clovers", 8, "clovers"),
        "eight_of_heart": Card("Eight of hearts", 8, "hearts"),
        "eight_of_spade": Card("Eight of spades", 8, "spades"),

        "nine_of_diamonds": Card("Nine of diamonds", 9, "diamonds"),
        "nine_of_clover": Card("Nine of clovers", 9, "clovers"),
        "nine_of_heart": Card("Nine of hearts", 9, "hearts"),
        "nine_of_spade": Card("Nine of spades", 9, "spades"),

        "ten_of_diamonds": Card("Ten of diamonds",10, "diamonds"),
        "ten_of_clover": Card("Ten of clovers", 10, "clovers"),
        "ten_of_heart": Card("Ten of hearts", 10, "hearts"),
        "ten_of_spade": Card("Ten of spades", 10, "spades"),

        "jack_of_diamonds": Card("Jack of diamonds", 11, "diamonds"),
        "jack_of_clover": Card("Jack of clovers", 11, "clovers"),
        "jack_of_heart": Card("Jack of hearts", 11, "hearts"),
        "jack_of_spade": Card("Jack of spades", 11, "spades"),

        "queen_of_diamonds": Card("Queen of diamonds", 12, "diamonds"),
        "queen_of_clover": Card("Queen of clovers", 12, "clovers"),
        "queen_of_heart": Card("Queen of hearts", 12, "hearts"),
        "queen_of_spade": Card("Queen of spades", 12, "spades"),

        "king_of_diamonds": Card("King of diamonds",13, "diamonds"),
        "king_of_clover": Card("King of clovers", 13, "clovers"),
        "king_of_heart": Card("King of hearts", 13, "hearts"),
        "king_of_spade": Card("King of spades", 13, "spades"),

        "ace_of_diamonds": Card("Ace of diamonds", 14, "diamonds"),
        "ace_of_clover": Card("Ace of clovers", 14, "clovers"),
        "ace_of_heart": Card("Ace of hearts", 14, "hearts"),
        "ace_of_spade": Card("Ace of spades", 14, "spades"),
       
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
    