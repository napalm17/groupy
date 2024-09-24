from group import Group
from elements.quaternion import UnitQuaternion

class Dicyclic(Group):
    def __init__(self, n: int):
        """
        Initialize a Dicyclic group of order 2n.

        Parameters:
        n (int): An integer greater than 1, representing half the order of the group.
        """

        assert n > 1
        self.n = n
        j = UnitQuaternion(0, True, n)
        i = UnitQuaternion(1, False, n)
        elements = sorted(Group.generate_from({i, j}))
        super().__init__(elements)


Q8 = Dicyclic(2)
Q16 = Dicyclic(4)
Q32 =Dicyclic(5)

print(Q16.subgroup_lattice())
