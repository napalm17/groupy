import math

class Algo:

    @staticmethod
    def factors(n):
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
        # Two transpositions commute if they share no common element
        return not bool(set(trans1) & set(trans2))

    @staticmethod
    def simplify_transpositions(transpositions: list[list[int]]) -> list[list[int]]:
        """
        Parameters:
        transpositions: list[list[int]]: A list of transpositions, each represented as a list of length 2.
        Returns:
        list[list[int]]: A list of transpositions after applying the commuting and cancellation rules.
        """
        j = 0
        while j < len(transpositions) - 1:
            i = 0
            while i < len(transpositions) - 1:
                print(transpositions)
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
        # Sort each cycle internally
        #sorted_cycles = [sorted(cycle) for cycle in cycles]
        # Sort cycles based on their smallest element
        cycles.sort(key=lambda x: x[0])
        return cycles

    @staticmethod
    def one_line_to_cycles(perm: tuple):
        """
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
#print(cycles)  # Output: [(3, 4)]
#print(Algo.factors(28))

