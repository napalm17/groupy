from group import Group
from elements.rotation import RotateReflect
from helpers.root_of_unity import RoU
import numpy as np
from vfx import Table
from helpers.utils import Utility
from cyclic import CyclicGroup


class DihedralGroup(Group):
    NUM_UNIDIM_CHARS = 4

    def __init__(self, n: int):
        """
        Initialize a Dihedral group of order 2n.

        Parameters:
        n (int): The number of rotations in the dihedral group.
        """

        self.n = n
        elements = {RotateReflect(r, s, n) for s in [False, True] for r in range(n)}
        super().__init__(elements)
        self.num_conj_classes = len(self.conjugacy_classes())

    def __repr__(self):
        return f'D{self.n}={self.elements}'

    def name(self):
        return 'D' + str(self.n).translate(Utility.SUBSCRIPT_MAP)

    def character_table(self):
        """
        Compute the character table of the Dihedral group.

        Returns:
        Table: A table representing the character table of the group.
        """

        blocks = self.even_char_table() if self.n % 2 == 0 else self.odd_char_table()
        return Table(np.column_stack(blocks), f'Character Table of {self.name()}')

    def even_char_table(self):
        m = self.n // 2
        unidimensional = np.array([[(-1) ** (col % 2 and row > 1)
                                    for col in range(m + 1)]
                                   for row in range(DihedralGroup.NUM_UNIDIM_CHARS)], dtype=int)

        bidimensional = np.array([[RoU(self.n, col * row) + RoU(self.n, -col * row)
                                   for col in range(m + 1)]
                                  for row in range(1, m)], dtype=object)
        block1 = np.vstack((unidimensional, bidimensional))
        block2 = np.vstack(([[1, 1], [-1, -1], [1, -1], [-1, 1]], np.zeros(shape=(m - 1, 2)).astype(int)))
        return block1, block2

    def odd_char_table(self):
        m = self.n // 2
        unidimensional = np.ones((2, m + 1), dtype=int)
        bidimensional = np.array([[RoU(self.n, col * row) + RoU(self.n, -col * row)
                                   for col in range(m + 1)]
                                  for row in range(1, m + 1)], dtype=object)

        block1 = np.vstack((unidimensional, bidimensional))
        block2 = np.transpose([1, -1] + [0] * m)
        return block1, block2


D3 = DihedralGroup(3)
C3 = CyclicGroup(3)


#D8 = DihedralGroup(4) * D3
print((D3*C3).subgroup_lattice())
#print((c2).character_table())
