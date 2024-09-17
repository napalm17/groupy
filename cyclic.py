from group import Group
from operations import add_mod_n
from algorithms import Algo
from integer import IntegerMod
from operations import bijection
import math
from map import Map
from bijection import Bijection
from dihedral import DihedralGroup

class CyclicGroup(Group):
    def __init__(self, order: int):
        elements = {IntegerMod(i, order) for i in range(order)}
        super().__init__(elements)

    def __repr__(self):
        return f'C{self.order}={list(self.elements)}'

    def __getitem__(self, index):
        return self.sorted()[index]

    def __iter__(self):
        return iter(self.sorted())

    def subgroup(self, suborder: int):
        return Group({IntegerMod(i, self.order) for i in range(0, self.order, int(self.order / suborder))})

    def subgroups(self):
        return [self.subgroup(n) for n in Algo.factors(self.order)]

    def normal_subgroups(self):
        return self.subgroups()

    def sorted(self):
        return sorted(self.elements, key=lambda x: x.value)

    def index(self, g):
        return self.sorted().index(g)


c2 = CyclicGroup(2)
c4 = CyclicGroup(4)
c4sub2 = c4.subgroup(2)
d2 = DihedralGroup(2)
print(d2)
print(c2 * c2 == c4)
#print(any(Bijection(c2, c4sub2, m).is_isomorphism() for m in range(1, math.factorial(c2.order) + 1)))