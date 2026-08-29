class Select():

    def __init__(self, card1 = "", card2 = "", card3 = "", card4 = "", card5 = "", isPassTurn = False, isPlaying = False):
        
        self.cards = self.sortCards([card1, card2, card3, card4, card5])
        self.isPassTurn = isPassTurn
        self.isPlaying = isPlaying
    
    def sortCards(self, cards):
        # sort smallest to greatest
        cards.sort(key= lambda card.getNumber())
    
    def play(self):
        combo = Combos(self.cards)
        if combo.isSingle():
            return Play("Single", self.cards)
        elif combo.isPair():
            return Play("Pair", self.cards)
        elif combo.isTriple():
            return Play("Triple", self.cards)
        elif combo.isStraight():
            return Play("Straight", self.cards)
        elif combo.isFlush():
            return Play("Flush", self.cards)
        elif combo.isFullHouse():
            return Play("Full House", self.cards)
        elif combo.isStraightFlush():
            return Play("Straight Flush", self.cards)