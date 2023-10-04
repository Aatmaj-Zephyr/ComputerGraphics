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


# Function to draw a circle
def draw_circle(center_x, center_y, radius, num_segments=100):
    glBegin(GL_LINE_LOOP)
    glVertex2f(center_x, center_y)  # Center of the circle
    for i in range(num_segments + 1):
        theta = 2.0 * 3.1415926 * i / num_segments
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        glVertex2f(center_x + x, center_y + y)
    glEnd()

def draw_line(x,y,x2,y2):
     glBegin(GL_LINES)
     glVertex2f(x, y)
     glVertex2f(x2, y2)
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
    for point in grid:
        draw_circle(point[0], point[1], 0.1)
    
    for point in grid:
        draw_line(point[0],point[1],point[0]+0.1,point[1])
        draw_line(point[0],point[1],point[0],point[1]+0.1)

    pygame.display.flip()
    pygame.time.wait(10)
