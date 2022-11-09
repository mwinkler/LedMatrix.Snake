import board
import displayio
import time
from adafruit_matrixportal.matrix import Matrix
import random
from analogio import AnalogIn

def create_food():
    return (random.randint(0, FIELD_WIDTH), random.randint(0, FIELD_HEIGHT))
def get_random_color():
    return random.randint(1, 4)

# init display
FIELD_WIDTH = 32
FIELD_HEIGHT = 32
matrix = Matrix(width=FIELD_WIDTH, height=FIELD_HEIGHT)

# colors
palette = displayio.Palette(5)
palette[0] = 0x000000   # black
palette[1] = 0x00FF00   # green
palette[2] = 0xFF0000   # red
palette[3] = 0x0000FF   # blue
palette[4] = 0xFFFFDD   # yellow

# play field
grid = displayio.Bitmap(FIELD_WIDTH, FIELD_HEIGHT, len(palette))
field_tile = displayio.TileGrid(grid, pixel_shader=palette)

# snake
snake_pos = (int(FIELD_WIDTH / 2), int(FIELD_HEIGHT / 2)) # (x, y)
snake_direction = (1, 0)    # (x, y)
snake_color = get_random_color()
snake_body = [snake_pos]
snake_length = 5
snake_speed = 20 
food_pos = create_food()
food_color = get_random_color()

# init display
group = displayio.Group(scale=1)
group.append(field_tile)
matrix.display.show(group)

# init joystick
joy_y = AnalogIn(board.A1) # 0=up   65k=down
joy_x = AnalogIn(board.A2) # 0=rigt 65k=left

frame_counter = 0

while True:
    
    frame_counter += 1

    # read joystick position
    if (joy_y.value > 50000 and snake_direction != (0, -1)):
        snake_direction = (0, 1)
    elif (joy_y.value < 20000 and snake_direction != (0, 1)):
        snake_direction = (0, -1)
    elif (joy_x.value > 50000 and snake_direction != (1, 0)):
        snake_direction = (-1, 0)
    elif (joy_x.value < 20000 and snake_direction != (-1, 0)):
        snake_direction = (1, 0)

    if (frame_counter > snake_speed):
        
        # reset frame counter
        frame_counter = 0

        # delete snake tail
        if (len(snake_body) > snake_length):
            snake_tail = snake_body.pop(0)
            grid[snake_tail] = 0


        # display food
        grid[food_pos] = food_color

        # eat food
        if (snake_pos == food_pos):
            snake_color = food_color
            food_pos = create_food()
            food_color = get_random_color()
            snake_length += 2

        # render snake pos
        grid[snake_pos] = snake_color
        
        # new snake pos
        snake_pos = (snake_pos[0] + snake_direction[0], snake_pos[1] + snake_direction[1])

        # gard sname pos
        if (snake_pos[0] < 0):
            snake_pos = (FIELD_WIDTH - 1, snake_pos[1])
        if (snake_pos[0] >= FIELD_WIDTH):
            snake_pos = (0, snake_pos[1])
        if (snake_pos[1] < 0):
            snake_pos = (snake_pos[0], FIELD_HEIGHT - 1)
        if (snake_pos[1] >= FIELD_HEIGHT):
            snake_pos = (snake_pos[0], 0)

        snake_body.append(snake_pos)


    time.sleep(0.01)
