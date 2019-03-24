import unittest
from model.cards import Card


class CardTestCase(unittest.TestCase):

    def test_create(self):
        self.assertIsNotNone(Card('Ace', 'Spades'))

    def test_different(self):
        """Cards must be different based on rank or suit"""
        first = Card('Ace', 'Spades')
        second = Card('Ace', 'Hearts')
        self.assertNotEqual(first, second)

        first = Card('Ace', 'Spades')
        second = Card('Queen', 'Spades')
        self.assertNotEqual(first, second)

    def test_equals(self):
        """Cards must be equal based on rank and suit"""
        first = Card('Ace', 'Spades')
        second = Card('Ace', 'Spades')
        self.assertIsNot(first, second)
        self.assertEqual(first, second)


if __name__ == '__main__':
    unittest.main()
