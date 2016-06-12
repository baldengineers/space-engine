def calculateMass(vertices, edges, material=''):
    
    #INSERT A PLANET/OBJECT TYPE DICTIONARY HERE
    #--
    #name of planet type or manmade object : density
    #--
    #these would be like planets being gas giants, hard rock
    #life supporting, ice, etc. We can research densities
    #accordingly
    
    totalVolume = 0
    for tri in len(edges):
        ind0,ind1,ind2 = vertices[edges[tri][0]],vertices[edges[tri][1]],vertices[edges[tri+1][1]]
        x1,y1,z1 = ind0[0],ind0[1],ind0[2]
        x2,y2,z2 = ind1[0],ind1[1],ind1[2]
        x3,y3,z3 = ind2[0],ind2[1],ind2[2]
        totalVolume += abs((1/6) * ( (-x3*y2*z1)+(x2*y3*z1)+(x3*y1*z2)-(x1*y3*z2)-(x2*y1*z3)+(x1*y2*z3) ) )
        
    
