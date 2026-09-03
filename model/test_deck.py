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
        # print(self.deck1.getDeck())
        assert self.deck1.getDeck()
        assert len(self.deck1.getDeck()) == 52
    
    def test_shuffle(self):
        print(self.deck1)
        preShuffleDeck = self.deck1.getDeck()
        self.deck1.shuffle()
        print(self.deck1.getDeck())
        assert self.deck1 != preShuffleDeck

    def test_deal(self):
        self.deck1.shuffle()
        self.deck1.deal()
        assert len(self.deck1.getPlayer1Hand()) == 13
        assert len(self.deck1.getPlayer2Hand()) == 13
        assert len(self.deck1.getPlayer3Hand()) == 13
        assert len(self.deck1.getPlayer4Hand()) == 13
    
    
