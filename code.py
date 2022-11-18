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
snake = Snake(matrix.display.width, matrix.display.height, group)
food = Food(matrix.display.width, matrix.display.height, group)

matrix.display.show(group)

while True:
    
    contoller.update()
    snake.tick(contoller, food)

    if (snake.collision):
        snake.reset()

        # gard sname pos
        # if (snake_pos[0] < 0):
        #     snake_pos = (FIELD_WIDTH - 1, snake_pos[1])
        # if (snake_pos[0] >= FIELD_WIDTH):
        #     snake_pos = (0, snake_pos[1])
        # if (snake_pos[1] < 0):
        #     snake_pos = (snake_pos[0], FIELD_HEIGHT - 1)
        # if (snake_pos[1] >= FIELD_HEIGHT):
        #     snake_pos = (snake_pos[0], 0)

        #print(contoller.get_direction())


    time.sleep(0.01)
