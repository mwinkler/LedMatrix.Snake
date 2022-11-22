import time
import displayio
from adafruit_matrixportal.matrix import Matrix
import helper
from game import Game
from adafruit_display_text import label
import terminalio
import board
import busio
import adafruit_tca9548a

with busio.I2C(board.SCL, board.SDA) as i2c:

    helper.i2c_channels = adafruit_tca9548a.TCA9548A(i2c)
    helper.matrix = Matrix(width=64, height=32, color_order="GBR")
    helper.framegroup = displayio.Group()
    helper.matrix.display.show(helper.framegroup)

    game = Game()
    game.add_player()

    text = label.Label(terminalio.FONT, text="Hello")
    text.x = 1
    text.y = 4
    helper.framegroup.insert(0, text)

    while True:
        
        game.tick()

        time.sleep(0.05)