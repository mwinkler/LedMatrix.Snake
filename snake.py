import random
import color
from food import Food
from layer import Layer
from ticker import Ticker
from controller import Controller
import helper

class Snake(Layer):
    
    def __init__(self):
        super().__init__()
        self.reset()

    
    def reset(self):
        self.bitmap.fill(color.non)
        self.direction = (1, 0)    # (x, y)
        self.body = [(random.randint(5, self.bitmap.width - 5), random.randint(5, self.bitmap.height - 5))]
        self.length = 5
        self.color = [color.pink] + [color.blue for _ in range(self.length - 1)]
        self.collision = False
        self.speed_fast = 15    # pixel per second
        self.speed_default = 3  # pixel per second
        self.speed = self.speed_default
        self.ticker = Ticker()

    
    def tick(self, controller: Controller, food: Food):
        # wait until next render cycle by snake speed
        if (self.ticker.elapsed() < 1000.0 / self.speed):
            return
        else:
            self.ticker.reset()

        # handle controller input
        self.handle_controller_input(controller)

        # move snake
        self.move()

        # check collisions
        self.check_collision_border_and_self()
        self.check_collision_food(food)

        # render
        self.render()

    
    def handle_controller_input(self, controller: Controller):
        # poll last controller input
        state = controller.poll()

        # increase speed when button pressed
        self.speed = self.speed_fast if state.button_bottom else self.speed_default

        # abort when no direction is set
        if (state.direction == (0, 0)):
            return

        # ignore current direction from controller (prevent reverse)
        if (self.direction[0] == 0 and state.direction[0] != 0):
            self.direction = (state.direction[0], 0)
        elif (self.direction[1] == 0 and state.direction[1] != 0):
            self.direction = (0 ,state.direction[1])


    def move(self):
        # set new head position by direction
        head = (self.body[-1][0] + self.direction[0], self.body[-1][1] + self.direction[1])

        # add new head to body
        self.body.append(head)

        # delete snake tail
        if (len(self.body) > self.length):
            self.body.pop(0)


    def check_collision_food(self, food: Food):
        # check if head is on food position
        if (food.position == self.body[-1]):
            self.length += 1
            self.color.append(food.color)  # add eaten food color as to snake tail
            food.new()


    def check_collision_border_and_self(self):
        # leave head screen x
        if (self.body[-1][0] < 0 or self.body[-1][0] >= self.bitmap.width):
            self.collision = True
        
        # leave head screen y
        if (self.body[-1][1] < 0 or self.body[-1][1] >= self.bitmap.height):
            self.collision = True

        # check if head collide with own body
        if (self.body[-1] in self.body[:-1]):
            self.collision = True


    def render(self):
        # stop render on collision
        if (self.collision):
            return

        # disable auto refresh while drawing the snake
        helper.matrix.display.auto_refresh = False

        # clear screen
        self.bitmap.fill(color.non)

        # draw snake
        for i in range(len(self.body)):
            self.bitmap[self.body[-1 - i]] = self.color[i]

        # reenable auto refresh
        helper.matrix.display.auto_refresh = True
