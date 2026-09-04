class Combo():

    def __init__(self, comboName, cards):
        self.comboName = comboName
        self.cards = cards
        self.organize()

    def changeComboName(self, newName):
        self.comboName = newName

    def getComboName(self):
        return self.comboName
    
    def getCards(self):
        return self.cards

    def isSingle(self):
        return len(self.cards) == 1
    
    def isPair(self):
        if len(self.cards) == 2:
            return self.cards[0].getNumber() == self.cards[-1].getNumber()
        return False
    
    def isTriple(self):
        if len(self.cards) == 3:
            return self.cards[0].getNumber() == self.cards[1].getNumber() and self.cards[1].getNumber() == self.cards[-1].getNumber()
        return False

    def isStraight(self):
        if len(self.cards) == 5:
            return abs(self.cards[0].getNumber() - self.cards[-1].getNumber()) == 4
        return False

    def isFlush(self):
        if len(self.cards) == 5:
            suit = self.cards[0].getSuit()
            for card in self.cards:
                if card.getSuit() != suit:
                    return False
            return True

    def isStraightFlush(self):
        if len(self.cards) == 5:
            return self.isStraight() and self.isFlush()
        return False
    
    def isFullHouse(self):
        if len(self.cards) == 5:
            # check if first two cards are a pair
            if self.cards[0].getNumber() == self.cards[1].getNumber():
                # check if last 3 cards are a triple
                return self.cards[2].getNumber() == self.cards[3].getNumber() and self.cards[3].getNumber() == self.cards[4].getNumber()
            # check if first 3 cards are a triple
            elif self.cards[0].getNumber() == self.cards[1].getNumber() and self.cards[1].getNumber() == self.cards[2].getNumber():
                return self.cards[3].getNumber() == self.cards[4].getNumber
        return False


    def isFourOfKind(self, cards):
        num = cards[0].getNumber()
        for card in cards:
            if card.getNumber != num:
                return False
        return True

    def isDynamite(self):
        if len(self.cards) == 5:
            # check if first 4 cards are four of a kind
            if self.isFourOfKind(cards[1:]) or self.isFourOfKind(cards[:4]):
                return True
        return False

    def organize(self):
        self.cards.sort(key=lambda card: card.getNumber())

    def __eq__(self, other):
        return self.comboName == other.comboName and self.cards == other.cards