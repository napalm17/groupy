from helpers import Algo, perm_composition


class PermutationCycle:
    def __init__(self, cycles: list[list]):
        """
        Parameters:
        cycles: list[list]: A list of lists representing the permutation cycles.
        """
        self.cycles = cycles

    def __repr__(self):
        """
        Returns:
        str: String representation of the permutation in cycle notation.
        """
        return ''.join(f"({''.join(map(str, cycle))})" for cycle in self.cycles) if self.cycles else '(1)'

    def __mul__(self, other: 'PermutationCycle'):
        """
        Parameters:
        other: Permutation: Another Permutation object.

        Returns:
        Permutation: A new Permutation object representing the composition of the two permutations.
        """
        combined_cycles = self.cycles + other.cycles
        return PermutationCycle(combined_cycles)

    def __eq__(self, other: 'PermutationCycle'):
        """
        Parameters:
        other: Permutation: Another Permutation object.

        Returns:
        bool: True if both objects have the same tuple list, False otherwise.
        """
        return self.cycles == other.cycles

    def __hash__(self):
        """
        Returns:
        int: Hash value based on the sorted tuple list.
        """
        return hash(tuple(sorted(self.cycles)))

    def transpositions(self) -> 'PermutationCycle':
        """
        Returns:
        Permutation: A Permutation object containing transpositions representing the original permutation.
        """
        transpositions = []
        for cycle in self.cycles:
            if len(cycle) > 1:
                k = len(cycle) - 1
                for i in range(k):
                    transpositions.append([cycle[0], cycle[k - i]])

        return PermutationCycle(Algo.simplify_transpositions(transpositions))

    def disjoint_form(self):
        return PermutationCycle(Algo.transpositions_to_disjoint_cycles(self.transpositions().cycles))


class PermutationArray:
    def __init__(self, sigma: tuple):
        """
        Parameters:
        sigma: list[list]: A list of integers representing the image of the permutation.
        """
        self.sigma = sigma

    def __repr__(self):
        """
        Returns:
        str: String representation of the permutation in one line notation.
        """
        #return ''.join([str(p) for p in self.sigma])
        return self.get_cycle()

    def __mul__(self, other: 'PermutationArray'):
        """
        Parameters:
        other: Permutation: Another Permutation object.

        Returns:
        Permutation: A new Permutation object representing the composition of the two permutations.
        """
        composition = perm_composition(self.sigma, other.sigma)
        return PermutationArray(composition)

    def __eq__(self, other: 'PermutationArray'):
        """
        Parameters:
        other: Permutation: Another Permutation object.

        Returns:
        bool: True if both objects have the same list, False otherwise.
        """
        return self.sigma == other.sigma

    def __hash__(self):
        """
        Returns:
        int: Hash value based on the list.
        """
        return hash(tuple(self.sigma))

    def get_cycle(self):
        """
        :return: The permutation represented in cycle notation.
        """
        return str(PermutationCycle(Algo.one_line_to_cycles(self.sigma)))

    def __pow__(self, power, modulo=None):
        result = self
        for i in range(power - 1):
            result *= result
        return result

    def __lt__(self, other):
        return self.sigma < other.sigma

    def __gt__(self, other):
        return self.sigma > other.sigma


