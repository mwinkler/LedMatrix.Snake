import board
import time
import displayio
from adafruit_matrixportal.matrix import Matrix
from controller import Controller
from snake import Snake
from food import Food

matrix = Matrix(width=32, height=32)
contoller = Controller(board.I2C())
group = displayio.Group()
snake = Snake(matrix.display, group)
food = Food(matrix.display, group)

matrix.display.show(group)

while True:
    
    contoller.tick()
    snake.tick(contoller, food)

    if (snake.collision):
        snake.reset()

    time.sleep(0.01)
