class Combos():

    def __init__(self, combo):
        self.combo = combo

    def isSingle(self):
        return len(self.combo) == 0
    
    def isDouble(self):
        if len(self.combo) == 2:
            card1 = self.combo[0]
            card2 = self.combo[-1]
            return card1.getNumber() == card2.getNumber()
        else:
            return false

    def isTriple(self):
        if len(self.combo) == 3:
            card1 = self.combo[0]
            card2 = self.combo[1]
            card3 = self.combo[2]
            return card1.getNumber() == card2.getNumber() and card2.getNumber() == card3.getNumber()
        else:
            return false
    
    def isStraight(self):
        if len(self.combo) == 5:
            return abs(self.combo[-1] - self.combo[0]) == 4:
        else:
            return false
    
    def isFlush(self):
        if len(self.combo) == 5:
            index = 0
            suit = self.combo[0].getSuit()
            for card in self.combo:
                if card.getSuit() != suit:
                    return false
        return true
    
    def isFullHouse(self):
        return

    def isStraightFlush(self):
        return self.isStraight() and self.isFlush()
    
    def isDynamite(self):
        if len(self.combos) == 5:
            self.combo[0]
            self.combo[1]
            self.combo[2]
            self.combo[3]
            self.combo[4]
            
            for card in self.combo:
    
