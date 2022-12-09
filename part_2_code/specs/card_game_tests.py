import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card('Hearts', 10)
        self.card2 = Card('Clubs', 5)
        self.card3 = Card('Spade', 6)
        self.card4 = Card('Diamonds', 7)
        self.card5 = Card('Clubs', 1)

    def test_card_has_suit(self):
        self.assertEqual('Hearts', self.card1.suit)

    def test_card_has_value(self):
        self.assertEqual(5, self.card2.value)

    def test_check_for_ace_true(self):
        card = self.card5
        self.assertEqual(True, CardGame.check_for_ace(self, card))

    def test_check_for_ace_false(self):
        card = self.card3
        self.assertEqual(False, CardGame.check_for_ace(self, card))

    def test_highest_card_is_card1(self):
        card1 = self.card1
        card2 = self.card2
        self.assertEqual(self.card1, CardGame.highest_card(self, card1, card2))

    def test_highest_card_is_card2(self):
        card1 = self.card2
        card2 = self.card3
        self.assertEqual(self.card3, CardGame.highest_card(self, card1, card2))

    def test_cards_total(self):
        cards = [self.card1, self.card2]
        expected_output = "You have a total of 15"
        actual_output = CardGame.cards_total(self, cards)
        self.assertEqual(expected_output, actual_output)
