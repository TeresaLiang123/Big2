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
        "two_of_diamonds": Card("2 of ♦️", 15, "diamonds"),
        "two_of_clover": Card("2 of ♣️", 15, "clovers"),
        "two_of_heart": Card("2 of ❤️", 15, "hearts"),
        "two_of_spade": Card("2 of ♠️", 15, "spades"),
        
        "three_of_diamonds": Card("3 of ♦️", 3, "diamonds"),
        "three_of_clover": Card("3 of ♣️", 3, "clovers"),
        "three_of_heart": Card("3 of ❤️", 3, "hearts"),
        "three_of_spade": Card("3 of ♠️", 3, "spades"),

        "four_of_diamonds": Card("4 of ♦️", 4, "diamonds"),
        "four_of_clover": Card("4 of ♣️", 4, "clovers"),
        "four_of_heart": Card("4 of ❤️", 4, "hearts"),
        "four_of_spade": Card("4 of ♠️", 4, "spades"),

        "five_of_diamonds": Card("5 of ♦️", 5, "diamonds"),
        "five_of_clover": Card("5 of ♣️", 5, "clovers"),
        "five_of_heart": Card("5 of ❤️", 5, "hearts"),
        "five_of_spade": Card("5 of ♠️", 5, "spades"),

        "six_of_diamonds": Card("6 of ♦️", 6, "diamonds"),
        "six_of_clover": Card("6 of ♣️", 6, "clovers"),
        "six_of_heart": Card("6 of ❤️", 6, "hearts"),
        "six_of_spade": Card("6 of ♠️", 6, "spades"),

        "seven_of_diamonds": Card("7 of ♦️", 7, "diamonds"),
        "seven_of_clover": Card("7 of ♣️", 7, "clovers"),
        "seven_of_heart": Card("7 of ❤️", 7, "hearts"),
        "seven_of_spade": Card("7 of ♠️", 7, "spades"),

        "eight_of_diamonds": Card("8 of ♦️",8, "diamonds"),
        "eight_of_clover": Card("8 of ♣️", 8, "clovers"),
        "eight_of_heart": Card("8 of ❤️", 8, "hearts"),
        "eight_of_spade": Card("8 of ♠️", 8, "spades"),

        "nine_of_diamonds": Card("9 of ♦️", 9, "diamonds"),
        "nine_of_clover": Card("9 of ♣️", 9, "clovers"),
        "nine_of_heart": Card("9 of ❤️", 9, "hearts"),
        "nine_of_spade": Card("9 of ♠️", 9, "spades"),

        "ten_of_diamonds": Card("10 of ♦️",10, "diamonds"),
        "ten_of_clover": Card("10 of ♣️", 10, "clovers"),
        "ten_of_heart": Card("10 of ❤️", 10, "hearts"),
        "ten_of_spade": Card("10 of ♠️", 10, "spades"),

        "jack_of_diamonds": Card("Jack of ♦️", 11, "diamonds"),
        "jack_of_clover": Card("Jack of ♣️", 11, "clovers"),
        "jack_of_heart": Card("Jack of ❤️", 11, "hearts"),
        "jack_of_spade": Card("Jack of ♠️", 11, "spades"),

        "queen_of_diamonds": Card("Queen of ♦️", 12, "diamonds"),
        "queen_of_clover": Card("Queen of ♣️", 12, "clovers"),
        "queen_of_heart": Card("Queen of ❤️", 12, "hearts"),
        "queen_of_spade": Card("Queen of ♠️", 12, "spades"),

        "king_of_diamonds": Card("King of ♦️",13, "diamonds"),
        "king_of_clover": Card("King of ♣️", 13, "clovers"),
        "king_of_heart": Card("King of ❤️", 13, "hearts"),
        "king_of_spade": Card("King of ♠️", 13, "spades"),

        "ace_of_diamonds": Card("Ace of ♦️", 14, "diamonds"),
        "ace_of_clover": Card("Ace of ♣️", 14, "clovers"),
        "ace_of_heart": Card("Ace of ❤️", 14, "hearts"),
        "ace_of_spade": Card("Ace of ♠️", 14, "spades"),
       
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
    