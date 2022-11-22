import adafruit_nunchuk
from collections import namedtuple
import helper

ControllerState = namedtuple("ControllerState", "direction button_top button_bottom")

class Controller():
    "Use poll() to get last input"

    def __init__(self, channel: int):
        self.nc = adafruit_nunchuk.Nunchuk(helper.i2c_channels[0])
        self.reset()

    def reset(self):
        self.direction = (0, 0)
        self.button_top = False
        self.button_bottom = False

    def tick(self):
        # x: left=28, center=123, right=225
        # y: top=227, center=132, down=36
        (x ,y) = self.nc.joystick
        
        cx = -1 if x < 80 else 1 if x > 170 else self.direction[0]
        cy = 1 if y < 80 else -1 if y > 170 else self.direction[1]
        self.direction = (cx, cy)

        # button top
        if (self.nc.buttons[0]):
            self.button_top = True

        # button bottom
        if (self.nc.buttons[1]):
            self.button_bottom = True

    def poll(self):
        ret = ControllerState(self.direction, self.button_top, self.button_bottom)
        self.reset()
        return ret
