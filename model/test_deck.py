# tests for deck
from deck import Deck

'''
    pytest
    pytest -s
    pytest -v -s
    pytest test_deck.py -v -s

    -s shows any print functions
    -v shows each test name whether they were passed or failed
'''

class TestDeck:

    def setup_method(self):
        self.deck1 = Deck()

    def test_getDeck(self):
        print("deck of cards")
        print(self.deck1.getDeck())
        assert self.deck1.getDeck()