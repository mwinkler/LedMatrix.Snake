import busio
import adafruit_nunchuk

class Controller():

    def __init__(self, i2c: busio.I2C) -> None:
        self.nc = adafruit_nunchuk.Nunchuk(i2c)

    def get_direction(self) -> tuple[int, int]:
        # x: left=28, center=123, right=225
        # y: top=227, center=132, down=36
        (x ,y) = self.nc.joystick
        
        if (x < 80):
            return (-1, 0)
        if (x > 170):
            return (1, 0)
        if (y < 80):
            return (0, 1)
        if (y > 170):
            return (0, -1)
        
        return (0 , 0)