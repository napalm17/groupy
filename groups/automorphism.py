from group import Group
from maps.bijection import Bijection
import math



class Aut(Group):
    def __init__(self, G: Group):
        """
        Initialize the automorphism group of a given group G.

        Parameters:
        G (Group): The group for which the automorphism group is being created.
        """
        self.G = G
        bijections = [Bijection(G, G, m) for m in range(math.factorial(G.order))]
        elements = {b for b in bijections if b.is_automorphism()}
        super().__init__(elements)

    def __repr__(self):
        return f'Aut({self.G})'

