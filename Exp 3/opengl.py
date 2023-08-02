from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_line(x1, y1, x2, y2):
    
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)  # Set color to white (RGB values: 1.0, 1.0, 1.0)
    glBegin(GL_LINES)

    draw_line(0.0, 0.0, 0.0, 0.5)
    draw_line(0.0, 0.5, 0.5, 0.5)
    draw_line(0.5, 0.5, 0.5, 0.0)
    draw_line(0.5, 0.0, 0.0, 0.0)
    

    glEnd()
    glFlush()


glutInit()
glutInitWindowSize(400, 400)
glutCreateWindow(b"PyOpenGL Line Example")
glutDisplayFunc(display)
glutMainLoop()
