import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Global list to store points
points = []

def draw_point(x, y):
    glPointSize(10)  # Set the size of the points
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set clear color to black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_p:
                    print("Pressed p")
                    x, y = pygame.mouse.get_pos()
                    print(x, y)
                    glColor3f(1.0, 0.0, 0.0)  # Red color
                    draw_point((x/400)-1, 1-(y/300)-1)
                    print((x/400)-1, (y/300)-1)
                    pygame.display.flip()
                    
                elif event.key == pygame.K_LEFT:
                    x, y = pygame.mouse.get_pos()
                    points.append((x, 600 - y))

        pygame.display.flip()  # Update the display
        pygame.time.wait(10)

        
        #draw_point(0,0)
        
        

    

if __name__ == "__main__":
    main()
