from helpers import Utility


class UnitQuaternion:
    def __init__(self, i: int, j: bool, n: int, sgn: int=1):
        assert 0 <= i <= n
        self.i = i
        self.j = j
        self.n = n
        self.sgn = sgn

    def __repr__(self):
        return self.sgn_str() + self.i_str() + self.j_str()

    def __mul__(self, other: 'UnitQuaternion'):
        assert self.n == other.n
        new_i, new_j = (self.i - other.i, not other.j) if self.j else (self.i + other.i, other.j)
        new_sgn = self.sgn * other.sgn * (-1) ** ((new_i < 0) ^ other.j if self.j else new_i >= self.n)
        return UnitQuaternion(abs(new_i) % self.n, new_j, self.n, new_sgn)

    def __eq__(self, other: 'UnitQuaternion'):
        return (self.i, self.j, self.sgn, self.n) == (other.i, other.j, other.sgn, other.n)

    def __hash__(self):
        return hash((self.i, self.j, self.sgn, self.n))

    def __lt__(self, other: 'UnitQuaternion'):
        return (self.j, self.i, other.sgn) < (other.j, other.i, self.sgn)

    def name(self):
        return 'Dc' + str(self.n).translate(Utility.SUBSCRIPT_MAP)

    def j_str(self):
        return 'j' if self.j else ''

    def i_str(self):
        if not self.i:
            return ''
        return 'i' if self.i == 1 else f'i{Utility.to_superscript(self.i)}'

    def sgn_str(self):
        if self.i == self.j == 0:
            return str(self.sgn)
        return '' if self.sgn == 1 else '-'

j = UnitQuaternion(0, True, 8, 1)
i = UnitQuaternion(1, False, 8, 1)

#elements = sorted(Group.generate_from({i, j}))

#print(elements, len(elements))