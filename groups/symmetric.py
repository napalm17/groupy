from group import Group
import itertools
from elements.permutation import PermutationArray


class SymmetricGroup(Group):
    def __init__(self, n: int):
        """
        Initialize a symmetric group of order n.

        Parameters:
        n (int): The index of the symmetric group.
        """

        elements = list(itertools.permutations(range(1, n + 1, 1)))
        perms = [PermutationArray(sigma) for sigma in elements]
        super().__init__(perms)
        self.n = n

    def __repr__(self):
        return f'S{self.n}={self.elements}'


    def alternating_group(self):
        return self.commutator_subgroup()


S4 = SymmetricGroup(4)
#S4.subgroup_lattice()