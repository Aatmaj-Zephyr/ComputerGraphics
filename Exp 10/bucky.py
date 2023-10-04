phi=1.618
coord = [(0,1,3*phi),
(0,1,-3*phi),
(0,-1,3*phi),
(0,-1,-3*phi),
(1,3*phi,0),
(1,-3*phi,0),
(-1,3*phi,0),
(-1,-3*phi,0),
(3*phi,0,1),
(3*phi,0,-1),
(-3*phi,0,1),
(-3*phi,0,-1),
(2,(1+2*phi),1*phi),
(2,(1+2*phi),-1*phi),
(2,-(1+2*phi),1*phi),
(2,-(1+2*phi),-1*phi),
(-2,(1+2*phi),1*phi),
(-2,(1+2*phi),-1*phi),
(-2,-(1+2*phi),1*phi),
(-2,-(1+2*phi),-1*phi),
((1+2*phi),1*phi,2),
((1+2*phi),1*phi,-2),
((1+2*phi),-1*phi,2),
((1+2*phi),-1*phi,-2),
(-(1+2*phi),1*phi,2),
(-(1+2*phi),1*phi,-2),
(-(1+2*phi),-1*phi,2),
(-(1+2*phi),-1*phi,-2),
(1*phi,2,(1+2*phi)),
(1*phi,2,-(1+2*phi)),
(1*phi,-2,(1+2*phi)),
(1*phi,-2,-(1+2*phi)),
(-1*phi,2,(1+2*phi)),
(-1*phi,2,-(1+2*phi)),
(-1*phi,-2,(1+2*phi)),
(-1*phi,-2,-(1+2*phi)),
(1,(2+1*phi),2*phi),
(1,(2+1*phi),-2*phi),
(1,-(2+1*phi),2*phi),
(1,-(2+1*phi),-2*phi),
(-1,(2+1*phi),2*phi),
(-1,(2+1*phi),-2*phi),
(-1,-(2+1*phi),2*phi),
(-1,-(2+1*phi),-2*phi),
((2+1*phi),2*phi,1),
((2+1*phi),2*phi,-1),
((2+1*phi),-2*phi,1),
((2+1*phi),-2*phi,-1),
(-(2+1*phi),2*phi,1),
(-(2+1*phi),2*phi,-1),
(-(2+1*phi),-2*phi,1),
(-(2+1*phi),-2*phi,-1),
(2*phi,1,(2+1*phi)),
(2*phi,1,-(2+1*phi)),
(2*phi,-1,(2+1*phi)),
(2*phi,-1,-(2+1*phi)),
(-2*phi,1,(2+1*phi)),
(-2*phi,1,-(2+1*phi)),
(-2*phi,-1,(2+1*phi)),
(-2*phi,-1,-(2+1*phi))]

print(coord)
normalizedCoord=[]
for coordinate in coord:
    normalizedCoordinate=[0,0,0]
    normalizedCoordinate[0]=coordinate[0]/3
    normalizedCoordinate[1]=coordinate[1]/3
    normalizedCoordinate[2]=coordinate[2]/3
    normalizedCoord.append(normalizedCoordinate)




import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Define some 3D points
points = [
    (0.0, 0.0, 0.0),  # Point at the origin
    (1.0, 2.0, 3.0),  # Example point
    (-2.0, -1.0, 1.0),  # Another example point
]

def dis(point1,point2):
    return sum((point1[i]-point2[i])**2 for i in [0,1,2])**0.5
def draw_points():
    glPointSize(5) 
    glBegin(GL_POINTS)
    for point in normalizedCoord:
        glVertex3fv(point)
    glEnd()

    for point1 in normalizedCoord:
        for point2 in normalizedCoord:
            
            if(dis(point1,point2)<=0.757):
                draw_lines(point1,point2)

def draw_lines(point1,point2):
    
    glBegin(GL_LINES)
    
    glVertex3fv(point1)
    glVertex3fv(point2)
    glEnd()


pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_points()
    pygame.display.flip()
    pygame.time.wait(10)

