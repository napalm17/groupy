class Map:
    def __init__(self, G, H, f):
        self.G = G
        self.H = H
        self.f = f

    def __repr__(self):
        return f'Map from {self.G} to {self.H}'

    def image(self):
        """
        Returns:
        set: The set of all images of elements in G under f.
        """
        return {self.f(g) for g in self.G}

    def kernel(self):
        """
        Returns:
        set: The set of all elements in G that map to the identity element in H.
        """
        return {g for g in self.G if self.f(g) == self.H.id}

    def is_injective(self):
        """
        Returns:
        bool: True if f is injective, False otherwise.
        """

        return all(a == b or self.f(a) != self.f(b) for a in self.G for b in self.G)

    def is_surjective(self):
        """
        Returns:
        bool: True if f is surjective, False otherwise.
        """
        return self.image() == self.H.elements

    def is_bijective(self):
        """
        Returns:
        bool: True if f is bijective, False otherwise.
        """
        return self.is_injective() and self.is_surjective()

    def is_homomorphism(self):
        """
        Returns:
        bool: True if f is a homomorphism, False otherwise.
        """
        return all(self.f(g1 * g2) == self.f(g1) * self.f(g2) for g1 in self.G for g2 in self.G)

    def is_endomorphism(self):
        """
        Returns:
        bool: True if f is a homomorphism, False otherwise.
        """
        return self.is_homomorphism() and self.G.elements == self.H.elements

    def is_isomorphism(self):
        """
        Returns:
        bool: True if f is an isomorphism, False otherwise.
        """
        return self.is_homomorphism() and self.is_bijective()

    def is_automorphism(self):
        """
        Returns:
        bool: True if f is an automorphism, False otherwise.
        """
        return self.is_isomorphism() and self.G.elements == self.H.elements
