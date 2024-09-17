class LeftCoset:
    def __init__(self, representative, H):
        self.representative = representative
        self.H = H
        self.elements = {self.representative * h for h in self.H.elements}

    def __repr__(self):
        return f'{self.elements}'

    def __mul__(self, other: 'LeftCoset'):
        return LeftCoset(self.representative * other.representative, self.H)

    def __eq__(self, other: 'LeftCoset'):
        return self.elements == other.elements

    def __hash__(self):
        return hash(frozenset(self.elements))


class RightCoset:
    def __init__(self, representative, H):
        self.representative = representative
        self.H = H
        self.elements = {self.representative * h for h in self.H.elements}

    def __repr__(self):
        return f'{set([h * self.representative for h in self.H.elements])}'

    def __mul__(self, other: 'RightCoset'):
        return LeftCoset(self.representative * other.representative, self.H)

    def __eq__(self, other: 'LeftCoset'):
        return self.elements == other.elements

    def __hash__(self):
        return hash(frozenset(self.elements))