import busio
import adafruit_nunchuk

class Controller():

    def __init__(self, i2c: busio.I2C) -> None:
        self.nc = adafruit_nunchuk.Nunchuk(i2c)

    def get_direction(self) -> tuple[int, int]:
        (x ,y) = self.nc.joystick
        return 