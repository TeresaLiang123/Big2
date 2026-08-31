class Select():

    def __init__(self, card1 = "", card2 = "", card3 = "", card4 = "", card5 = "", isPassTurn = False, isPlaying = False):
        
        self.cards = self.sortCards([card1, card2, card3, card4, card5])
        self.isPassTurn = isPassTurn
        self.isPlaying = isPlaying
    
    def sortCards(self, cards):
        # sort smallest to greatest
        cards.sort(key= lambda card.getNumber())
