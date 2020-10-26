from Directions import Direction
import time
#from client import *
speed_lvl =1500
CurrentDirection=""
class ControlMotion:
    def __init__(self):
       self.temp=Direction()
       return
    def DirectionofTravel(self,msg):
        array = msg.split()
        global speed_lvl
        global CurrentDirection
        if(array[0]=="move"):
            if(array[1]=="forward"):                   #forward
               self.temp.forward(speed_lvl)
               CurrentDirection="forward"
            
            elif(array[1]=="backward"):                #backward
                self.temp.Backward(speed_lvl)
                CurrentDirection = "backward"
            
            elif(array[1]=="right"):                   #slide right
                self.temp.Right(speed_lvl)
                CurrentDirection = "right"
           
            elif(array[1]=="left"):                    #slide left
                self.temp.Left(speed_lvl)
                CurrentDirection = "left"
            
            elif(array[1]=="up"):                      #upward
                self.temp.Up(speed_lvl)
                CurrentDirection = "up"
            
            elif(array[1]=="down"):                    #downward
                self.temp.Down(speed_lvl)
                CurrentDirection = "down"

            elif(array[1]=="rolltoright"):             #rolling clockwise
                self.temp.RollToRight(speed_lvl)
                CurrentDirection = "rolltoright"

            elif(array[1]=="rolltoleft"):              #rolling counterclockwise
                self.temp.RollToLeft(speed_lvl)
                CurrentDirection = "rolltoleft"    
            
            elif(array[1]=="pitchup"):                 #pitching up
                self.temp.PitchUp(speed_lvl)
                CurrentDirection = "pitchup"

            elif(array[1]=="pitchdown"):               #pitching down
                self.temp.PitchDown(speed_lvl)
                CurrentDirection = "pitchdown"

            elif(array[1]=="yawcw"):                   #rotating right 
                self.temp.YawCw(speed_lvl)
                CurrentDirection = "yawcw"

            elif(array[1]=="yawccw"):                  #rotating left 
                self.temp.YawCCw(speed_lvl)
                CurrentDirection = "yawccw"
            elif(array[1]== "stop"):
                self.temp.Stop()                       #motors stopped

        ###############################################################
        
        elif(array[0]=="speed"):
            z=1500
            if (CurrentDirection == "forward"):
                self.temp.forward(int(array[1])+z)
            elif (CurrentDirection == "backward"):
                self.temp.Backward(array[1]+z)
            # all motion ......
            #speed_lvl = array[1] + z
        return

#print (msg)
y=ControlMotion()
y.DirectionofTravel("move forward")
print("waitagain")
time.sleep (5)
y.DirectionofTravel("speed 30")
