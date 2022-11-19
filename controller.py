import adafruit_nunchuk
import board
from collections import namedtuple

ControllerState = namedtuple("ControllerState", "direction button_top button_bottom")

class Controller():
    "Use poll() to get last input"

    def __init__(self):
        self.nc = adafruit_nunchuk.Nunchuk(board.I2C())
        self.reset()

    def reset(self):
        self.direction = (0, 0)
        self.button_top = False
        self.button_bottom = False

    def tick(self):
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

        if (self.nc.buttons[0]):
            self.button_top = True

        if (self.nc.buttons[1]):
            self.button_bottom = True

    def poll(self):
        ret = ControllerState(self.direction, self.button_top, self.button_bottom)
        self.reset()
        return ret
