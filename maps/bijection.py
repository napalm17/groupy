from maps.map import Map
import itertools


class Bijection(Map):
    def __init__(self, G, H, index):
        """
        Initialize the bijection with domain G, codomain H, and the m-th permutation.
        Parameters:
        G: set
            The domain set.
        H: set
            The codomain set.
        index: int
            The index of the permutation bijection to be selected.
        """
        self.G = G
        self.H = H
        self.index = index
        self.permutations = list(itertools.permutations(self.H))
        if len(G) != len(H):
            raise ValueError("Domain and codomain must have the same size for a bijection.")
        if not (0 <= self.index < len(self.permutations)):
            raise ValueError(f"Invalid m: must be between 1 and {len(self.permutations)}")

        # Pass the permutation function to the superclass
        super().__init__(G, H, self.apply)

    def __mul__(self, other: 'Bijection'):
        if other.H == self.G:
            # this is just shit
            composed_permutation = [self.apply(other.apply(x)) for x in other.G]
            composed_index = self.permutations.index(tuple(composed_permutation))
            return Bijection(other.G, self.H, composed_index)
        raise ValueError("Domain of one function doesn't match with codomain of the other.")

    def __eq__(self, other: 'Bijection'):
        return self.G == other.G and self.H == other.H and self.index == other.index

    def __hash__(self):
        return self.index

    def apply(self, g):
        return self.permutations[self.index][self.G.index(g)]

    def is_injective(self):
        return True

    def is_surjective(self):
        return True

    def is_bijective(self):
        return True

