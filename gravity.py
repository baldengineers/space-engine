#contains the functions needed to simulate gravity and orbit of two masses

def translate(cl,dir_facing,vel,oa,vector):
    #cl = object class
    #direction = direction of acceleration of object (in degrees)
    #vel = velocity of object due to gravity
    #oa = original acceleration before being affected by gravity
    #vector = vector to travel on

    #normalize the vector
    hyp = (x**2+y**2+z**2)**.5
    for item in vector:
        item /= hyp
        item *= vel

    
    cl.accelerate(vector)
    
        
def main(class1,class2,m1,m2,d,oa1,oa2,dir1,dir2):
    #class1 = class of 1st object
    #class2 = class of 2nd object
    #f = force of gravity
    #g = gravitational constant
    #m1 = mass of more massive object
    #m2 = mass of smaller object
    #d = distance between two masses
    #a1 = acceleration of 1st object
    #a2 = acceleration of 2nd object
    #oa1 = original acceleration of 1st object
    #oa2 = original acceleration of 2nd object
    #dir1 = direction of acceleration of 1st object (in degs)
    #dir2 = direction of acceleration of 2nd object (in degs)
    
    g = 6.673*(10**-11)
    f = (g*m1*m2/d**2)
    print("%.4f Newtons" %(f))
    
    #acceleration of objects toward each other in m/s^2
    a1 = f/m1
    a2 = f/m2

    print("acceleration of larger object:%d\nsmaller object:%d" %(a1,a2))

    #vel 2 = velocity of ship(camera)
    vel1 = 0
    vel2 = 0

    #TODO: write something using the oa2 to offset the acceleration into
    #      the planet.
    
    while True: # some testing
        vel1 += a1
        vel2 += a2

        #the following tuples determine vector with which to travel on when being pulled by gravity
        vector1 = ()
        vector1[0] = class2.x - class1.x
        vector1[1] = class2.y - class1.y
        vector1[2] = class2.z - class1.z

        vector2 = ()
        vector2[0] = class1.x - class2.x
        vector2[1] = class1.y - class2.y
        vector2[2] = class1.z - class2.z

        translate(class1,dir1,vel1,oa1,vector1)
        translate(class2,dir2,vel2,oa2,vector2)

        #glTranslatef()
        #accelerate position of the ship towards the core of the planet
        #accelerate position of the ship due to its own acceleration
        #ship could either be pulled into orbit or crash into planet or slingshot away
        pass



if __name__ == '__main__':
    #mass is in kg
    #distance is in km

    from OpenGL.GL import *
    from OpenGL.GLU import *

    mass1 = 5.98*(10**24)
    mass2 = 68
    distance = 6.38*(10**6)
    main(mass1,mass2,distance)
