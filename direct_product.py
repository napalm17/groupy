
class DirectProduct:
    def __init__(self, element1, element2):
        self.element1 = element1
        self.element2 = element2

    def __repr__(self):
        return f'({self.element1}, {self.element2})'

    def __mul__(self, other: 'DirectProduct'):
        return DirectProduct(self.element1 * other.element1, self.element2 * other.element2)

    def __eq__(self, other: 'DirectProduct'):
        return self.element1 == other.element1 and self.element2 == other.element2

    def __hash__(self):
        return hash((self.element1, self.element2))

    def __lt__(self, other):
        return (self.element1, self.element2) < (other.element1, other.element2)

    def __gt__(self, other):
        return (self.element1, self.element2) > (other.element1, other.element2)





