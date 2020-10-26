#import pigpio
#pi = pigio.pi()
from motion_initialization import addmotor
import time 

pins = [3,5,7,11,13,15,8,10]
class Direction :
    def __init__(self):
        for i in range(8) :
          # pi.set_mode(pins[i], pigpio.INPUT)
          print("set the mode of pins",pins[i])
        self.motor1 = addmotor(pins[0])
        self.motor2 = addmotor(pins[1])
        self.motor3 = addmotor(pins[2])
        self.motor4 = addmotor(pins[3])
        self.motor5 = addmotor(pins[4])
        self.motor6 = addmotor(pins[5])
        self.motor7 = addmotor(pins[6])
        self.motor8 = addmotor(pins[7])
        print("WAITING------")
        time.sleep(3)
        print("motors are ready to work..")
        return

    # Forward:
    # 1&2 (-)
    # 3&4 (-)
    def forward(self,speed_lvl):
        print("forward direction")
        if (speed_lvl > 1900):
            speed_lvl=1900
        if(speed_lvl<1100):
            speed_lvl=1100
        if((speed_lvl<=1900)and(speed_lvl>=1100)):
            self.motor1.ccw(speed_lvl)
            self.motor2.ccw(speed_lvl)
            self.motor3.ccw(speed_lvl)
            self.motor4.ccw(speed_lvl)
            self.motor5.stop()
            self.motor6.stop()
            self.motor7.stop()
            self.motor8.stop()
        return

    # Backward:
    # 1&2 (+)
    # 3&4 (+)
    def Backward(self,speed_lvl):
        print("Backward direction")
        if (speed_lvl > 1900):
            speed_lvl=1900
        if(speed_lvl<1100):
            speed_lvl=1100
        if((speed_lvl<=1900)and(speed_lvl>=1100)):
            self.motor1.cw(speed_lvl)
            self.motor2.cw(speed_lvl)
            self.motor3.cw(speed_lvl)
            self.motor4.cw(speed_lvl)
            self.motor5.stop()
            self.motor6.stop()
            self.motor7.stop()
            self.motor8.stop()
        return

    # Right:
    # 2&3 (-)
    # 1&4 (+)
    def Right(self, speed_lvl):
        print("Right direction")
        if (speed_lvl > 1900):
            speed_lvl = 1900
        if (speed_lvl < 1100):
            speed_lvl = 1100
        if ((speed_lvl <= 1900) and (speed_lvl >= 1100)):
            self.motor1.cw(speed_lvl)
            self.motor2.ccw(speed_lvl)
            self.motor3.ccw(speed_lvl)
            self.motor4.cw(speed_lvl)
            self.motor5.stop()
            self.motor6.stop()
            self.motor7.stop()
            self.motor8.stop()
        return

# Left:
# 2&3 (+)
# 1&4 (-)
    def Left(self, speed_lvl):
        print("Left direction")
        if (speed_lvl > 1900):
            speed_lvl = 1900
        if (speed_lvl < 1100):
            speed_lvl = 1100
        if ((speed_lvl <= 1900) and (speed_lvl >= 1100)):
            self.motor1.ccw(speed_lvl)
            self.motor2.cw(speed_lvl)
            self.motor3.cw(speed_lvl)
            self.motor4.ccw(speed_lvl)
            self.motor5.stop()
            self.motor6.stop()
            self.motor7.stop()
            self.motor8.stop()
        return

# Up:
# 5&8 (-)
# 6&7 (+)
    def Up(self, speed_lvl):
        print("Up direction")
        if (speed_lvl > 1900):
            speed_lvl = 1900
        if (speed_lvl < 1100):
            speed_lvl = 1100
        if ((speed_lvl <= 1900) and (speed_lvl >= 1100)):
            self.motor1.stop()
            self.motor2.stop()
            self.motor3.stop()
            self.motor4.stop()
            self.motor5.ccw(speed_lvl)
            self.motor6.cw(speed_lvl)
            self.motor7.cw(speed_lvl)
            self.motor8.ccw(speed_lvl)
        return

# Down:
# 5&8 (+)
# 6&7 (-)
    def Down(self, speed_lvl):
        print("Down direction")
        if (speed_lvl > 1900):
            speed_lvl = 1900
        if (speed_lvl < 1100):
            speed_lvl = 1100
        if ((speed_lvl <= 1900) and (speed_lvl >= 1100)):
            self.motor1.stop()
            self.motor2.stop()
            self.motor3.stop()
            self.motor4.stop()
            self.motor5.cw(speed_lvl)
            self.motor6.ccw(speed_lvl)
            self.motor7.ccw(speed_lvl)
            self.motor8.cw(speed_lvl)
        return

# Roll to right (x):
# 7&8 (-)
# 5&6 (+)
    def RollToRight(self, speed_lvl):
        print("RollToRight direction")
        if (speed_lvl > 1900):
            speed_lvl = 1900
        if (speed_lvl < 1100):
            speed_lvl = 1100
        if ((speed_lvl <= 1900) and (speed_lvl >= 1100)):
            self.motor1.stop()
            self.motor2.stop()
            self.motor3.stop()
            self.motor4.stop()
            self.motor5.cw(speed_lvl)
            self.motor6.cw(speed_lvl)
            self.motor7.ccw(speed_lvl)
            self.motor8.ccw(speed_lvl)
        return

# Roll to left (x):
# 7&8 (+)
# 5&6 (-)
    def RollToLeft(self, speed_lvl):
        print("RollToLeft direction")
        if (speed_lvl > 1900):
            speed_lvl = 1900
        if (speed_lvl < 1100):
            speed_lvl = 1100
        if ((speed_lvl <= 1900) and (speed_lvl >= 1100)):
            self.motor1.stop()
            self.motor2.stop()
            self.motor3.stop()
            self.motor4.stop()
            self.motor5.ccw(speed_lvl)
            self.motor6.ccw(speed_lvl)
            self.motor7.cw(speed_lvl)
            self.motor8.cw(speed_lvl)
        return

# Pitch up (y):
# 5&7 (-)
# 6&8 (+)
    def PitchUp(self, speed_lvl):
        print("PitchUp direction")
        if (speed_lvl > 1900):
            speed_lvl = 1900
        if (speed_lvl < 1100):
            speed_lvl = 1100
        if ((speed_lvl <= 1900) and (speed_lvl >= 1100)):
            self.motor1.stop()
            self.motor2.stop()
            self.motor3.stop()
            self.motor4.stop()
            self.motor5.ccw(speed_lvl)
            self.motor6.cw(speed_lvl)
            self.motor7.ccw(speed_lvl)
            self.motor8.cw(speed_lvl)
        return

# Pitch down (y):
# 5&7 (+)
# 6&8 (-)
    def PitchDown(self, speed_lvl):
        print("PitchDown direction")
        if (speed_lvl > 1900):
            speed_lvl = 1900
        if (speed_lvl < 1100):
            speed_lvl = 1100
        if ((speed_lvl <= 1900) and (speed_lvl >= 1100)):
            self.motor1.stop()
            self.motor2.stop()
            self.motor3.stop()
            self.motor4.stop()
            self.motor5.cw(speed_lvl)
            self.motor6.ccw(speed_lvl)
            self.motor7.cw(speed_lvl)
            self.motor8.ccw(speed_lvl)
        return

# Yaw cw (z):
# 2&4 (-)
# 1&3 (+)
    def YawCw(self, speed_lvl):
        print("YawCw direction")
        if (speed_lvl > 1900):
            speed_lvl = 1900
        if (speed_lvl < 1100):
            speed_lvl = 1100
        if ((speed_lvl <= 1900) and (speed_lvl >= 1100)):
            self.motor1.cw(speed_lvl)
            self.motor2.ccw(speed_lvl)
            self.motor3.cw(speed_lvl)
            self.motor4.ccw(speed_lvl)
            self.motor5.stop()
            self.motor6.stop()
            self.motor7.stop()
            self.motor8.stop()
        return

# Yaw ccw (z):
# 2&4 (+)
# 1&3 (-)
    def YawCCw(self, speed_lvl):
        print("YawCCw direction")
        if (speed_lvl > 1900):
            speed_lvl = 1900
        if (speed_lvl < 1100):
            speed_lvl = 1100
        if ((speed_lvl <= 1900) and (speed_lvl >= 1100)):
            self.motor1.ccw(speed_lvl)
            self.motor2.cw(speed_lvl)
            self.motor3.ccw(speed_lvl)
            self.motor4.cw(speed_lvl)
            self.motor5.stop()
            self.motor6.stop()
            self.motor7.stop()
            self.motor8.stop()
        return

#stop
    def Stop(self):
        print("motors are stopped")
        self.motor1.stop()
        self.motor2.stop()
        self.motor3.stop()
        self.motor4.stop()
        self.motor5.stop()
        self.motor6.stop()
        self.motor7.stop()
        self.motor8.stop()

        return