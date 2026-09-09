class TestBigTwo:

    def setup_method(self):
        deck = Deck()
        player1Name = input("What's player 1's name: ")
        player2Name = input("What's player 2's name: ")
        player3Name = input("What's player 3's name: ")
        player4Name = input("What's player 4's name: ")

        player1Hand = deck.getPlayer1Hand()
        player2Hand = deck.getPlayer2Hand()
        player3Hand = deck.getPlayer3Hand()
        player4Hand = deck.getPlayer4Hand()
        
        player1 = Player(player1Name, player1Hand)
        player2 = Player(player2Name, player2Hand)
        player3 = Player(player3Name, player3Hand)
        player4 = Player(player4Name, player4Hand)

        game = BigTwo(deck, player1, player2, player3, player4)