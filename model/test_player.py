from player import Player
from card import Card

class TestPlayer:

    def setup_method(self):
        cards = [
            Card(2, "spade"),
            Card(3, "heart"),
            Card(5, "clover"),
            Card(8, "diamond"),
            Card(6, "spade"),
            Card(7, "heart"),
            Card(4, "diamond"),
            Card(9, "clover"),
            Card(10, "spade"),
            Card(14, "spade"),
            Card(11, "heart"),
            Card(12, "diamond"),
            Card(13, "clover"),
        ]
        self.player1 = Player("Bob", cards)
        self.player2 = Player("Billy", cards)
        self.player3 = Player("Tom", cards)

    def test_getName(self):
        assert self.player1.getName() == "Bob"
    
    def test_getPassTurn(self):
        assert self.player1.getPassTurn() == False
    
    def test_organize(self):
        sortedCardsVersion = [
            Card(2, "spade"),
            Card(3, "heart"),
            Card(4, "diamond"),
            Card(5, "clover"),
            Card(6, "spade"),
            Card(7, "heart"),
            Card(8, "diamond"),
            Card(9, "clover"),
            Card(10, "spade"),
            Card(11, "heart"),
            Card(12, "diamond"),
            Card(13, "clover"),
            Card(14, "spade"),
        ]

        organizedCards = self.player1.organize(self.player1.getHand())
        print(organizedCards)
        assert organizedCards == sortedCardsVersion
    
    def test_select(self):
        assert self.player1.select() == []
        assert self.player2.select() == [Card(2, "spade")]
        assert self.player3.select() == [Card(2, "spade"), Card(14, "spade")]
