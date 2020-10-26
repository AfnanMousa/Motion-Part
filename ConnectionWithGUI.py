from Directions import Direction


class ControlMotion:
    def __init__(self):
       self.x=Direction()
       return
    def DirectionofTravel(self,t,speed_lvl):
        if(t==1):
            self.x.forward(speed_lvl)
        elif (t == 2):
            self.x.Backward(speed_lvl)
        return


y=ControlMotion()
y.DirectionofTravel(2,1550)