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
        # check who goes first
        # Keep track of first round/turn
        roundNum = 1
        newRound = False
        playerCombo = None
        while True:
            if len(self.currentPlayStack) != 0:
                print("Previously played:")
                for card in self.currentPlayStack[-1].getCards():
                    print(card.getName())

            if roundNum == 1:
                playerCombo = self.playerTurn.play()
                if playerCombo is None:
                    print("You must play a valid combo containing the 3 of diamonds!")
                    continue
                has_diamond3 = any(card.getNumber() == 3 and card.getSuit() == "diamonds" for card in playerCombo.getCards())
                if not has_diamond3:
                    print("Must play diamond 3!")
                    continue
                else:
                    self.currentPlayStack.append(playerCombo)          
                    self.playerTurn.discardCard(playerCombo.getCards()) 
                    if self.playerIndex == 3:
                        self.playerIndex = 0
                    else:
                        self.playerIndex += 1
                    self.playerTurn = self.players[self.playerIndex]
                    roundNum += 1
                    continue
                
            # clear
            playerCombo = self.playerTurn.play()
            if playerCombo is None:
                # player passed (or made an invalid play that returned None)
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

            if self.playerIndex == 5:
                self.playerIndex = 0

            if len(self.currentPlayStack) == 0:
                self.currentPlayStack.append(playerCombo)
                self.playerTurn.discardCard(playerCombo.getCards())
                # update to next player's turn
                if self.playerIndex == 3:
                    self.playerIndex = 0
                else:
                    self.playerIndex += 1
                self.playerTurn = self.players[self.playerIndex]
                pass
            
            
            # Combos to compare and identify which combo is bigger and if
            # player's combo is a valid play
            currentPlayCombo = self.currentPlayStack[-1]
            isValidPlay = False
            # Check if Singles only play
            if currentPlayCombo.getComboName() == "Single" and playerCombo.getComboName() == "Single":
                if self.isBiggerSingleOrPairOrTriple(currentPlayCombo, playerCombo):
                    print("Valid play! Your card is bigger\n")
                    isValidPlay = True
                else:
                    print("Your card is not bigger\n")
                    pass
            elif currentPlayCombo.getComboName() == "Pair" and playerCombo.getComboName() == "Pair":
                if self.isBiggerSingleOrPairOrTriple(currentPlayCombo, playerCombo):
                    print("Valid play! Your pair is bigger\n")
                    isValidPlay = True
                else:
                    print("Your pair is not bigger\n")
                    pass
            elif currentPlayCombo.getComboName() == "Triple" and playerCombo.getComboName() == "Triple":
                if self.isBiggerSingleOrPairOrTriple(currentPlayCombo, playerCombo):
                    print("Valid play! Your triple is bigger\n")
                    isValidPlay = True
                else:
                    print("Your triple is not bigger\n")
                    pass
            elif currentPlayCombo.getComboName() == "Straight" and playerCombo.getComboName() == "Straight":
                if self.isBiggerStraightOrStriaghtFlush(currentPlayCombo, playerCombo):
                    print("Valid play! Your straight is bigger\n")
                    isValidPlay = True
                else:
                    print("Your straight is not bigger\n")
                    pass
            elif currentPlayerCombo.getComboName() == "Straight Flush" and playerCombo.getComboName() == "Straight Flush":
                if self.isBiggerStraightOrStriaghtFlush(currentPlayCombo, playerCombo):
                    print("Valid play! Your straight flush is bigger\n")
                    isValidPlay = True
                else:
                    print("Your straight flush is smaller\n")
                    pass
            elif currentPlayerCombo.getComboName() == "Full House" and playerCombo.getComboName() == "Full House":
                if self.isBiggerFullHouse(currentPlayCombo, playerCombo):
                    print("Valid play! Your full house is bigger\n")
                    isValidPlay = True
                else:
                    print("Your full house is smaller\n")
                    pass
            elif currentPlayerCombo.getComboName() == "Flush" and playerCombo.getComboName() == "Flush":
                if self.isBiggerFlush(currentPlayCombo, playerCombo):
                    print("Valid play! Your flush is bigger\n")
                    isValidPlay = True
                else:
                    print("Your flush is smaller\n")
                    pass
            elif currentPlayerCombo.getComboName() == "Dynamite" and playerCombo.getComboName() == "Dynamite":
                if self.isBiggerDynamite(currentPlayCombo, playerCombo):
                    print("Valid play! Your dynamite is bigger\n")
                    isValidPlay = True
                else:
                    print("Your dynamite is smaller\n")
                    pass
            elif currentPlayerCombo.getComboName() == "Straight" and playerCombo.getComboName() in self.heigharchyCombos["Straight"]:
                print("Valid play! Your combo is bigger")
                isValidPlay = True
            elif currentPlayerCombo.getComboName() == "Flush" and playerCombo.getComboName() in self.heigharchyCombos["Flush"]:
                print("Valid play! Your combo is bigger")
                isValidPlay = True
            elif currentPlayerCombo.getComboName() == "Full House" and playerCombo.getComboName() in self.heigharchyCombos["Full House"]:
                print("Valid play!. Your combo is bigger")
                isValidPlay = True
            elif currentPlayerCombo.getComboName() == "Dynamite" and playerCombo.getComboName() in self.heigharchyCombos["Dynamite"]:
                print("Valid play!. Your combo is bigger")
                isValidPlay = True
            else:
                pass

            roundNum += 1

            if isValidPlay:
                self.currentPlayStack.append(playerCombo)
                self.playerTurn.discardCard(playerCombo.getCards())
                if self.playerIndex == 3:
                    self.playerIndex = 0
                else:
                    self.playerIndex += 1
                self.playerTurn = self.players[self.playerIndex]
                roundNum += 1
            else:
                continue

        self.currentPlayStack.append(playerCombo)
        # bigTwo.py — both call sites
        self.playerTurn.discardCard(playerCombo.getCards())
        # update to next player's turn
        self.playerIndex += 1
        self.playerTurn = self.players[self.playerIndex]
        for player in Players:
            if len(player.getHand()) == 0:
                self.winner = player
                break
        print("Winner is", self.winner.getName(), "!")

    def isBiggerSingleOrPairOrTriple(self, currentPlayCombo, playerCombo):
        sortedCurrentCombo = self.sortBySuit(currentPlayCombo)
        sortedPlayerCombo = self.sortBySuit(playerCombo)

        currentPlayComboNumber = sortedCurrentCombo[-1].getNumber()
        playerComboNumber = sortedPlayerCombo[-1].getNumber()

        currentPlayComboSuit = sortedCurrentCombo[-1].getSuit()
        playerComboSuit = sortedPlayerCombo[-1].getSuit()

        if currentPlayComboNumber > playerComboNumber:
            print("Your card is not bigger\n")
            return False
        elif currentPlayComboNumber < playerComboNumber:
            print("Valid play! Your card's number is bigger\n")
            return True
        else:
            if self.suitRanks[currentPlayComboSuit] > self.suitRanks[playerComboSuit]:
                print("Your card is not bigger\n")
                return False
            elif self.suitRanks[currentPlayComboSuit] < self.suitRanks[playerComboSuit]:
                print("Valid play! Your card's suit is bigger\n")
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
        # 3 3 3 4 4
        # 5 5 6 6 6
        currentThreeTriple = Combo("Unknown", currentPlayCombo[:3])
        isCurrentThreeTriple = currentThreeTriple.isTriple()

        playerThreeTriple = Combo("Unknown", playerCombo[:3])
        isPlayerThreeTriple = playerThreeTriple.isTriple()

        if not isCurrentThreeTriple and isPlayerThreeTriple:
            currentThreeTriple = Combo("Unknown", currentPlayCombo[3:])
        elif isCurrentThreeTriple and not isPlayerThreeTriple:
            playerThreeTriple = Combo("Unknown", playerCombo[3:])
        elif not isCurrentThreeTriple and not isPlayerThreeTriple:
            currentThreeTriple = Combo("Unknown", currentPlayCombo[3:])
            playerThreeTriple = Combo("Unknown", playerCombo[3:])
        return isBiggerSingleOrPairOrTriple(currentThreeTriple, playerThreeTriple)
    
    def isBiggerFlush(self, currentPlayCombo, playerCombo):

        currentComboSuit = currentPlayCombo[0].getSuit()
        playerComboSuit = playerCombo[0].getSuit()

        return self.suitRanks[currentComboSuit] < self.suitRanks[playerComboSuit]

    def isBiggerDynamite(self, currentPlayCombo, playerCombo):
        
        currentDynamite = Combo("Unknown", currentPlayCombo[:4])
        playerDynamite = Combo("Unkown", playerCombo[:4])

        isFirstFourCurrentDynamite = currentDynamite.isDynamite()
        isFirstFourPlayerDynamite = playerDynamite.isDynamite()

        if isFirstFourCurrentDynamite and not isFirstFourPlayerDynamite:
            playerDynamite = Combo("Unkown", playerPlayCombo[1:])
        elif not isFirstFourCurrentDynamite and isFirstFourPlayerDynamite:
            currentDynamite = Combo("Unknown", currentPlayCombo[1:])
        elif not isFirstFourCurrentDynamite and not isFirstFourCurrentDynamite:
            playerDynamite = Combo("Unkown", playerPlayCombo[1:])
            currentDynamite = Combo("Unknown", currentPlayCombo[1:])
        return currentDynamite[0].getNumber() < playerDynamite[0].getNumber()