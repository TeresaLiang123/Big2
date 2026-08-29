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
            return False

    def isTriple(self):
        if len(self.combo) == 3:
            card1 = self.combo[0]
            card2 = self.combo[1]
            card3 = self.combo[2]
            return card1.getNumber() == card2.getNumber() and card2.getNumber() == card3.getNumber()
        else:
            return False
    
    def isStraight(self):
        if len(self.combo) == 5:
            return abs(self.combo[-1] - self.combo[0]) == 4:
        else:
            return False
    
    def isFlush(self):
        if len(self.combo) == 5:
            index = 0
            suit = self.combo[0].getSuit()
            for card in self.combo:
                if card.getSuit() != suit:
                    return False
        return True
    
    def isFullHouse(self):
        # 22333
        # 55599
        if len(self.combo) == 5:
            firstNum = self.combo[0].getNumber()
            lastNum = self.combo[-1].getNumber()
            # check how many duplicates of num in a dictionary
            counts = Counter(card.getNumber() for card in self.combos)
            if counts[firstNum] == 2 and counts[lastNum] == 3 or counts[lastNum] == 2 and counts[firstNum] == 3:
                return True
            else:
                False


    def isStraightFlush(self):
        return self.isStraight() and self.isFlush()
    
    def isDynamite(self):
        if len(self.combos) == 5:
            # 24444
            # 55558

            firstNum = self.combos[0]
            lastNum = self.combos[-1]
            if counts[firstNum] == 1 and counts[lastNum] == 4 or counts[lastNum] == 4 and counts[firstNum] == 1:
                return True
            else:
                return False