import pygame
import random
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, 1, 1),
    (-1, -1, 1)
    )

tri = (
    (0,1,2),
    (0,3,2),
    (0,4,5),
    (0,1,5),
    (0,4,7),
    (0,3,7),
    (6,2,1),
    (6,5,1),
    (6,2,3),
    (6,7,3),
    (6,7,4),
    (6,5,4)
    )
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,6),
    (7,3),
    (7,4),
    (6,7),
    (5,1),
    (5,4),
    (5,6)
    )
    

clrs = [(0,1,0),(1,0,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1),(0,0,0)]


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
##        glColor(clrs[random.randint(0,7)])
##        glVertex3fv(vertices[edge[0]])
##        glVertex3fv(vertices[edge[1]])
##        glVertex3fv(vertices[edge[2]])
        for vertex in edge:
            
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
