import random


class DisplayCard:
    """Generates a random card between 1 to 13
    """

    def __init__(self):
        self.card_number = 0

    def drawn(self):
        """Draws a new card between 1 and 13, and return the number of the card.
        """
        self.card_number = random.randint(1, 13)
        return self.card_number