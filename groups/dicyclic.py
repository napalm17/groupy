from group import Group
from elements.quaternion import UnitQuaternion

class Dicyclic(Group):
    def __init__(self, n: int):
        assert n > 1
        self.n = n
        j = UnitQuaternion(0, True, n)
        i = UnitQuaternion(1, False, n)
        elements = Group.generate_from({i, j})
        super().__init__(elements)


Q8 = Dicyclic(2)
Q16 = Dicyclic(4)
Q32 =Dicyclic(5)

print(Q32.cayley_graph().plot())