from group import Group
from helpers.algorithms import Algo
from elements.integer import IntegerMod
from dihedral import DihedralGroup


class CyclicGroup(Group):
    def __init__(self, order: int):
        elements = [IntegerMod(i, order) for i in range(order)]
        super().__init__(elements)

    def __repr__(self):
        return f'C{self.order}={list(self.elements)}'

    def __getitem__(self, index):
        return self.sorted_elements()[index]

    def __iter__(self):
        return iter(self.sorted_elements())

    def subgroup(self, suborder: int):
        return Group({IntegerMod(i, self.order) for i in range(0, self.order, int(self.order / suborder))})

    def subgroups(self):
        return [self.subgroup(n) for n in Algo.factors(self.order)]

    def normal_subgroups(self):
        return self.subgroups()

    def sorted_elements(self):
        return sorted(self.elements, key=lambda x: x.value)

    def index(self, g):
        return self.sorted_elements().index(g)

    def conjugacy_classes(self):
        return [{g} for g in self.sorted_elements()]


c2 = CyclicGroup(2)
c4 = CyclicGroup(6)
c3 = CyclicGroup(3)

c4sub2 = c4.subgroup(2)
d2 = DihedralGroup(3)

print(d2.conjugacy_classes())
#(c2*c2).cayley_graph().plot()

