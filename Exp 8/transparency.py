from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Define vertices and colors for the squares
square1_vertices = [
    (-0.5, -0.5),
    (-0.5, 0.5),
    (0.5, 0.5),
    (0.5, -0.5)
]

square2_vertices = [
    (0, 0),
    (0, 1),
    (1, 1),
    (1, 0)
]

colors = [
    (1, 0.5, 0,int(input("please enter orange transparency 1-10 "))/10),  # Orange
    (0, 1, 0,int(input("please enter green transparency 1-10 "))/10)     # Green
]

def draw_square(vertices, color):
    glColor4fv(color)
    
    for vertex in vertices:
        glVertex2fv(vertex)
    
    

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # Set color to white (RGB values: 1.0, 1.0, 1.0)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
  
    glBegin(GL_QUADS)
        # Enable blending for transparency
    draw_square(square1_vertices,colors[0])
    draw_square(square2_vertices,colors[1])
    
    

    glEnd()
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 800)
glutCreateWindow(b"PyOpenGL transparency Example")
glutDisplayFunc(display)
glutMainLoop()
