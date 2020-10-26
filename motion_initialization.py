#import pigpio
#pi = pigpio.pi()


# this is a module in which the intializations of the motor and its direction of motion


class addmotor:
    def __init__ (self ,gpiopin) :
        self.pin = gpiopin
        #pi.set_servo_pulsewidth(self.pin,1500)     #intializing the motor to stop signal to triger the esc
        print("motor is intailised with speed zero at pin :",self.pin)
   
    def stop(self) :                                #stopping the motor
        #pi.set_servo_pulsewidth(self.pin,1500)
        print("motor at pin :",self.pin,"is stopped ")
    def cw (self,speed_lvl):                        #launching the motor in clock wise rotation
        self.speed =speed_lvl
        #pi.set_servo_pulsewidth(self.pin,self.speed)
        print("motor at pin :",self.pin," is moving clockwise with speed:",self.speed )
    def ccw (self,speed_lvl):                        #launching the motor in counter clock wise rotation
        self.speed =speed_lvl
        #pi.set_servo_pulsewidth(self.pin,self.speed)
        print("motor at pin :",self.pin," is moving counter clockwise with speed:",self.speed )
