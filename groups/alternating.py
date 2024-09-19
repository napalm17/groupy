from group import Group
from groups.symmetric import SymmetricGroup

class AlternatingGroup(Group):
    def __init__(self, n: int):
        elements = SymmetricGroup(n).commutator_subgroup().elements
        super().__init__(elements)
        self.n = n

    def __repr__(self):
        return f'S{self.n}={self.elements}'


A4 = AlternatingGroup(3)
print(A4)