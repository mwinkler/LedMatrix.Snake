import board
import time
from adafruit_matrixportal.matrix import Matrix
import random
from analogio import AnalogIn


# init display
FIELD_WIDTH = 32
FIELD_HEIGHT = 32
matrix = Matrix(width=FIELD_WIDTH, height=FIELD_HEIGHT)

frame_counter = 0
game_tick = 10

while True:
    
    frame_counter += 1

    if (frame_counter > game_tick):
        
        # reset frame counter
        frame_counter = 0

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



    time.sleep(0.01)
