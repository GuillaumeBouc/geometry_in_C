import math


def apply_transform(points, transform):
    """Applies a transformation to a list of points."""
    return [transform(point) for point in points]


def transform_0(point):
    """Transform 0."""
    return point


def transform_1(point):
    """Transform 1."""
    z = complex(*point)
    z = z**2 + z.conjugate()
    return (z.real, z.imag)


def transform_2(point):
    """Transform 2."""
    z = complex(*point)
    z = z**2 + 0.1 * z.conjugate()
    return (z.real, z.imag)


def transform_3(point):
    """Transform 3."""
    z = complex(*point)
    z = (z * math.e ** (math.pi / 3 * 1j) + 0.1 * z.conjugate()) ** 2
    return (z.real, z.imag)
