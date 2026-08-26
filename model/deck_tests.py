# tests for deck
from deck import Deck
class TestDeck:

    def setup_method(self):
        self.deck1 = Deck()

    def test_getDeck(self):
        assert self.deck1.getDeck()