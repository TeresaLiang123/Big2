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

    def getPassTurn(self):
        return self.passTurn
    
    def organize(self, cards):
        # sort smallest to greatest
        cards.sort(key= lambda card: card.getNumber())
        return cards
    # show player's hand
    def select(self):
        print("Your hand: \n")
        for card in self.hand:
            print(str(card.getNumber()), card.getSuit())
        
        selection = []
        while not self.isDoneSelecting and len(selection) <= 5:
            isNotSelecting = input("Are you done selecting?: ")
            if isNotSelecting == "y":
                self.isDoneSelecting = True
            else:
                selectOrDelete = input("Are you selecting or deselecting?: ")
                if selectOrDelete == "selecting": # if player is selecting cards
                    cardIndex = int(input("Select which card to play: "))
                    if self.hand[cardIndex] not in selection:
                        selection.append(self.hand[cardIndex])
                    else:
                        print("already selected that card")
                else: # if player is deselecting cards
                    if len(selection) == []:
                        print("There is nothing to deselect")
                    else:
                        cardIndex = int(input("Select which card to deselect: "))
                        deselecting = selection[cardIndex]
                        selection.remove(deselecting)
            selection = self.organize(selection)
        return selection



    # cards is a list of cards that is selected to play
    def play(self):
        selectedCards = self.select()
        combo = Combo("unknown", selectedCards)
        isPass = input("Do you want to pass your turn?: ")
        if isPass == "y":
            print("Turn passed!")
            self.passTurn = True
        elif combo.isSingle(cards):
            return Combo("Single", cards)
        elif combo.isPair(cards):
            return Combo("Pair", cards)
        elif combo.isTriple(cards):
            return Combo("Triple", cards)
        elif combo.isStraight(cards):
            return Combo("Straight", cards)
        elif combo.isFlush(cards):
            return Combo("Flush", cards)
        elif combo.isFullHouse(cards):
            return Combo("Full House", cards)
        elif combo.isStraightFlush(cards):
            return Combo("Straight Flush", cards)
        elif combo.isDynamite(cards):
            return Combo("Dynamite", cards)
        else:
            return print("Invalid play!")
    
    def discardCard(self, cards):
        for card in cards:
            self.hand.remove(card)