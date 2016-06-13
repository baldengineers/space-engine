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


def Cube(r):
    glBegin(GL_TRIANGLES) #we could do quads, i just already have triangle info
                          #because of mass calculations

    for edge in tri:
        glVertex3fv(vertices[edge[0]])
        glVertex3fv(vertices[edge[1]])
        glVertex3fv(vertices[edge[2]])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glMaterial(GL_FRONT, GL_AMBIENT, (0.1, 0.1, 0.1, 1.0))    
    glMaterial(GL_FRONT, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))
    glTranslate(0,0,-40)

    glEnable(GL_DEPTH_TEST)
    
    glShadeModel(GL_FLAT)
    glClearColor(1.0, 1.0, 1.0, 0.0)

    glEnable(GL_COLOR_MATERIAL)
    
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)        
    glLightfv(GL_LIGHT0, GL_POSITION,  (10, 10, 10))

    crash = False

    while not crash:
        r = (0,0,1,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            glTranslatef(0.1,0,0)
        if keys[pygame.K_RIGHT]:
            glTranslatef(-0.1,0,0)
        if keys[pygame.K_UP]:
            glTranslatef(0,0,0.1)
        if keys[pygame.K_DOWN]:
            glTranslatef(0,0,-0.1)
        if keys[pygame.K_r]:
            r = (10,0,1,0)

        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        #print(x)

        camera_x=x[3][0]
        camera_y=x[3][1]
        camera_z=x[3][2]

        if camera_z < -1:
            crash = True
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glTranslatef(0,0,0.2)
        Cube(r)
        pygame.display.flip()
        pygame.time.wait(10)

for i in range(10):
    main()
pygame.quit()
quit()
