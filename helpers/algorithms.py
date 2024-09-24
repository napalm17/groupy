import math
from collections import defaultdict
import numpy as np

class Algo:

    @staticmethod
    def transform_indices(input_array):
        input_array = np.array(input_array)
        result = np.zeros_like(input_array, dtype=int)  # Initialize result array with zeros

        # Get unique values and their counts
        unique_values, counts = np.unique(input_array, return_counts=True)

        # Assign values centered around zero
        for unique_value, count in zip(unique_values, counts):
            indices = np.where(input_array == unique_value)[0]
            half_range = (count - 1) / 2
            centered_values = np.arange(-half_range, half_range + 1)  # Create centered values
            result[indices] = centered_values[:len(indices)]  # Assign based on indices

        return result

    @staticmethod
    def build_partial_ordering(sets):
        """Builds a directed graph representing the inclusion relationships between sets."""
        edges = []

        # Compare every pair of sets to check for inclusion
        for i, set_a in enumerate(sets):
            for j, set_b in enumerate(sets):
                if i != j and set_a.issubset(set_b):
                    # Check if set_a is a subset of any other sets
                    smaller_set = set_b
                    for k, set_c in enumerate(sets):
                        if k != i and set_a.issubset(set_c) and set_b != set_c:
                            if len(set_c) < len(smaller_set):
                                smaller_set = set_c
                    edges.append((tuple(sorted(set_a)), tuple(sorted(smaller_set))))

        return edges, [tuple(sorted(set)) for set in sets]

    @staticmethod
    def factors(n):
        """
        Get all factors of a positive integer n.

        Parameters:
        n (int): A positive integer.

        Returns:
        list: A sorted list of factors of n.

        Raises:
        ValueError: If n is not a positive integer.
        """
        if n <= 0:
            raise ValueError("Input must be a positive integer.")

        # Generate potential factors up to the square root of n
        potential_factors = range(1, int(math.sqrt(n)) + 1)

        # Check for divisibility
        factors = [i for i in potential_factors if n % i == 0]

        # Include the corresponding pairs of factors
        all_factors = set(factors + [n // i for i in factors])

        return sorted(all_factors)

    @staticmethod
    def do_commute(trans1, trans2):
        """
        Check if two transpositions commute.

        Parameters:
        trans1 (list): First transposition.
        trans2 (list): Second transposition.

        Returns:
        bool: True if the transpositions commute, False otherwise.
        """
        return not bool(set(trans1) & set(trans2))

    @staticmethod
    def simplify_transpositions(transpositions: list[list[int]]) -> list[list[int]]:
        """
        Simplify a list of transpositions by applying commuting and cancellation rules.

        Parameters:
        transpositions (list[list[int]]): A list of transpositions, each represented as a list of length 2.

        Returns:
        list[list[int]]: A list of simplified transpositions.
        """
        j = 0
        while j < len(transpositions) - 1:
            i = 0
            while i < len(transpositions) - 1:
                trans1, trans2 = transpositions[i: i + 2]
                if sorted(trans1) == sorted(trans2):
                    transpositions.pop(i)
                    transpositions.pop(i)
                    i = 0
                    continue
                elif Algo.do_commute(trans1, trans2):
                    transpositions[i], transpositions[i + 1] = trans2, trans1
                i += 1
            j += 1
        return transpositions

    @staticmethod
    def transpositions_to_disjoint_cycles(transpositions):
        """
        Converts a list of transpositions into disjoint cycles.

        Parameters:
        transpositions (list): A list of tuples representing transpositions.

        Returns:
        list: A list of tuples representing the permutation in disjoint cycles notation.
        """
        # Initialize a mapping of elements to their final positions
        mapping = {}
        # Apply each transposition
        for transposition in transpositions:
            a, b = transposition
            mapping[a], mapping[b] = mapping.get(b, b), mapping.get(a, a)
        # Find disjoint cycles
        visited = set()
        cycles = []
        for elem in sorted(mapping):  # Iterate through sorted elements for consistent output
            if elem not in visited:
                cycle = []
                current = elem
                while current not in visited:
                    visited.add(current)
                    cycle.append(current)
                    current = mapping[current]
                if len(cycle) > 1:
                    cycles.append(tuple(cycle))
        # Sort cycles based on their smallest element
        cycles.sort(key=lambda x: x[0])
        return cycles

    @staticmethod
    def one_line_to_cycles(perm: tuple):
        """
        Convert a permutation from one-line notation to disjoint cycles.

        Parameters:
        perm (tuple): A tuple of integers representing a permutation in one-line notation.

        Returns:
        list: A list of tuples representing the permutation in disjoint cycles notation.
        """
        n = len(perm)
        visited = [False] * n  # To track visited elements
        cycles = []  # List to store the cycles
        for i in range(n):
            if not visited[i]:
                cycle = []
                current = i
                while not visited[current]:
                    visited[current] = True
                    cycle.append(current + 1)  # 1-based indexing
                    current = perm[current] - 1  # Go to the next element in the cycle (1-based to 0-based)
                if len(cycle) > 1:  # Only non-trivial cycles
                    cycles.append(cycle)

        return cycles

# Example usage
perm = (2, 1, 4, 3)
cycles = Algo.one_line_to_cycles(perm)
# print(cycles)  # Output: [(3, 4)]
# print(Algo.factors(28))
