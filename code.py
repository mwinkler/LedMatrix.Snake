import board
import time
import displayio
import helper
from adafruit_matrixportal.matrix import Matrix
import bitbangio
import adafruit_nunchuk
from game import Game

with bitbangio.I2C(board.A1, board.A2) as i2c:

    nunchuck1 = adafruit_nunchuk.Nunchuk(board.I2C())
    nunchuck2 = adafruit_nunchuk.Nunchuk(i2c)

    helper.matrix = Matrix(width=64, height=32, color_order="GBR")
    helper.framegroup = displayio.Group()
    helper.matrix.display.show(helper.framegroup)

    game = Game()
    game.add_player(nunchuck1)
    game.add_player(nunchuck2)

    while True:
        
        game.tick()
        #print(nunchuck1.values)

        time.sleep(0.05)