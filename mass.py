def calculateMass(vertices, triangles, DENSITY=''):
    
    #INSERT A PLANET/OBJECT TYPE DICTIONARY HERE
    #--
    #name of planet type or manmade object : density
    #--
    #these would be like planets being gas giants, hard rock
    #life supporting, ice, etc. We can research densities
    #accordingly.

    #for now, density = 1

    DENSITY = 1

   
    totalVolume = 0
    for tri in range(len(triangles)):
        ind0,ind1,ind2 = vertices[triangles[tri][2]],vertices[triangles[tri][1]],vertices[triangles[tri][0]]
        x1,y1,z1 = ind0[0],ind0[1],ind0[2]
        x2,y2,z2 = ind1[0],ind1[1],ind1[2]
        x3,y3,z3 = ind2[0],ind2[1],ind2[2]
        totalVolume += abs((1/6) * ( -(x3*y2*z1)+(x2*y3*z1)+(x3*y1*z2)-(x1*y3*z2)-(x2*y1*z3)+(x1*y2*z3) ))
        
        
    mass = abs(totalVolume)*DENSITY
    print(mass)
    return mass
##
##vertices = (
##    (1, -1, -1),
##    (1, 1, -1),
##    (-1, 1, -1),
##    (-1, -1, -1),
##    (1, -1, 1),
##    (1, 1, 1),
##    (-1, 1, 1),
##    (-1, -1, 1)
##    )
##
##tris = (
##    (0,1,2),
##    (0,3,2),
##    (0,4,5),
##    (0,1,5),
##    (0,4,7),
##    (0,3,7),
##    (6,2,1),
##    (6,5,1),
##    (6,2,3),
##    (6,7,3),
##    (6,7,4),
##    (6,5,4)
##    )
##
##
##calculateMass(vertices,tris)
