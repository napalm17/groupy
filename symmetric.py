from group import Group
from operations import perm_composition
import itertools
from permutation import PermutationArray


class SymmetricGroup(Group):
    def __init__(self, n: int):
        elements = list(itertools.permutations(range(1, n + 1, 1)))
        perms = [PermutationArray(sigma) for sigma in elements]
        super().__init__(perms)
        self.n = n

    def __repr__(self):
        return f'S{self.n}={self.elements}'

    def alternating_group(self):
        return self.commutator_subgroup()

S3 = SymmetricGroup(3)
A3 = S3.alternating_group()

print(S3.quotient_group(A3).is_group())