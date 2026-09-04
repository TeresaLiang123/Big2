class Combo():

    def __init__(self, comboName, cards):
        self.comboName = comboName
        self.cards = cards

    def getComboName(self):
        return self.comboName
    
    def getCards(self):
        return self.cards

    def __eq__(self, other):
        return self.comboName == other.comboName and self.cards == other.cards
    