class Card():

    def __init__(self, name, num, suit):
        self.name = name
        self.number = num
        self.suit = suit
    
    def getName(self):
        return self.name

    def getNumber(self):
        return self.number
    
    def getSuit(self):
        return self.suit

    def __eq__(self, other_card):
        return self.name == other_card.name and self.number == other_card.number and self.suit == other_card.suit