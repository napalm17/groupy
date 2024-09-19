from group import Group
import numpy as np
import cmath
import math
import matplotlib.pyplot as plt
from elements.unit_complex import UnitComplex
import numpy as np
from groups.cyclic import CyclicGroup


class U1(Group):
    def __init__(self, size):
        self.size = size
        self.resolution = 2 * np.pi / size
        self.angles = np.arange(0, 2*np.pi, self.resolution)
        elements = [UnitComplex(theta, self.resolution) for theta in self.angles]
        super().__init__(elements)
        #self.order = math.inf

    def __repr__(self):
        return f'{self.elements}'



u1 = U1(4)
print(u1.commutator_subgroup())
print(u1 == CyclicGroup(4))

