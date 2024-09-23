import numpy as np
from helpers.utils import Utility
from helpers.character import Character


class RoU:
    def __init__(self, n, power):
        self.n = n
        self.power = power
        self.value = np.round(np.exp(2j * np.pi * power / n), 5)
        self.text = Utility.format_root_of_unity(n, power)

    def __repr__(self):
        return '1' if self.power % self.n == 0 else self.text

    def __add__(self, other: 'RoU'):
        result = self.value + other.value
        return Character(result, str(int(result.real)) if result == int(result.real) else f'{self}+{other}')