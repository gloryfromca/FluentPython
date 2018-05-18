from math import hypot


class Vector(object):
    """
    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 3)
    >>> v1 + v2
    Vector(4, 7)

    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0

    >>> v * 3
    Vector(9, 12)

    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%s, %s)" % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __bool__(self):
        return bool(self.x or self.y)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
