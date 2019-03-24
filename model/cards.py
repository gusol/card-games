class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        """Overrides the default implementation"""
        return isinstance(other, Card) \
            and self.rank == other.rank \
            and self.suit == other.suit


class StandardDeck:
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    _size = 52

    def __init__(self):
        self.cards = []
        StandardDeck.fill_suit('Spades', self.cards)
        StandardDeck.fill_suit('Hearts', self.cards)
        StandardDeck.fill_suit('Diamonds', self.cards)
        StandardDeck.fill_suit('Clubs', self.cards)

    @staticmethod
    def fill_suit(suit, cards):
        cards.append(Card('A', suit))
        for i in range(2, 11):
            cards.append(Card(str(i), suit))
        cards.append(Card('Q', suit))
        cards.append(Card('J', suit))
        cards.append(Card('K', suit))


if __name__ == '__main__':
    pass
