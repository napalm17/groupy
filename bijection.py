from map import Map
import itertools


class Bijection(Map):
    def __init__(self, G, H, m):
        """
        Initialize the bijection with domain G, codomain H, and the m-th permutation.
        Parameters:
        G: set
            The domain set.
        H: set
            The codomain set.
        m: int
            The index of the permutation bijection to be selected.
        """
        self.G = G
        self.H = H
        self.m = m
        self.permutations = list(itertools.permutations(self.H))
        if len(G) != len(H):
            raise ValueError("Domain and codomain must have the same size for a bijection.")
        if m < 1 or m > len(self.permutations):
            raise ValueError(f"Invalid m: must be between 1 and {len(self.permutations)}")


        # Pass the permutation function to the superclass
        super().__init__(G, H, self.mth_permutation)

    def mth_permutation(self, g):
        return self.permutations[self.m - 1][self.G.index(g)]

    def is_injective(self):
        return True

    def is_surjective(self):
        return True

    def is_bijective(self):
        return True

