import random

class Deck():

    def __init__(self):
        self.deck = self.createDeck()
        player1Name = input("What's player 1's name: ")
        player2Name = input("What's player 2's name: ")
        player1 = Player(player1Name)
        player2 = Player(player2Name)
        self.game = BigTwo(self.deck, player1, player2)
        
    
    def createDeck(self):
        cards = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "jack": 11,
        "queen": 12,
        "king": 13,
        "ace": 14
        }
        deck = []
        for card in cards.keys():
            for i in 4:
                deck.append(Card(card, cards[card]))
    
    def getDeck():
        return self.deck
    
    def shuffle():
        self.deck = random.shuffle(self.deck)