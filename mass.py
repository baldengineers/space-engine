def calculateMass(vertices, edges, material=''):
    
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
    for tri in range(len(edges)):

        sec = 0 if tri == len(edges)-1 else tri+1
        ind0,ind1,ind2 = vertices[edges[tri][0]],vertices[edges[tri][1]],vertices[edges[sec][1]]
        x1,y1,z1 = ind0[0],ind0[1],ind0[2]
        x2,y2,z2 = ind1[0],ind1[1],ind1[2]
        x3,y3,z3 = ind2[0],ind2[1],ind2[2]
        totalVolume += abs((1/6) * ( -(x3*y2*z1)+(x2*y3*z1)+(x3*y1*z2)-(x1*y3*z2)-(x2*y1*z3)+(x1*y2*z3) ) )
        
    mass = totalVolume*DENSITY
    print(mass)
    #return mass

    ## THIS IS NOT WORKING
    # I think it's because it's not getting the
    # vertices of all the triangles the shape makes.
    # no idea
    
    
## for testing
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7))

calculateMass(vertices,edges)
