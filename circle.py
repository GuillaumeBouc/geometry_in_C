import math


def get_circle_coordinates(center: tuple, radius: float, num_points: int = 100):
    """Returns a list of coordinates that form a circle."""
    circle_coords = []
    for i in range(num_points):
        angle = 2 * math.pi * i / num_points
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        circle_coords.append((x, y))
    return circle_coords
