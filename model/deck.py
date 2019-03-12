class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Card):
            return self.rank == other.rank and self.suit == other.suit
        return False


if __name__ == '__main__':
    pass
