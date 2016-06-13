import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

import camera

def main():
    pygame.init()
    display=(1280,720)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(70, (display[0]/display[1]), 0.1, 150000000)#camera distance maximum is one AU, we may change.
    camera.Camera(0,0,0,0) # camera starts at the center of the map
    #not moving and pointing forward
    

    while True: #main loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.ENTER: #going to change this to hold down
                direction = camera.Camera.get_dir()
                dirx,diry,dirz=direction[0],direction[1],direction[2]
                sum_dir = abs(dirx)+abs(diry)+abs(dirz)
                velx,vely,velz=(dirx/sum_dir)*0.0001,(diry/sumdir)*0.0001,(dirz/sumdir)*0.0001      
                camera.Camera.accelerate(velx,vely,velz)
                #adds to total velocity 0.0001 in total, distributed accross all 3 axes
            if event.type == pygame.SHIFT: 
                direction = camera.Camera.get_dir()
                dirx,diry,dirz=direction[0],direction[1],direction[2]
                sum_dir = abs(dirx)+abs(diry)+abs(dirz)
                velx,vely,velz=(dirx/sum_dir)*-0.0001,(diry/sumdir)*-0.0001,(dirz/sumdir)*-0.0001      
                camera.Camera.accelerate(velx,vely,velz) #subtracts from total velocity   
            
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
