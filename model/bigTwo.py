class BigTwo():

    def __init__(self, deck, player1, player2, player3, player4):
        self.players = [player1, player2, player3, player4]
        self.deck = deck
        self.currentPlayStack = [] # list of combo lists Played objects
        self.winner = None
        self.playerTurn = None
        self.playerIndex = None

'''
        self.whosTurn = random.choice(self.players)
        
        index = self.players.indexOf(self.whosTurn)
        self.playerIndex = index
        if self.playerIndex + 1 > len(self.players):
            self.whosNext = self.players[0]
        else:
            self.playerIndex += 1
            self.whosNext = self.players[self.playerIndex]
'''

        
        self.suitRanks = {
            "diamond" = 1
            "clover" = 2
            "heart" = 3
            "spade" = 4
        }

        # key = type of combo
        # value = [list of combos that can beat the key which is the type of combo]
        self.heigharchyCombos = {
            "Single": ["Single"],
            "Pair": ["Pair"],
            "Triple": ["Triple"],
            "Striaght": ["Straight", "Flush", "Straight Flush", "Full House", "Dynamite"]
            "Flush": ["Flush", "Straight Flush", "Full House", "Dynamite"]
            "Full House":["Full House", "Striaght Flush", "Dynamite"]
            "Straight Flush": ["Straight Flush", "Dynamite"]
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

    def play(self):
        self.deck.shuffle()

        # Dealing cards to players
        dealToPlayerIndex = 0
        for card in self.deck:
            self.players[dealToPlayerIndex].addToHand(card)
            # figure out who has diamond 3
            if card.getNumber() == 3 and card.getSuit() == "diamonds":
                self.playerTurn = self.players[dealToPlayerIndex]
                self.playerIndex = dealToPlayerIndex
            dealToPlayerIndex += 1
            if dealToPlayerIndex == 4:
                dealToPlayerIndex = 0

        # check who goes first
        # Keep track of first round/turn
        roundNum = 1
        while True:
            if roundNum == 1:
                playerCombo = self.playerTurn.play()
                has_diamond3 = any(card.getNumber() == 3 and card.getSuit() == "diamond" for card in playedCombo.getCards())
                if not has_diamond3:
                    print("Must play diamond 3!")
                    pass
            else:
                if self.playerIndex == 5:
                    self.playerIndex = 0
                
                # Combos to compare and identify which combo is bigger and if
                # player's combo is a valid play
                currentPlayCombo = self.currentPlayStack[-1]
                playerCombo = self.playerTurn.play()

                # Check if Singles only play
                if currentPlayCombo.getComboName() == "Single" and playerCombo.getComboName() == "Single":
                    if self.isBiggerSingle(currentPlayCombo, playerCombo):
                        print("Valid play! Your card is bigger\n")
                    else:
                        print("Your card is not bigger\n")
                        pass


            self.currentPlayStack.append(playerCombo)
            self.playerIndex += 1
            self.playerTurn = self.players[self.playerIndex]


                    
    # Returns true or false whether the player's single combo is
    # bigger than the previous played single combo
    def isBiggerSingle(self, currentPlayCombo, playerCombo):

        # is player's single card bigger than previous played card
        currentPlayComboNumber = currentPlayCombo.getCards()[-1].getNumber()
        playerComboNumber = playerCombo.getCards()[-1].getNumber()

        currentPlayComboSuit = currentPlayCombo.getCards()[-1].getSuit()
        playerComboSuit = playerCombo.getCards()[-1].getSuit()

        if currentPlayComboNumber > playerComboNumber:
            print("Your card is not bigger\n")
            return False
        elif currentPlayComboNumber < playerComboNumber:
            print("Valid play! Your card's number is bigger\n")
            self.currentPlayStack.append(playerCombo)
            return True
        else: # when both cards are the same number
            if self.suitRanks[currentPlayCombo] > self.suitRanks[playerCombo]:
                print("Your card is not bigger\n")
                return False
            elif self.suitRanks[currentPlayCombo] < self.suitRanks[playerCombo]
                print("Valid play! Your card's suit is bigger\n")
                self.currentPlayStack.append(playerCombo)
                return True
            
    def appendAndDiscard(self, player, card):
        self.currentPlayStack.append(card)
        player.discardCard(card)

    def isPair(self, carad1, card2):
        return card1.getNumber() == card2.getNumber()

    def isBiggestPair(self, card1, card2):
        # [card1, card2]
        self.currentPlayStack[-1]
        if isPair and 

