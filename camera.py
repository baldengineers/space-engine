#contains the camera class

class Camera():
    def __init__(self,x,y,z,acceleration,direction):
        self.x = x
        self.y = y
        self.z = z

        self.acceleration = acceleration
        self.direction = direction
        self.velocity = 0
        
    def update_dir(self, direction, axis):
        #vector can be 'x', 'y', 'z', 'xy', 'xz', etc.
        glRotatef(direction, 1 if 'x' in axis else 0, 1 if 'y' in axis else 0, 1 if 'z' in axis)
        
    def update_pos(self, amount)
        glTranslate(amount[0], amount[1], amount[2])
