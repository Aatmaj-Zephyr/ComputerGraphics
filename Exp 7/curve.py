import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np

# Define the control points for the quadratic Bezier curve
control_points = np.array([
    [-0.1, 1.0],
    [1.0, 0.9],
    [-0.8, 0.0]
])

# Variable to control the number of segments in the curve
num_segments = 100

def draw_quadratic_bezier_curve(control_points, num_segments):
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_STRIP)
    for i in range(num_segments + 1):
        t = i / float(num_segments)
        p = (1 - t) ** 2 * control_points[0] + 2 * (1 - t) * t * control_points[1] + t ** 2 * control_points[2] # formula of beizer
        glVertex2f(p[0], p[1])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_quadratic_bezier_curve(control_points, num_segments)
    glFlush()

def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 800, "Quadratic Bezier Curve", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glOrtho(-1, 1, -1, 1, -1, 1)
    glClearColor(0.0, 0.0, 0.0, 1.0)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        display()
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
