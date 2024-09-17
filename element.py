class Element:
    def __init__(self, value, group):
        self.value = value  # The value of the group element
        self.group = group  # The group this element belongs to

    def __mul__(self, other):
        if isinstance(other, Element):
            # Return a new GroupElement that represents the product
            return Element(self.group.operation(self.value, other.value), self.group)
        else:
            raise ValueError("Elements must belong to the same group to multiply")

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return self.value

