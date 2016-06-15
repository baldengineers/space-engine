#contains the camera class

class Camera():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.acceleration=[0,0,0]
        self.direction = (0,0,-1.0) #direction camera is looking, this is the default
        #uhhh, what I meant self.direction to be was the DEGREE measure of the direction
        self.velocity = [self.x,self.y,self.z] #it is moving 0 units per second in all axes. direction (and speed) camera is moving
        
    def update_dir(self, direction, axis):
        #vector can be 'x', 'y', 'z', 'xy', 'xz', etc.

        #this needs to be way more specific; the direction will be defined by
        #where a mouse is pointed
        glRotatef(direction, 1 if 'x' in axis else 0, 1 if 'y' in axis else 0, 1 if 'z' in axis)

    def get_dir(self):
        return self.direction
    
    def get_velocity(self):
        return self.velocity
    
    def update_accleration(self,acc):
        for index,i in enumerate(acc):
            self.acceleration[index]=i    
        
    def accelerate(self, amount)
        self.x += amount[0]
        self.y += amount[1]
        self.z += amount[2]
        self.velocity[0]+=amount[0]
        self.velocity[1]+=amount[1]
        self.velocity[2]+=amount[2]

        
    def move(self):
        #done every tick
        #this moves everything. other classes will
        #pop a matrix and use the matrix of that
        #class. it is negative because everything
        #else is moving
        self.accelerate(self.acceleration)
        glTranslatef(-self.velocity[0],-self.velocity[1],-self.velocity[2])
