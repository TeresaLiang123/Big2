class Card():

    def __init__(self, num, suit):
        self.number = num
        self.suit = suit
    
    def getNumber(self):
        return self.number
    
    def getSuit(self):
        return self.suit

    def __eq__(self, other_card):
        return self.number == other_card.number and self.suit == other_card.suit