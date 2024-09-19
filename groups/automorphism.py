from group import Group
from maps.bijection import Bijection
import math
from groups.cyclic import CyclicGroup
from groups.symmetric import SymmetricGroup


class Aut(Group):
    def __init__(self, G: Group):
        self.G = G
        bijections = [Bijection(G, G, m) for m in range(math.factorial(G.order))]
        elements = {b for b in bijections if b.is_automorphism()}
        super().__init__(elements)

    def __repr__(self):
        return f'Aut({self.G})'

V4 = CyclicGroup(2) * CyclicGroup(2)
autc = Aut(V4)

print(autc == SymmetricGroup(3))

