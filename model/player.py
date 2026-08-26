class Player():
    def __init__(self, name):
        self.name = name
        self.cards = []
    
    def getName(self):
        return self.name
    
    def getCards(self):
        return self.cards
    
    def organize(self):
        return
    
    def playCard(self):
        return
    
    def discardCard(self, card):
        self.cards.remove(card)