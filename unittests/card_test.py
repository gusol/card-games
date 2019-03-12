import unittest
from model import deck


class CardTestCase(unittest.TestCase):

    def test_create(self):
        self.assertIsNotNone(deck.Card('Ace', 'Spades'))

    def test_different(self):
        first = deck.Card('Ace', 'Spades')
        second = deck.Card('Ace', 'Hearts')
        self.assertNotEqual(first, second)

        first = deck.Card('Ace', 'Spades')
        second = deck.Card('Queen', 'Spades')
        self.assertNotEqual(first, second)

    def test_equals(self):
        first = deck.Card('Ace', 'Spades')
        second = deck.Card('Ace', 'Spades')
        self.assertIsNot(first, second)
        self.assertEqual(first, second)


if __name__ == '__main__':
    unittest.main()
