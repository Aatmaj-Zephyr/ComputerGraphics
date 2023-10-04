import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import math
# Initialize Pygame
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

grid = []
for x in range(-10,10):
    x=x/10
    for y in range(-10,10):
        y=y/10
        grid.append([x,y]) 
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
def dis(point1,point2):
    return sum((point1[i]-point2[i])**2 for i in [0,1])**0.5



# Example usage:
num_sides = 11
vertices = equilateral_polygon_vertices(num_sides)
d = dis(vertices[0],vertices[1]) # for calculation of distance to cutoff

def distance_from_origin(x,y):
    return (x**2+y**2)**0.5

# Function to draw a circle
def draw_circle(center_x, center_y, radius, num_segments=1000):
    
    for i in range(num_segments + 1):
        glBegin(GL_POINTS)
        theta = 2.0 * 3.1415926 * i / num_segments
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        if(distance_from_origin(center_x + x, center_y + y)<(2*(1/2)**2-(d/4)**2)**0.5):
         glVertex2f(center_x + x, center_y + y)
        glEnd()


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Draw the circle with the user-defined parameters
    glColor3f(1.0, 0.0, 0.0)  # Red color
    for point in vertices:
        draw_circle(point[0],point[1],1)

    pygame.display.flip()
    pygame.time.wait(10)
