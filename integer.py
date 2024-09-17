from operations import add_mod_n


class IntegerMod:
    def __init__(self, value, n):
        self.value = value
        self.n = n
    def __mul__(self, other: 'IntegerMod'):
        if self.n == other.n:
            value = add_mod_n(self.n)(self.value, other.value)
            return IntegerMod(value, self.n)
        return None

    def __repr__(self):
        return f'{self.value}'

    def __eq__(self, other: 'IntegerMod'):
        return (self.value == other.value) and self.n == other.n

    def __hash__(self):
        return hash((self.value, self.n))

a = IntegerMod(1, 10)
b = IntegerMod(25, 10)
