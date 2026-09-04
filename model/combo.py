class Combo():

    def __init__(self, comboName, cards):
        self.comboName = comboName
        self.cards = cards
        self.organize()

    def getComboName(self):
        return self.comboName
    
    def getCards(self):
        return self.cards

    def isSingle(self, cards):
        return len(cards) == 1
    
    def isPair(self, cards):
        if len(cards) == 2:
            return cards[0].getNumber() == cards[-1].getNumber()
        return False
    
    def isTriple(self, cards):
        if len(cards) == 3:
            return cards[0].getNumber() == cards[1].getNumber() and cards[1].getNumber() == self.cards[-1].getNumber()
        return False

    def isStraight(self, cards):
        if len(cards) == 5:
            return abs(cards[0].getNumber() - cards[-1]) == 4
        return False

    def isFlush(self, cards):
        if len(cards) == 5:
            suit = cards[0].getSuit()
            for card in cards:
                if card.getSuit() != suit:
                    return False
            return True

    def isStraightFlush(self, cards):
        if len(cards) == 5:
            return self.isStraight(cards) and self.isFlush(cards)
        return False
    
    def isFullHouse(self, cards):
        if len(cards) == 5:
            return self.isPair(cards[:2]) and self.isTriple(cards[2:]) or self.isTriple([:3]) and self.isPair(3:):

    def isFourOfKind(self, cards):
        num = cards[0].getNumber()
        for card in cards:
            if card.getNumber != num:
                return False
        return True

    def isDynamite(self, cards):
        if len(cards) == 5:
            return self.isSingle(cards[:1]) and self.isFourOfKind(cards[1:]) or self.isSingle(cards[:4]) and self.isFourOfKind[:1]

    def organize(self):
        self.cards.sort(key=lambda card: card.getNumber())

    def __eq__(self, other):
        return self.comboName == other.comboName and self.cards == other.cards