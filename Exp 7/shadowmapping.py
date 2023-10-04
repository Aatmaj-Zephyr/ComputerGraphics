import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Define vertices for the triangle
vertices = [
    (0, 1, 0),
    (-1, -1, 0.5),
    (1, -1, 1)
]

# Define the light source position
light_position = (4, 2, 0)

# Initialize Pygame
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glClearColor(0.0, 0.0, 0.0, 1.0)
glEnable(GL_DEPTH_TEST)

# Define the projection matrix
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0, 0, -5)

def draw_triangle(color):
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()

def draw_plane():
    glBegin(GL_QUADS)   
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-2.7, 0.7, -2.7)
    glVertex3f(2.7, 0.7, -2.7)
    glVertex3f(1.7, -1.7, 1.7)
    glVertex3f(-1.7, -1.7, 1.7)
    glEnd()

def draw_shadow():
    glDisable(GL_LIGHTING)
    glColor3f(1.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(0, -1.01, 0)  # Slightly below the plane
    draw_triangle((0.5,0.5,0.5))
    glPopMatrix()
     

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        # Setup lighting
        #glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)

        # Draw the triangle
        glPushMatrix()
        glRotatef(1, 3, 1, 1)
        draw_triangle((0,1,0))
        glPopMatrix()

        # Draw the plane
        draw_plane()

        # Draw the shadow
        draw_shadow()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
