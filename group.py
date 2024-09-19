from itertools import combinations, product
from helpers.algorithms import Algo
from tqdm import tqdm
from direct_product import DirectProduct
from coset import LeftCoset
from maps.bijection import Bijection
import math
from vfx.table import Table
import numpy as np
from vfx.graph import Graph

class Group:
    def __init__(self, elements, operation=None):
        self.elements = set(elements)
        self.order = len(self.elements)
        self.id = self.identity()

    def __repr__(self):
        return f'{self.elements}'

    def __mul__(self, other: 'Group'):
        product_elements = [DirectProduct(a, b) for a in self.elements for b in other.elements]
        return Group(product_elements)

    def __iter__(self):
        return iter(self.elements)

    def __len__(self):
        return self.order

    def __eq__(self, other: 'Group'):
        if self.order != other.order:
            return False
        return any(Bijection(self, other, m).is_isomorphism() for m in range(math.factorial(self.order) ))

    def index(self, g):
        return list(self.elements).index(g)

    def is_group(self):
        return self.has_identity() and self.is_closed() and self.has_inverses()

    def is_abelian(self):
        return all(a * b == b * a for a in self.elements for b in self.elements)

    def is_simple(self):
        return all(N.order in {1, self.order} for N in self.normal_subgroups())

    def is_closed(self):
        #ab = [(a*b) for a in self.elements for b in self.elements if a * b not in self.elements][0]
        #print('\n\n\n\n')
        #print(ab in self.elements)
        return all(a * b in self.elements for a in self.elements for b in self.elements)

    def identity(self):
        return next((e for e in self.elements if all(e * a == a and a * e == a for a in self.elements)), None)

    def has_identity(self):
        return self.identity() is not None

    def inverse(self, g):
        return next((b for b in self.elements if g * b == self.identity()), None)

    def has_inverses(self):
        return all(self.inverse(g) is not None for g in self.elements)

    def do_commute(self, g, h):
        if g in self.elements and h in self.elements:
            return g * h == h * g
        raise ValueError("The given elements don't belong to the group")

    def center(self):
        return {z for z in self.elements if all(self.do_commute(z , g) for g in self.elements)}

    def factoring_subsets(self, maxorder):
        orders = [r for r in Algo.factors(self.order) if r <= maxorder]
        return [set(subset) for r in orders for subset in tqdm(combinations(self.elements, r), desc="Processing items") if self.id in subset]

    def has_subgroup(self, subgroup: 'Group'):
        return subgroup.is_group() and subgroup.elements.issubset(self.elements)

    def has_normal_subgroup(self, subgroup: 'Group'):
        if self.has_subgroup(subgroup):
            return all(self.left_coset(subgroup, g) == self.right_coset(subgroup, g) for g in self.elements)
        return False

    def subgroups(self, maxorder=None):
        # Generate all possible subsets of the group
        if maxorder is None:
            maxorder = self.order
        subgroups = [Group(subset) for subset in tqdm(self.factoring_subsets(maxorder), desc='sg') if Group(subset).is_group()]
        return subgroups

    def normal_subgroups(self):
        subgroups = self.subgroups()
        return [subgroup for subgroup in subgroups if self.has_normal_subgroup(subgroup)]

    def left_coset(self, H: 'Group', g):
        if not self.has_subgroup(H):
            raise ValueError('The input is not a subgroup ')
        return {g * h for h in H.elements}

    def right_coset(self, H: 'Group', g):
        if not self.has_subgroup(H):
            raise ValueError('The input is not a subgroup ')
        return {h * g for h in H.elements}

    def conjugate(self, g, x):
        return g * (x * self.inverse(g))

    def conjugacy_class(self, x):
        return {self.conjugate(g, x) for g in self.elements}

    def commutator(self, g, h):
        return (g * h) * (self.inverse(g) * self.inverse(h))

    def commutator_subgroup(self):
        return Group({self.commutator(g, h) for g in self.elements for h in self.elements})

    def quotient_group(self, N: 'Group'):
        if not self.has_normal_subgroup(N):
            raise ValueError('The input is not a normal subgroup.')
        cosets = {LeftCoset(g, N) for g in self.elements}
        return Group(cosets)

    def generate_from(self, subset):
        """Generate all elements from a subset using the group operation."""
        generated = set(subset)
        while True:
            new_elements = set()
            for a, b in product(generated, repeat=2):
                new_elements.add(a * b)
            if new_elements.issubset(generated):
                break
            generated.update(new_elements)
        return generated

    def generators(self):
        """Find all generator sets of the same minimal order and return them."""
        for size in range(1, self.order + 1):
            pairs = [(subset, self.generate_from(subset)) for subset in tqdm(combinations(self.elements, size))]
            generators = [set(subset) for subset, generated in pairs if generated == self.elements]
            if generators:
                return generators
        return None

    def is_generator(self, subset):
        return self.generate_from(subset) == self.elements

    def cayley_table(self):
        print(sorted(self.elements))
        """Creates a Cayley table for the group and returns a Table object."""
        matrix = [[x * y for x in sorted(self.elements)] for y in [self.inverse(g) for g in sorted(self.elements)]]
        return Table(np.array(matrix))  # Return a Table object containing the matrix

    def cayley_graph(self, generators=None):
        """
        Create a Cayley graph of the group with respect to the given generators.

        Parameters:
        - generators (list): A list of generators for the group.

        Returns:
        - Graph: A Graph object representing the Cayley graph.
        """
        if not generators:
            generators = self.generators()[3]
        # Create a new Graph object
        graph = Graph()
        # Add vertices to the graph (group elements)
        for element in self.elements:
            graph.add_vertex(element)
        # Add edges based on generators
        for g in generators:
            for elem1 in self.elements:
                elem2 = elem1 * g
                if elem2 != elem1:
                    graph.add_edge(elem1, elem2, generator=g)


        return graph



def add_mod_n(n):
    return lambda a, b: int((a + b) % n)


add_mod_4 = add_mod_n(4)

#Z4 = Group({0, 1, 2, 3}, add_mod_4)
#Z2 = Group({0, 2}, add_mod_4)
#Z9 = Group(set(range(9)), add_mod_n(9))
#Z1 = Z4.get_subgroups()[2]

#oneZ1 = Z4.left_coset(Z1, 1)
#print(Z4.normal_subgroups())