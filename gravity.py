def main(m1,m2,d,oa1,oa2):
    #f = force of gravity
    #g = gravitational constant
    #m1 = mass of more massive object
    #m2 = mass of smaller object
    #d = distance between two masses
    #a1 = acceleration of 1st object
    #a2 = acceleration of 2nd object
    #oa1 = original acceleration of 1st object
    #oa2 = original acceleration of 2nd object
    
    g = 6.673*(10**-11)
    f = (g*m1*m2/d**2)
    print("%.4f Newtons" %(f))
    
    #acceleration of objects toward each other in m/s^2
    a1 = f/m1
    a2 = f/m2

    print("acceleration of larger object:%d\nsmaller object:%d" %(a1,a2))

    #TODO: write something using the oa2 to offset the acceleration into
    #      the planet.

    while True: # some testing
        #accelerate position of the ship towards the core of the planet
        #accelerate position of the ship due to its own acceleration
        #ship could either be pulled into orbit or crash into planet or slingshot away
        pass

    

if __name__ == '__main__':
    #mass is in kg
    #distance is in km

    mass1 = 5.98*(10**24)
    mass2 = 68
    distance = 6.38*(10**6)
    main(mass1,mass2,distance)
