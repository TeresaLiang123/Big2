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
        for i, card in enumerate(self.hand, start=1):
            print(f"{i}. {card.getNumber()} {card.getSuit()}")

        selection = []
        while not self.isDoneSelecting:
            print("This is your selection: \n")
            for i, card in enumerate(selection, start=1):
                print(f"{i}. {card.getNumber()} {card.getSuit()}")

            if len(selection) == 5:
                print("You've reached the max number of cards you can select")
                isDeselectingOrDone = input("Would you like to deselect or are you done?: ")
                if isDeselectingOrDone == "deselect":
                    cardIndex = int(input("Select which card to deselect: ")) - 1
                    deselecting = selection[cardIndex]
                    selection.remove(deselecting)
                elif isDeselectingOrDone == "done":
                    self.isDoneSelecting = True
                selection = self.organize(selection)
                continue  # skip the normal prompt this round

            isNotSelecting = input("Are you done?: ")
            if isNotSelecting == "y":
                self.isDoneSelecting = True
            else:
                selectOrDelete = input("Are you selecting or deselecting?: ")
                if selectOrDelete == "selecting":
                    cardIndex = int(input("Select which card to play: ")) - 1
                    if self.hand[cardIndex] not in selection:
                        selection.append(self.hand[cardIndex])
                    else:
                        print("already selected that card")
                else:
                    if len(selection) == 0:
                        print("There is nothing to deselect")
                    else:
                        cardIndex = int(input("Select which card to deselect: ")) - 1
                        deselecting = selection[cardIndex]
                        selection.remove(deselecting)

            selection = self.organize(selection)

        return selection

    # NEW: pure combo-classification logic — no input(), fully testable
    def playCards(self, cards):
        combo = Combo("Unknown", cards)
        if combo.isSingle():
            combo.changeComboName("Single")
        elif combo.isPair():
            combo.changeComboName("Pair")
        elif combo.isTriple():
            combo.changeComboName("Triple")
        elif combo.isDynamite():
            combo.changeComboName("Dynamite")
        elif combo.isStraightFlush():
            combo.changeComboName("Straight Flush")
        elif combo.isFullHouse():
            combo.changeComboName("Full House")
        elif combo.isFlush():
            combo.changeComboName("Flush")
        elif combo.isStraight():
            combo.changeComboName("Straight")
        else:
            print("Invalid play!")
            return None
        return combo

    # cards is a list of cards that is selected to play
    def play(self):
        selectedCards = self.select()
        isPass = input("Do you want to pass your turn?: ")
        if isPass == "y":
            print("Turn passed!")
            self.passTurn = True
            return None
        return self.playCards(selectedCards)

    def discardCard(self, cards):
        for card in cards:
            self.hand.remove(card)