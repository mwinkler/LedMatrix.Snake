import board
import time
import displayio
from adafruit_matrixportal.matrix import Matrix
from controller import Controller
from snake import Snake

# init display
#matrix = Matrix(width=32, height=32)

frame_counter = 0
game_tick = 10

contoller = Controller(board.I2C())
#snake = Snake(matrix.display)

#matrix.display.show()

while True:
    
    frame_counter += 1

    if (frame_counter > game_tick):
        
        # reset frame counter
        frame_counter = 0

        #snake.move()

        # eat food
        # if (snake_pos == food_pos):
        #     snake_color = food_color
        #     food_pos = create_food()
        #     food_color = get_random_color()
        #     snake_length += 2


        # gard sname pos
        # if (snake_pos[0] < 0):
        #     snake_pos = (FIELD_WIDTH - 1, snake_pos[1])
        # if (snake_pos[0] >= FIELD_WIDTH):
        #     snake_pos = (0, snake_pos[1])
        # if (snake_pos[1] < 0):
        #     snake_pos = (snake_pos[0], FIELD_HEIGHT - 1)
        # if (snake_pos[1] >= FIELD_HEIGHT):
        #     snake_pos = (snake_pos[0], 0)

        print(contoller.get_direction())


    time.sleep(0.01)
