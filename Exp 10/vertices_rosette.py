# vertices that are equidistant


def equilateral_polygon_vertices(num_sides):
    import math

    # Calculate the angle between each pair of consecutive vertices
    angle = 360 / num_sides

    # Calculate the distance from the origin to each vertex
    radius = 1.0  # You can adjust this to change the size of the polygon

    # Calculate the coordinates of the vertices
    vertices = []

    for i in range(num_sides):
        x = radius * math.cos(math.radians(i * angle))
        y = radius * math.sin(math.radians(i * angle))
        vertices.append((x, y))

    return vertices

# Example usage:
num_sides = 5
vertices = equilateral_polygon_vertices(num_sides)
for vertex in vertices:
    print(vertex)
