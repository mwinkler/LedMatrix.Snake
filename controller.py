import adafruit_nunchuk
import time
from collections import namedtuple

ControllerState = namedtuple("ControllerState", ["direction", "button_top", "button_bottom"])

class Controller():
    "Use poll() to get last input"

    def __init__(self, nunchuck: adafruit_nunchuk.Nunchuk):
        self.nc = nunchuck
        self.reset()

    def reset(self):
        self.direction = (0, 0)
        self.button_top = False
        self.button_bottom = False

    def tick(self):
        
        # get values (polling)
        values = self.nc.values

        # get joystick value
        # x: left=28, center=123, right=225
        # y: top=227, center=132, down=36
        (x ,y) = values.joystick
        
        # translate axis value to -1 or 1
        # if axis is in central, keep direction (until poll resets it to 0)
        # this is needed to remember joystick direction between game ticks
        cx = -1 if x < 80 else 1 if x > 170 else self.direction[0]
        cy = 1 if y < 80 else -1 if y > 170 else self.direction[1]
        self.direction = (cx, cy)

        # button top
        if (values.buttons[0]):
            self.button_top = True

        # button bottom
        if (values.buttons[1]):
            self.button_bottom = True

    def poll(self):
        ret = ControllerState(self.direction, self.button_top, self.button_bottom)
        self.reset()
        return ret
