from card import Card

class TestCard:

    def setup_method(self):
        self.card1 = Card(2, "spade")
        self.card2 = Card(13, "diamond")

    def test_getNumber(self):
        assert self.card1.getNumber() == 2
        assert self.card2.getNumber() == 13