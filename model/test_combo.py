from combo import Combo
from card import Card

class TestCombo():

    def setup_method(self):
        self.comboSingle = Combo("Single", [Card(4, "diamond")])
        self.comboPair = Combo("Pair", [Card(4, "diamond"), Card(4, "Spade")])
        self.comboTriple = Combo("Triple", [Card(4, "diamond"), Card(4, "spade"), Card(4, "clover")])
        self.comboStraight = Combo("Straight", [Card(3, "diamond"), Card(4, "clover"), Card(5, "clover"), Card(6, "spade"), Card(7, "diamond")])
        self.comboFullHouse = Combo("Full House", [Card(3, "diamond"), Card(3, "clover"), Card(3, "spade"), Card(5, "clover"), Card(5, "diamond")])
        self.comboStraightFlush = Combo("Straight Flush", [Card(3, "diamond"), Card(4, "diamond"), Card(5, "diamond"), Card(6, "diamond"), Card(7, "diamond")])
        self.comboFlush = Combo("Flush", [Card(5, "spade"), Card(4, "spade"), Card(10, "spade"), Card(6, "spade"), Card(13, "spade")])
        self.comboDynamite = Combo("Dynamite", [Card(3, "diamond"), Card(3, "clover"), Card(3, "spade"), Card(3, "heart"), Card(5, "heart")])

    def test_getComboName(self):
        assert self.comboSingle.getComboName() == "Single"
        assert self.comboPair.getComboName() == "Pair"
        assert self.comboTriple.getComboName() == "Triple"
        assert self.comboStraight.getComboName() == "Straight"
        assert self.comboFullHouse.getComboName() == "Full House"
        assert self.comboStraightFlush.getComboName() == "Straight Flush"
        assert self.comboFlush.getComboName() == "Flush"
        assert self.comboDynamite.getComboName() == "Dynamite"
    
    def test_getCards(self):
        assert self.comboSingle.getCards() == [Card(4, "diamond")]
        assert self.comboPair.getCards() == [Card(4, "diamond"), Card(4, "Spade")]
        assert self.comboTriple.getCards() == [Card(4, "diamond"), Card(4, "spade"), Card(4, "clover")]
        assert self.comboStraight.getCards() == [Card(3, "diamond"), Card(4, "clover"), Card(5, "clover"), Card(6, "spade"), Card(7, "diamond")]
        assert self.comboFullHouse.getCards() == [Card(3, "diamond"), Card(3, "clover"), Card(3, "spade"), Card(5, "clover"), Card(5, "diamond")]
        assert self.comboStraightFlush.getCards() == [Card(3, "diamond"), Card(4, "diamond"), Card(5, "diamond"), Card(6, "diamond"), Card(7, "diamond")]
        assert self.comboFlush.getCards() == [Card(5, "spade"), Card(4, "spade"), Card(10, "spade"), Card(6, "spade"), Card(13, "spade")]
        assert self.comboDynamite.getCards() == [Card(3, "diamond"), Card(3, "clover"), Card(3, "spade"), Card(3, "heart"), Card(5, "heart")]
