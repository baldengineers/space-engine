import gravity
class Star():
    def __init__(self,x,y,z,radius):
        self.acceleration=[0,0,0]
        self.x,self.y,self.z,self.radius=x,y,z,radius
        self.velocity= [x,y,z]
        glLoadIdentity()
        #radius in km
        glEnable(GL_LIGHTING)
        gluNewSphere(gluNewQuadric(),radius,int(radius/10),int(radius/10))
        glDisable(GL_LIGHTING);
        glPushMatrix()
        glTranslatef(x,y,z)
        glPopMatrix()
    def update_accleration(self,acc):
        for index,i in enumerate(acc):
            self.acceleration[index]=i
        
    def accelerate(self,amount):
        self.x += amount[0]
        self.y += amount[1]
        self.z += amount[2]        
        self.velocity[0]+=amount[0]
        self.velocity[1]+=amount[1]
        self.velocity[2]+=amount[2]
    def move(self):
        glLoadIdentity()
        #radius in km
        glEnable(GL_LIGHTING)
        gluNewSphere(gluNewQuadric(),self.radius,int(self.radius/10),int(self.radius/10))
        glDisable(GL_LIGHTING);
        glPushMatrix()
        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        if x[3][2] < 150000000 or x[3][1] < 150000000 or x[3][0] < 150000000:
            #this has to be using <gravity.main> with the first class being the
            #planet/body. we can get information about the camera to pass into
            #gravity by calling the get_ funcs in camera.py

            #mass is going to be (4/3)*(3.1415926)*(self.radius**3)

            #for the other ones, we'll have to loop through ALL the matrices
            #instead of except this one and comparing them.
            pass
        self.accelerate(self.accleration)
        glTranslatef(self.velocity[0],self.velocity[1],self.velocity[2])
        glPopMatrix()
        
    def get_velocity(self):
        return self.velocity
