import time
import displayio
from adafruit_matrixportal.matrix import Matrix
import helper
from game import Game

helper.matrix = Matrix(width=64, height=32, color_order="GBR")
helper.framegroup = displayio.Group()
helper.matrix.display.show(helper.framegroup)

game = Game()
game.add_player()

while True:
    
    game.tick()

    time.sleep(0.01)