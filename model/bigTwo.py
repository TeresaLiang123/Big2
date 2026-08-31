class BigTwo():

    def __init__(self, deck, player1, player2, player3, player4):
        self.players = [player1, player2, player3, player4]
        self.deck = deck
        self.currentPlayStack = [] # list of combo lists Played objects
        self.winner = None
        self.whosTurn = random.choice(self.players)
        
        index = self.players.indexOf(self.whosTurn)
        self.playerIndex = index
        if self.playerIndex + 1 > len(self.players):
            self.whosNext = self.players[0]
        else:
            self.playerIndex += 1
            self.whosNext = self.players[self.playerIndex]
        
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

    7. Update who the winner is by checking who has no cards in their hand
    '''

    def play(self):

        
    
    def isBiggerSingle(self, player, card):

        # When player's card number is bigger than previous card played
        if currentPlayStack[-1].getNumber() < card.getNumber():
            # append player's card to 
            appendAndDiscard(player, card)

        # When player's card number is less than previous card played
        elif currentPlayStack[-1].getNumber() > card.getNumber()
            print("Can't play that card, your card number is smaller!")
        # When previous card played is same number
        elif currentPlayStack[-1].getNumber() == card.getNumber():
            stackCardSuit = currentPlayStack[-1].getSuit() # card previously played
            playedStackCardSuit = card.getSuit() # player's card

            prevPlayedCardSuit = self.suitRanks[stackCardSuit]
            playersCardSuit = self.suitRanks[playedStackCardSuit]

            # When player card suit is bigger than previous card played
            if prevPlayedCardSuit < playersCardSuit:
                appendAndDiscard(player, card)

            # When player card suit is smaller than previous card played
            elif prevPlayedCardSuit > playersCardSuit:
                print("Can't play that card, your card suit is smaller!")
            
    def appendAndDiscard(self, player, card):
        self.currentPlayStack.append(card)
        player.discardCard(card)

    def isPair(self, carad1, card2):
        return card1.getNumber() == card2.getNumber()

    def isBiggestPair(self, card1, card2):
        # [card1, card2]
        self.currentPlayStack[-1]
        if isPair and 

