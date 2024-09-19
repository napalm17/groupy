import math
from helpers.utils import Utility
import cmath


class UnitComplex:
    """
    A class to represent a unit complex number on the complex plane.
    """
    def __init__(self, theta, resolution):
        """
        Parameters:
            theta (float): The angle in radians.
            resolution (float): The tolerance for comparison.
        """
        self.theta = theta % (2 * math.pi)
        self.resolution = resolution
        self.size = 2 * math.pi / resolution

    def __repr__(self):
        """
        Returns:
            str: A string in the form 'exp(i * theta)'.
        """
        return f"e{Utility.to_superscript(f'{round(self.theta, 2)}i')}"

    def __mul__(self, other):
        """
        Parameters:
            other (UnitComplex): Another UnitComplex instance.

        Returns:
            UnitComplex: A new UnitComplex instance representing the product.
        """
        # Multiply by adding angles modulo 2π
        new_theta = (self.theta + other.theta) % (2 * math.pi)
        return UnitComplex(new_theta, self.resolution)

    def __eq__(self, other):
        """
        Parameters:
            other (UnitComplex): Another UnitComplex instance.

        Returns:
            bool: True if the unit complex numbers are equal within the tolerance, False otherwise.
        """
        # Compare angles with tolerance based on resolution
        angle_diff = abs(self.theta - other.theta) % (2 * math.pi)
        return angle_diff <= self.resolution

    def __hash__(self):
        angle_hash = int(self.theta / self.resolution) % int(self.size)
        print(angle_hash)
        return hash((angle_hash, self.resolution))

    def get_value(self):
        return cmath.exp(1j * self.theta)

uc1 = UnitComplex(math.pi / 4, 1e-2)
uc2 = UnitComplex(math.pi / 3, 1e-2)
uc3 = UnitComplex(math.pi / 4 + 2 * math.pi, 1e-2)  # Same as uc1

