from random import randint


class Die:
    """A class representing a single die.
    """

    def __init__(self, num_sides=6):
        """Assume a six-sided die.ult 6
        """
        self.num_sides = num_sides

    def roll(self):
        """Return a random number value between 1 and number of sides.
        """
        return randint(1, self.num_sides)

    def __str(self):
        """Get a text representation for the die
        """
        return f"D{self.num_sides}"

    __str__ = __str
    __repr__ = __str
