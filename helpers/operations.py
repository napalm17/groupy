from elements.rotation import RotateReflect
import itertools
import math

def add_mod_n(n):
    return lambda a, b: int((a + b) % n)

def dihedral_op(a: RotateReflect, b: RotateReflect):
    return a * b

def perm_cycle_composition(a, b):
    return a * b

def perm_composition(sigma: tuple, tau: tuple) -> tuple:
    """
    Composes two permutations and returns the result as a list.

    Parameters:
    sigma (tuple): The first permutation (1-based index).
    tau (tuple): The second permutation (1-based index).

    Returns:
    tuple: The composed permutation (1-based index).
    """
    return tuple([sigma[tau[i] - 1] for i in range(len(sigma))])

def bijection(G, H, m):
    """
    Parameters:
    G (list): The domain set (list of elements).
    H (list): The codomain set (list of elements).
    m (int): The index of the permutation bijection (1-based index).

    Returns:
    function: A function that represents the m-th permutation bijection.
    Raises:
    ValueError: If G and H do not have the same size or if m is out of bounds.
    """
    if len(G) != len(H):
        raise ValueError("Sets G and H must have the same size.")
    n = len(G)
    if m < 1 or m > math.factorial(n):
        raise ValueError("Index m is out of bounds.")

    perms = list(itertools.permutations(H))
    perm = perms[m - 1]

    # Define the bijection function
    def f(x):
        return perm[G.index(x)]
    return f

