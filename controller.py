import busio
import adafruit_nunchuk

class Controller():

    def __init__(self, i2c: busio.I2C):
        self.nc = adafruit_nunchuk.Nunchuk(i2c)
        self.direction = (0, 0)

    def update(self):
        # x: left=28, center=123, right=225
        # y: top=227, center=132, down=36
        (x ,y) = self.nc.joystick
        
        if (x < 80):
            self.direction = (-1, 0)
        elif (x > 170):
            self.direction = (1, 0)
        elif (y < 80):
            self.direction = (0, 1)
        elif (y > 170):
            self.direction = (0, -1)
        else:
            self.direction = (0, 0)