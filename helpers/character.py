import numpy as np


class Character:
    def __init__(self, value, text=None):
        """
        Initialize a Character entry with a value and a text representation.

        :param value: The value of the character entry, can be a number or a matrix.
        :param text: A string that describes the character entry.
        """
        self.value = value
        self.text = text
        if text is None:
            self.text = str(self.value)

    def __repr__(self):
        return self.text

    def __eq__(self, other):
        if isinstance(other, Character):
            return np.isclose(self.value, other.value)
        return False

    def __hash__(self):
        return hash(self.value)

    def __lt__(self, other):
        if isinstance(other, Character):
            return self.value < other.value
        elif isinstance(other, float) or isinstance(other, int):
            return np.abs(self.value) < other

    def __gt__(self, other):
        if isinstance(other, Character):
            return self.value > other.value
        elif isinstance(other, float) or isinstance(other, int):
            return np.abs(self.value) > other

    def __mul__(self, other):
        if isinstance(other, Character):
            result = self.value * other.value
            text = str(int(result)) if np.isclose(result, int(result)) else f'{self.text}·{other.text}'
            if text == 'ζ₃¹·ζ₃²':
                print(result)
            return Character(result, text)
        elif isinstance(other, float) or isinstance(other, int):
            result = self.value * other
            text = str(int(result)) if result == int(result) else f'{other}·{self.text}'
            return Character(self.value * other, text)

    def __rmul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self * other
