import adafruit_nunchuk
import board
import busio
import adafruit_tca9548a
from collections import namedtuple

ControllerState = namedtuple("ControllerState", "direction button_top button_bottom")

#i2c = busio.I2C(board.SCL, board.SDA)
i2c = board.I2C()
# tca = adafruit_tca9548a.TCA9548A(i2c, address=0x70)

# for channel in range(8):
#     if tca[channel].try_lock():
#         print("Channel {}:".format(channel), end="")
#         addresses = tca[channel].scan()
#         print([hex(address) for address in addresses if address != 0x70])
#         tca[channel].unlock()

class Controller():
    "Use poll() to get last input"

    def __init__(self, channel: int):
        self.nc = adafruit_nunchuk.Nunchuk(i2c)
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
