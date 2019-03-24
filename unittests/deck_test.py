import unittest
from model.cards import StandardDeck


class StandardDeckTestCase(unittest.TestCase):

    def test_create(self):
        self.assertIsNotNone(StandardDeck())

    def test_num_of_cards(self):
        self.assertEqual(52, StandardDeck().cards.__len__())

    def test_num_of_suits(self):
        self.assertEqual(4, StandardDeck.suits.__len__())

    def test_has_all_suits(self):
        self.assertTrue(StandardDeck().suits.__contains__('Spades'))
        self.assertTrue(StandardDeck().suits.__contains__('Hearts'))
        self.assertTrue(StandardDeck().suits.__contains__('Diamonds'))
        self.assertTrue(StandardDeck().suits.__contains__('Clubs'))

    def test_num_of_spades_cards(self):
        self.validate_suit_cards_num('Spades')

    def test_num_of_hearts_cards(self):
        self.validate_suit_cards_num('Hearts')

    def test_num_of_diamonds_cards(self):
        self.validate_suit_cards_num('Diamonds')

    def test_num_of_clubs_cards(self):
        self.validate_suit_cards_num('Clubs')

    def validate_suit_cards_num(self, suit):
        suit_cards = [c for c in StandardDeck().cards if c.suit == suit]
        self.assertEqual(13, suit_cards.__len__())


if __name__ == '__main__':
    unittest.main()
