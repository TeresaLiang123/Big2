class Player():
    def __init__(self, name, cards):
        self.name = name
        self.hand = cards # list of cards
        self.organize(self.hand)
        self.passTurn = False

    def getName(self):
        return self.name
    
    def getHand(self):
        return self.hand
    
    def organize(self, cards):
        # sort smallest to greatest
        cards.sort(key= lambda card.getNumber())
    
    # cards is a list of cards that is selected to play
    def play(self, cards, isPass):
        sortedCombo = self.organize(cards)
        combo = Combos(sortedCombo)
        if isPass:
            print("Turn passed!")
            self.passTurn = True
        elif combo.isSingle():
            return Play("Single", cards)
        elif combo.isPair():
            return Play("Pair", cards)
        elif combo.isTriple():
            return Play("Triple", cards)
        elif combo.isStraight():
            return Play("Straight", cards)
        elif combo.isFlush():
            return Play("Flush", cards)
        elif combo.isFullHouse():
            return Play("Full House", cards)
        elif combo.isStraightFlush():
            return Play("Straight Flush", cards)
        else:
            return print("Invalid play!")
    
    def discardCard(self, cards):
        for card in cards:
            self.hand.remove(card)