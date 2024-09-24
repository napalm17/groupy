from group import Group
from helpers import Algo, Character, RoU, Utility
from elements.integer import IntegerMod
import numpy as np
from vfx import Table

class CyclicGroup(Group):
    def __init__(self, order: int):
        """
        Initialize a CyclicGroup of a given order.

        Parameters:
        order (int): The order of the cyclic group.
        """
        elements = [IntegerMod(i, order) for i in range(order)]
        super().__init__(elements)

    def __repr__(self):
        return f'C{self.order}={list(self.elements)}'

    def __getitem__(self, index):
        return self.sorted_elements()[index]

    def __iter__(self):
        return iter(self.sorted_elements())

    def name(self):
        return 'C' + str(self.order).translate(Utility.SUBSCRIPT_MAP)

    def subgroup(self, suborder: int):
        """
        Initialize a CyclicGroup of a given order.

        Parameters:
        order (int): The order of the cyclic group.
        """
        return Group({IntegerMod(i, self.order) for i in range(0, self.order, int(self.order / suborder))})

    def subgroups(self, maxorder=None):
        """
        Compute all subgroups of the cyclic group up to a specified maximum order.

        Parameters:
        maxorder (int, optional): The maximum order of subgroups to compute.

        Returns:
        list: A list of subgroups.
        """

        return [self.subgroup(n) for n in Algo.factors(self.order)]

    def normal_subgroups(self):
        return self.subgroups()

    def sorted_elements(self):
        return sorted(self.elements, key=lambda x: x.value)

    def index(self, g):
        return self.sorted_elements().index(g)

    def conjugacy_classes(self):
        return [{g} for g in self.sorted_elements()]

    def character_table(self):
        """
        Compute the character table of a cyclic group of order n.
        :return: A numpy array with Character instances representing the character table.
        """
        n= self.order
        table = np.array([
            [Character(RoU(n, k*j).value, RoU(n, k*j).text)
             for j in range(n)]
            for k in range(n)
        ], dtype=object)

        return Table(table, 'Character Table of C' + str(n).translate(Utility.SUBSCRIPT_MAP))



c2 = CyclicGroup(2)
c4 = CyclicGroup(4)
c3 = CyclicGroup(3)

c4sub2 = c4.subgroup(2)

#(c2*c2*c2).subgroup_lattice()

