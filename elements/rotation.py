from helpers import Utility

class RotateReflect:
    def __init__(self, rotations: int, reflection=False, order=1):
        self.rotations = rotations
        self.reflection = reflection
        self.order = order

    def __mul__(self, other: 'RotateReflect'):
        if self.reflection:
            return RotateReflect((self.rotations-other.rotations)%self.order, not other.reflection, self.order)
        return RotateReflect((self.rotations+other.rotations)%self.order, other.reflection, self.order)

    def __repr__(self):
        symbol = (f'r{Utility.to_superscript(self.rotations)}' if self.rotations != 0 else 'e') + ('s' if self.reflection else '')
        return symbol if symbol != 'es' else 's'

    def __eq__(self, other: 'RotateReflect'):
        return (self.reflection == other.reflection) and self.rotations == other.rotations

    def __hash__(self):
        return hash((self.rotations, self.reflection))

    def __pow__(self, power, modulo=None):
        result = self
        for i in range(power - 1):
            result *= result
        return result

    def __lt__(self, other):
        return (self.reflection, self.rotations) < (other.reflection, other.rotations)

    def __gt__(self, other):
        return (self.reflection, self.rotations) > (other.reflection, other.rotations)


