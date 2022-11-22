import displayio
import busio
from adafruit_matrixportal.matrix import Matrix
import adafruit_tca9548a

matrix: Matrix = None
framegroup: displayio.Group = None
i2c_channels: adafruit_tca9548a.TCA9548A = None