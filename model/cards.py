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
        for i in range(0, StandardDeck._size // self.suits.__len__()):
            card = Card(0, 'Spades')
            self.cards.append(card)

        for i in range(0, StandardDeck._size // self.suits.__len__()):
            card = Card(0, 'Hearts')
            self.cards.append(card)

        for i in range(0, StandardDeck._size // self.suits.__len__()):
            card = Card(0, 'Diamonds')
            self.cards.append(card)

        for i in range(0, StandardDeck._size // self.suits.__len__()):
            card = Card(0, 'Clubs')
            self.cards.append(card)


if __name__ == '__main__':
    pass
