import unittest
from model.cards import StandardDeck, Card


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
        suit_cards = [c for c in StandardDeck().cards if c.suit == 'Spades']
        self.assertEqual(13, suit_cards.__len__())

    def test_num_of_hearts_cards(self):
        suit_cards = [c for c in StandardDeck().cards if c.suit == 'Hearts']
        self.assertEqual(13, suit_cards.__len__())

    def test_num_of_diamonds_cards(self):
        suit_cards = [c for c in StandardDeck().cards if c.suit == 'Diamonds']
        self.assertEqual(13, suit_cards.__len__())

    def test_num_of_clubs_cards(self):
        suit_cards = [c for c in StandardDeck().cards if c.suit == 'Clubs']
        self.assertEqual(13, suit_cards.__len__())

    def test_spades_has_all_ranks(self):
        suit_cards = [c for c in StandardDeck().cards if c.suit == 'Spades']
        self.check_suit_cards_complete(suit_cards, 'Spades')

    def test_hearts_has_all_ranks(self):
        suit_cards = [c for c in StandardDeck().cards if c.suit == 'Hearts']
        self.check_suit_cards_complete(suit_cards, 'Hearts')

    def test_diamonds_has_all_ranks(self):
        suit_cards = [c for c in StandardDeck().cards if c.suit == 'Diamonds']
        self.check_suit_cards_complete(suit_cards, 'Diamonds')

    def test_clubs_has_all_ranks(self):
        suit_cards = [c for c in StandardDeck().cards if c.suit == 'Clubs']
        self.check_suit_cards_complete(suit_cards, 'Clubs')

    def check_suit_cards_complete(self, suit_cards, suit):
        self.assertTrue(suit_cards.__contains__(Card('A', suit)))
        self.assertTrue(suit_cards.__contains__(Card('2', suit)))
        self.assertTrue(suit_cards.__contains__(Card('3', suit)))
        self.assertTrue(suit_cards.__contains__(Card('4', suit)))
        self.assertTrue(suit_cards.__contains__(Card('5', suit)))
        self.assertTrue(suit_cards.__contains__(Card('6', suit)))
        self.assertTrue(suit_cards.__contains__(Card('7', suit)))
        self.assertTrue(suit_cards.__contains__(Card('8', suit)))
        self.assertTrue(suit_cards.__contains__(Card('9', suit)))
        self.assertTrue(suit_cards.__contains__(Card('10', suit)))
        self.assertTrue(suit_cards.__contains__(Card('Q', suit)))
        self.assertTrue(suit_cards.__contains__(Card('J', suit)))
        self.assertTrue(suit_cards.__contains__(Card('K', suit)))


if __name__ == '__main__':
    unittest.main()
