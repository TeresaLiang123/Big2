from card import Card
class BigTwo():

    def __init__(self, deck, player1, player2, player3, player4):
        self.players = [player1, player2, player3, player4]
        self.deck = deck
        self.currentPlayStack = [] # list of combo lists Played objects
        self.winner = None
        self.playerTurn = None
        self.playerIndex = None
        self.passCounter = 0
        
        self.suitRanks = {
            "diamonds": 1,
            "clovers": 2,
            "hearts": 3,
            "spades": 4
        }

        # key = type of combo
        # value = [list of combos that can beat the key which is the type of combo]
        self.heigharchyCombos = {
            "Striaght": ["Flush", "Straight Flush", "Full House", "Dynamite"],
            "Flush": [ "Straight Flush", "Full House", "Dynamite"],
            "Full House":["Striaght Flush", "Dynamite"],
            "Straight Flush": ["Dynamite"]
        }

    '''
    1. shuffle deck of cards
    2. deal the cards to players

    First round matters. Diamond 3 goes first
    
    While players still have cards in their hand
    3. sort the hands of the players
    4. check who goes first (player with diamond 3 goes first, must play a combo that involves diamond 3)
    5. check if the player passes their turn. isPassTurn() if it is then pass. Count how many passes there are.
       if there's three passes clear the currentPlayStack list to be empty. Allow the current player to play anything
    
    6. if it's the first round have current player to play a combo (must play a combo that involves diamond 3)
    7. next player turn

    8. Update who the winner is by checking who has no cards in their hand
    '''

    def whoFirst(self):
        playerIndex = 0
        for player in self.players:
            for card in player.getHand():
                if card.getName() == "3 of ♦️":
                    self.playerTurn = player
                    self.playerIndex = playerIndex
            playerIndex+=1


    def play(self):
        self.whoFirst()
        print("Player's turn: \n")
        print(self.playerTurn)
        print(self.playerIndex)

        roundNum = 1
        playerCombo = None

        while True:
            if len(self.currentPlayStack) != 0:
                print("Previously played:")
                for card in self.currentPlayStack[-1].getCards():
                    print(card.getName())

            # ROUND 1: must play a combo containing the 3 of diamonds
            if roundNum == 1:
                playerCombo = self.playerTurn.play()
                if playerCombo is None:
                    print("You must play a valid combo containing the 3 of diamonds!")
                    continue
                if playerCombo.getComboName() == "Unknown":
                    print("That's not a valid combo. Try again.")
                    continue

                has_diamond3 = any(
                    card.getNumber() == 3 and card.getSuit() == "diamonds"
                    for card in playerCombo.getCards()
                )
                if not has_diamond3:
                    print("Must play diamond 3!")
                    continue

                self.currentPlayStack.append(playerCombo)
                self.playerTurn.discardCard(playerCombo.getCards())

                if len(self.playerTurn.getHand()) == 0:
                    self.winner = self.playerTurn
                    print(f"Winner is {self.winner.getName()}!")
                    return

                if self.playerIndex == 3:
                    self.playerIndex = 0
                else:
                    self.playerIndex += 1
                self.playerTurn = self.players[self.playerIndex]
                roundNum += 1
                continue

            # ROUNDS 2+
            playerCombo = self.playerTurn.play()

            if playerCombo is None:
                self.passCounter += 1
                print(f"{self.playerTurn.getName()} passed.\n")

                if self.passCounter == 3:
                    self.currentPlayStack = []
                    self.passCounter = 0

                if self.playerIndex == 3:
                    self.playerIndex = 0
                else:
                    self.playerIndex += 1
                self.playerTurn = self.players[self.playerIndex]
                continue

            if playerCombo.getComboName() == "Unknown":
                print("That's not a valid combo. Try again.")
                continue

            if len(self.currentPlayStack) == 0:
                # stack was just cleared (3 passes) — anything goes
                self.currentPlayStack.append(playerCombo)
                self.playerTurn.discardCard(playerCombo.getCards())

                if len(self.playerTurn.getHand()) == 0:
                    self.winner = self.playerTurn
                    print(f"Winner is {self.winner.getName()}!")
                    return

                if self.playerIndex == 3:
                    self.playerIndex = 0
                else:
                    self.playerIndex += 1
                self.playerTurn = self.players[self.playerIndex]
                continue

            # Combos to compare and identify which combo is bigger and if
            # player's combo is a valid play
            currentPlayCombo = self.currentPlayStack[-1]
            isValidPlay = False

            if currentPlayCombo.getComboName() == "Single" and playerCombo.getComboName() == "Single":
                if self.isBiggerSingleOrPairOrTriple(currentPlayCombo, playerCombo):
                    print("Valid play! Your card is bigger\n")
                    isValidPlay = True
                else:
                    print("Your card is not bigger\n")
            elif currentPlayCombo.getComboName() == "Pair" and playerCombo.getComboName() == "Pair":
                if self.isBiggerSingleOrPairOrTriple(currentPlayCombo, playerCombo):
                    print("Valid play! Your pair is bigger\n")
                    isValidPlay = True
                else:
                    print("Your pair is not bigger\n")
            elif currentPlayCombo.getComboName() == "Triple" and playerCombo.getComboName() == "Triple":
                if self.isBiggerSingleOrPairOrTriple(currentPlayCombo, playerCombo):
                    print("Valid play! Your triple is bigger\n")
                    isValidPlay = True
                else:
                    print("Your triple is not bigger\n")
            elif currentPlayCombo.getComboName() == "Straight" and playerCombo.getComboName() == "Straight":
                if self.isBiggerStraightOrStriaghtFlush(currentPlayCombo, playerCombo):
                    print("Valid play! Your straight is bigger\n")
                    isValidPlay = True
                else:
                    print("Your straight is not bigger\n")
            elif currentPlayCombo.getComboName() == "Straight Flush" and playerCombo.getComboName() == "Straight Flush":
                if self.isBiggerStraightOrStriaghtFlush(currentPlayCombo, playerCombo):
                    print("Valid play! Your straight flush is bigger\n")
                    isValidPlay = True
                else:
                    print("Your straight flush is smaller\n")
            elif currentPlayCombo.getComboName() == "Full House" and playerCombo.getComboName() == "Full House":
                if self.isBiggerFullHouse(currentPlayCombo, playerCombo):
                    print("Valid play! Your full house is bigger\n")
                    isValidPlay = True
                else:
                    print("Your full house is smaller\n")
            elif currentPlayCombo.getComboName() == "Flush" and playerCombo.getComboName() == "Flush":
                if self.isBiggerFlush(currentPlayCombo, playerCombo):
                    print("Valid play! Your flush is bigger\n")
                    isValidPlay = True
                else:
                    print("Your flush is smaller\n")
            elif currentPlayCombo.getComboName() == "Dynamite" and playerCombo.getComboName() == "Dynamite":
                if self.isBiggerDynamite(currentPlayCombo, playerCombo):
                    print("Valid play! Your dynamite is bigger\n")
                    isValidPlay = True
                else:
                    print("Your dynamite is smaller\n")
            elif currentPlayCombo.getComboName() == "Straight" and playerCombo.getComboName() in self.heigharchyCombos["Striaght"]:
                print("Valid play! Your combo is bigger")
                isValidPlay = True
            elif currentPlayCombo.getComboName() == "Flush" and playerCombo.getComboName() in self.heigharchyCombos["Flush"]:
                print("Valid play! Your combo is bigger")
                isValidPlay = True
            elif currentPlayCombo.getComboName() == "Full House" and playerCombo.getComboName() in self.heigharchyCombos["Full House"]:
                print("Valid play! Your combo is bigger")
                isValidPlay = True
            elif currentPlayCombo.getComboName() == "Straight Flush" and playerCombo.getComboName() in self.heigharchyCombos["Straight Flush"]:
                print("Valid play! Your combo is bigger")
                isValidPlay = True
            else:
                print("Not a valid play")

            if isValidPlay:
                self.currentPlayStack.append(playerCombo)
                self.playerTurn.discardCard(playerCombo.getCards())

                if len(self.playerTurn.getHand()) == 0:
                    self.winner = self.playerTurn
                    print(f"Winner is {self.winner.getName()}!")
                    return

                if self.playerIndex == 3:
                    self.playerIndex = 0
                else:
                    self.playerIndex += 1
                self.playerTurn = self.players[self.playerIndex]
                roundNum += 1
            else:
                continue

    def isBiggerSingleOrPairOrTriple(self, currentPlayCombo, playerCombo):
        sortedCurrentCombo = self.sortBySuit(currentPlayCombo)
        sortedPlayerCombo = self.sortBySuit(playerCombo)

        currentPlayComboNumber = sortedCurrentCombo[-1].getNumber()
        playerComboNumber = sortedPlayerCombo[-1].getNumber()

        currentPlayComboSuit = sortedCurrentCombo[-1].getSuit()
        playerComboSuit = sortedPlayerCombo[-1].getSuit()

        if currentPlayComboNumber > playerComboNumber:
            return False
        elif currentPlayComboNumber < playerComboNumber:
            return True
        else:
            if self.suitRanks[currentPlayComboSuit] > self.suitRanks[playerComboSuit]:
                return False
            elif self.suitRanks[currentPlayComboSuit] < self.suitRanks[playerComboSuit]:
                return True
        
    def sortBySuit(self, combo):
        cardsList = combo.getCards()
        cardsList.sort(key=lambda card: self.suitRanks[card.getSuit()])
        return cardsList

    def isBiggerStraightOrStriaghtFlush(self, currentPlayCombo, playerCombo):
        sortedCurrentCombo = self.sortBySuit(currentPlayCombo)
        sortedPlayerCombo = self.sortBySuit(playerCombo)

        currentPlayComboNumber = sortedCurrentCombo[-1].getNumber()
        playerComboNumber = sortedPlayerCombo[-1].getNumber()

        currentPlayComboSuit = sortedCurrentCombo[-1].getSuit()
        playerComboSuit = sortedPlayerCombo[-1].getSuit()

        if currentPlayComboNumber < playerComboNumber:
            return True
        elif currentPlayComboNumber > playerComboNumber:
            return False
        else:
            return currentPlayComboSuit < playerComboSuit
    
    def isBiggerFullHouse(self, currentPlayCombo, playerCombo):
        currentTripleNum = self.getTripleNumber(currentPlayCombo.getCards())
        playerTripleNum = self.getTripleNumber(playerCombo.getCards())
        return currentTripleNum < playerTripleNum
    
    def getTripleNumber(self, cards):
        counts = {}
        for card in cards:
            counts[card.getNumber()] = counts.get(card.getNumber(), 0) + 1
        for number, count in counts.items():
            if count == 3:
                return number

    def isBiggerFlush(self, currentPlayCombo, playerCombo):
        currentComboSuit = currentPlayCombo.getCards()[0].getSuit()
        playerComboSuit = playerCombo.getCards()[0].getSuit()
        return self.suitRanks[currentComboSuit] < self.suitRanks[playerComboSuit]

    def isBiggerDynamite(self, currentPlayCombo, playerCombo):
        currentFourNum = self.getFourOfKindNumber(currentPlayCombo.getCards())
        playerFourNum = self.getFourOfKindNumber(playerCombo.getCards())
        return currentFourNum < playerFourNum

    def getFourOfKindNumber(self, cards):
        counts = {}
        for card in cards:
            counts[card.getNumber()] = counts.get(card.getNumber(), 0) + 1
        for number, count in counts.items():
            if count == 4:
                return number