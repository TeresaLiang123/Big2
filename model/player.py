class Player():
    def __init__(self, name, cards):
        self.name = name
        self.hand = cards # list of cards
        self.organize(self.hand)
        self.passTurn = False
        self.isDoneSelecting = False

    def getName(self):
        return self.name
    
    def getHand(self):
        return self.hand

    def addToHand(self, card):
        self.hand.append(card)
    
    def organize(self, cards):
        # sort smallest to greatest
        return cards.sort(key= lambda card.getNumber())
    
    # show player's hand
    def select(self):
        print("Your hand: \n")
        for card in self.hand:
            print(str(card.getNumber()), card.getSuit())
        
        selection = []
        while not self.isDoneSelecting:
            cardIndex = input("Select which cards to play: ")
            selection.append(self.hand[cardIndex])
        selection = self.organize(selection)
        return selection



    # cards is a list of cards that is selected to play
    def play(self):
        selectedCards = self.select()
        combo = Combos(selectedCards)
        if isPass:
            print("Turn passed!")
            self.passTurn = True
        elif combo.isSingle():
            return Combo("Single", cards)
        elif combo.isPair():
            return Combo("Pair", cards)
        elif combo.isTriple():
            return Combo("Triple", cards)
        elif combo.isStraight():
            return Combo("Straight", cards)
        elif combo.isFlush():
            return Combo("Flush", cards)
        elif combo.isFullHouse():
            return Combo("Full House", cards)
        elif combo.isStraightFlush():
            return Combo("Straight Flush", cards)
        else:
            return print("Invalid play!")
    
    def discardCard(self, cards):
        for card in cards:
            self.hand.remove(card)