from group import Group
from symmetric import SymmetricGroup

class AlternatingGroup(Group):
    def __init__(self, n: int):
        """
        Initialize an AlternatingGroup of order n.

        Parameters:
        n (int): The degree of the symmetric group.
        """
        elements = SymmetricGroup(n).commutator_subgroup().elements
        super().__init__(elements)
        self.n = n

    def __repr__(self):
        return f'S{self.n}={self.elements}'


A4 = AlternatingGroup(3)
print(A4)