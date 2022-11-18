import busio
import adafruit_nunchuk

class Controller():

    def __init__(self, i2c: busio.I2C):
        self.nc = adafruit_nunchuk.Nunchuk(i2c)
        self._reset()

    def _reset(self):
        self._direction = (0, 0)
        self._button_top = False
        self._button_bottom = False

    def tick(self):
        # x: left=28, center=123, right=225
        # y: top=227, center=132, down=36
        (x ,y) = self.nc.joystick
        
        if (x < 80):
            self._direction = (-1, 0)
        elif (x > 170):
            self._direction = (1, 0)
        elif (y < 80):
            self._direction = (0, 1)
        elif (y > 170):
            self._direction = (0, -1)

        if (self.nc.buttons[0]):
            self._button_top = True
        if (self.nc.buttons[1]):
            self._button_bottom = True

    def poll(self):
        ret = (self._direction, self._button_top, self._button_bottom)
        self._reset()
        return ret
