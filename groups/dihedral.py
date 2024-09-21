from group import Group
from elements.rotation import RotateReflect


class DihedralGroup(Group):
    def __init__(self, n: int):
        self.n = n
        elements = {RotateReflect(r, s, n) for s in [False, True] for r in range(n)}
        super().__init__(elements)

    def __repr__(self):
        return f'D{self.n}={self.elements}'

D3 = DihedralGroup(3)

C3 = D3.normal_subgroups()[1]

#D3.cayley_graph().plot()

D8 = DihedralGroup(8)
print(D8.quotient_group(D8.subgroups()[2]).cayley_graph().plot())