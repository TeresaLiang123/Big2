class Select():

    def __init__(self, card1 = "", card2 = "", card3 = "", card4 = "", card5 = "", isPassTurn = False):
        
        self.cards = self.sortCards([card1, card2, card3, card4, card5])
        self.isPassTurn = isPassTurn
    
    def sortCards(self, cards):
        # sort smallest to greatest
        cards.sort(key= lambda card.getNumber())
    
    def play(self):
        combo = Combos(self.cards)
        if combo.isSingle():
            return "Single"
        elif combo.isPair():
            return "Pair"
        elif combo.isTriple():
            return "Triple"
        elif combo.isStraight():
            return "Straight"
        elif combo.isFlush():
            return "Flush"
        elif combo.isFullHouse():
            return "Full House"
        elif combo.isStraightFlush():
            return "Straight Flush"
        

        