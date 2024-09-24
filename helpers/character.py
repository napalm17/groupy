import numpy as np


class Character:
    def __init__(self, value, text=None):
        """
        Initialize a Character entry with a value and an optional text representation.

        Parameters:
        value: Numeric value of the character.
        text: Optional description. If None, str(value) is used.
        """
        self.value = value
        self.text = text if text is not None else str(value)

    def __repr__(self):
        """Return the string representation of the character."""
        return self.text

    def __eq__(self, other):
        """Check equality with another Character or numeric type."""
        return isinstance(other, Character) and np.isclose(self.value, other.value)

    def __hash__(self):
        """Return the hash of the character's value."""
        return hash(self.value)

    def __lt__(self, other):
        """Check if this Character is less than another Character or numeric type."""
        return (self.value < other.value) if isinstance(other, Character) else (np.abs(self.value) < other)

    def __gt__(self, other):
        """Check if this Character is greater than another Character or numeric type."""
        return (self.value > other.value) if isinstance(other, Character) else (np.abs(self.value) > other)

    def __mul__(self, other):
        """
        Multiply this Character by another Character or a numeric type.

        Returns:
        Character: A new Character representing the product.
        """
        if isinstance(other, Character):
            result = self.value * other.value
            text = f'{self.text}·{other.text}' if not np.isclose(result, int(result)) else str(int(result))
            return Character(result, text)
        elif isinstance(other, (float, int)):
            result = self.value * other
            text = f'{other}·{self.text}' if result != int(result) else str(int(result))
            return Character(result, text)

    def __rmul__(self, other):
        """Handle multiplication from the left."""
        return self * other if isinstance(other, (float, int)) else NotImplemented
