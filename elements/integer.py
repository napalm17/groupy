from helpers import add_mod_n


class IntegerMod:
    def __init__(self, value, n):
        self.value = value % n
        self.n = n

    def __mul__(self, other: 'IntegerMod'):
        if self.n == other.n:
            value = add_mod_n(self.n)(self.value, other.value)
            return IntegerMod(value, self.n)
        return None

    def __repr__(self):
        return f'{self.value}'

    def __eq__(self, other: 'IntegerMod'):
        return (self.value == other.value) and (self.n == other.n)

    def __hash__(self):
        return hash((self.value, self.n))

    def __pow__(self, power, modulo=None):
        result = IntegerMod(self.value, self.n)
        for _ in range(power - 1):
            result *= self
        return result

    def __lt__(self, other: 'IntegerMod'):
        return self.value < other.value

    def __gt__(self, other: 'IntegerMod'):
        return self.value > other.value
