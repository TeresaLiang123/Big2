from combo import Combo

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
        cardi = 0
        for card in self.hand:
            print(str(cardi) + ". " + str(card.getNumber()), card.getSuit())
            cardi+=1
        selection = []
        while not self.isDoneSelecting and len(selection) <= 5:
            print("This is your selection: \n")
            for card in selection:
                print(str(card.getNumber()), card.getSuit())
            if len(selection) == 5:
                print("You've reached the max number of cards you can select")
                isNotSelecting = input("Are you done selecting?: ")
                if isNotSelecting == "n":
                    cardIndex = int(input("Select which card to deselect: "))
                    deselecting = selection[cardIndex]
                    selection.remove(deselecting)
                
            
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
                    if len(selection) == 0:
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
        combo = Combo("Unknown", selectedCards)
        isPass = input("Do you want to pass your turn?: ")
        if isPass == "y":
            print("Turn passed!")
            self.passTurn = True
        elif combo.isSingle():
            combo.changeComboName("Single")
        elif combo.isPair():
            combo.changeComboName("Pair")
        elif combo.isTriple():
            combo.changeComboName("Triple")
        elif combo.isStraight():
            combo.changeComboName("Straight")
        elif combo.isFlush():
            combo.changeComboName("Flush")
        elif combo.isFullHouse():
            combo.changeComboName("Full House")
        elif combo.isStraightFlush():
            combo.changeComboName("Straight Flush")
        elif combo.isDynamite():
            combo.changeComboName("Dynamite")
        else:
            return print("Invalid play!")
        return combo
    
    def discardCard(self, cards):
        for card in cards:
            self.hand.remove(card)