from player import Player
from card import Card
from combo import Combo

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

        pairsCards = [
            Card(2, "spade"), Card(2, "heart"),
            Card(5, "diamond"), Card(5, "clover"),
            Card(7, "spade"), Card(7, "diamond"),
            Card(9, "heart"), Card(9, "clover"),
            Card(11, "spade"), Card(11, "diamond"),
            Card(13, "heart"), Card(13, "clover"),
        ]

        tripleCards = [
            Card(4, "diamond"), Card(4, "spade"), Card(4, "clover"),   # triple of 4s
            Card(2, "spade"),
            Card(3, "heart"),
            Card(6, "clover"),
            Card(7, "diamond"),
            Card(8, "spade"),
            Card(9, "heart"),
            Card(10, "clover"),
            Card(11, "diamond"),
            Card(12, "spade"),
            Card(14, "heart"),
        ]

        straightCards = [
            Card(5, "diamond"), Card(6, "clover"), Card(7, "spade"), Card(8, "heart"), Card(9, "diamond"),  # straight 5-9
            Card(2, "spade"),
            Card(3, "heart"),
            Card(11, "clover"),
            Card(12, "diamond"),
            Card(13, "spade"),
            Card(14, "heart"),
            Card(4, "clover"),
            Card(10, "diamond"),
        ]

        flushCards = [
            Card(2, "spade"), Card(5, "spade"), Card(8, "spade"), Card(11, "spade"), Card(14, "spade"),  # flush - all spades
            Card(3, "heart"),
            Card(4, "diamond"),
            Card(6, "clover"),
            Card(7, "heart"),
            Card(9, "diamond"),
            Card(10, "clover"),
            Card(12, "heart"),
            Card(13, "diamond"),
        ]

        straightFlushCards = [
            Card(3, "diamond"), Card(4, "diamond"), Card(5, "diamond"), Card(6, "diamond"), Card(7, "diamond"),  # straight flush
            Card(2, "spade"),
            Card(9, "heart"),
            Card(10, "clover"),
            Card(11, "spade"),
            Card(12, "heart"),
            Card(13, "clover"),
            Card(14, "spade"),
            Card(8, "heart"),
        ]

        fullHouseCards = [
            Card(6, "diamond"), Card(6, "clover"), Card(6, "spade"), Card(9, "heart"), Card(9, "clover"),  # full house - triple 6s, pair 9s
            Card(2, "spade"),
            Card(3, "heart"),
            Card(4, "diamond"),
            Card(5, "clover"),
            Card(7, "spade"),
            Card(10, "diamond"),
            Card(12, "heart"),
            Card(14, "clover"),
        ]

        dynamiteCards = [
            Card(8, "diamond"), Card(8, "clover"), Card(8, "spade"), Card(8, "heart"), Card(10, "clover"),  # dynamite - four 8s + 10
            Card(2, "spade"),
            Card(3, "heart"),
            Card(4, "diamond"),
            Card(5, "clover"),
            Card(6, "spade"),
            Card(9, "heart"),
            Card(12, "diamond"),
            Card(14, "clover"),
        ]

        self.player1 = Player("Bob", cards)
        self.player2 = Player("Billy", cards)
        self.player3 = Player("Tom", cards)
        self.player4 = Player("Rachael", pairsCards)
        self.player5 = Player("Timmy", tripleCards)
        self.player6 = Player("Jay", straightCards)
        self.player7 = Player("Luke", flushCards)
        self.player8 = Player("May", straightFlushCards)
        self.player9 = Player("George", fullHouseCards)
        self.player10 = Player("Bill", dynamiteCards)

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
    
    def test_play(self):
        singleCombo = Combo("Single", [Card(2, "spade")])
        pairCombo = Combo("Pair", [Card(2, "spade"), Card(2, "heart")])
        tripleCombo = Combo("Triple", [Card(4, "diamond"), Card(4, "spade"), Card(4, "clover"),])
        straightCombo = Combo("Straight", [Card(5, "diamond"), Card(6, "clover"), Card(7, "spade"), Card(8, "heart"), Card(9, "diamond")])
        flushCombo = Combo("Flush", [Card(2, "spade"), Card(5, "spade"), Card(8, "spade"), Card(11, "spade"), Card(14, "spade")])
        straightFlushCombo = Combo("Straight Flush", [Card(3, "diamond"), Card(4, "diamond"), Card(5, "diamond"), Card(6, "diamond"), Card(7, "diamond")])
        fullHouseCombo = Combo("Full House", [Card(6, "diamond"), Card(6, "clover"), Card(6, "spade"), Card(9, "heart"), Card(9, "clover")])
        dynamiteCombo = Combo("Dynamite", [Card(8, "diamond"), Card(8, "clover"), Card(8, "spade"), Card(8, "heart"), Card(10, "clover")])

        assert self.player2.playCards([Card(2, "spade")]) == singleCombo
        assert self.player4.playCards([Card(2, "spade"), Card(2, "heart")]) == pairCombo
        assert self.player5.playCards([Card(4, "diamond"), Card(4, "spade"), Card(4, "clover")]) == tripleCombo
        assert self.player6.playCards([Card(5, "diamond"), Card(6, "clover"), Card(7, "spade"), Card(8, "heart"), Card(9, "diamond")]) == straightCombo
        assert self.player7.playCards([Card(2, "spade"), Card(5, "spade"), Card(8, "spade"), Card(11, "spade"), Card(14, "spade")]) == flushCombo
        assert self.player8.playCards([Card(3, "diamond"), Card(4, "diamond"), Card(5, "diamond"), Card(6, "diamond"), Card(7, "diamond")]) == straightFlushCombo
        assert self.player9.playCards([Card(6, "diamond"), Card(6, "clover"), Card(6, "spade"), Card(9, "heart"), Card(9, "clover")]) == fullHouseCombo
        assert self.player10.playCards([Card(8, "diamond"), Card(8, "clover"), Card(8, "spade"), Card(8, "heart"), Card(10, "clover")]) == dynamiteCombo