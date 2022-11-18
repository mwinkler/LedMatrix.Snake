import displayio
import random
import color
from food import Food
from layer import Layer
from ticker import Ticker
from controller import Controller

class Snake(Layer):
    
    def __init__(self, width: int, height: int, container: displayio.Group):
        super().__init__(width, height, container)
        self.reset()

    
    def reset(self):
        self.bitmap.fill(color.non)
        self.head = (random.randint(5, self.bitmap.width - 5), random.randint(5, self.bitmap.height - 5)) # (x, y)
        self.direction = (1, 0)    # (x, y)
        self.color = color.rnd()
        self.body = [self.head]
        self.length = 5
        self.collision = False
        self.speed = 3  # pixel per second
        self.ticker = Ticker()

    
    def tick(self, controller: Controller, food: Food):
        # abort if not enough ticks are elapsed for next move
        if (self.ticker.elapsed() < 1000.0 / self.speed):
            return
        else:
            self.ticker.reset()

        # handle controller input
        self._process_controller(controller)

        # move snake
        self._move()

        # check collisions
        self._check_collision_border_and_self()
        self._check_collision_food(food)

        # render
        self._render()

    
    def _process_controller(self, controller: Controller):
        # get controller input
        (direction, button_top, button_bottom) = controller.poll()

        # increase speed when button pressed
        self.speed = 10 if button_bottom else 3

        # ignore when no direction is set
        if (direction == (0, 0)):
            return

        # prevent reverse direction
        if (self.direction[0] - direction[0] in [-2, 2] or self.direction[1] - direction[1] in [-2, 2]):
            return
        
        self.direction = direction


    def _move(self):
        # set head by direction
        self.head = (self.head[0] + self.direction[0], self.head[1] + self.direction[1])

        # add head to body
        self.body.append(self.head)

        # delete snake tail
        if (len(self.body) > self.length):
            self.body.pop(0)


    def _check_collision_food(self, food: Food):
        if (food.position == self.head):
            self.length += 1
            food.new_position()


    def _check_collision_border_and_self(self):
        # border x
        if (self.head[0] < 0 or self.head[0] >= self.bitmap.width):
            self.collision = True
        
        # border y
        if (self.head[1] < 0 or self.head[1] >= self.bitmap.height):
            self.collision = True

        # check head collide with own body
        if (self.head in self.body[:-1]):
            self.collision = True


    def _render(self):
        # stop render on collion
        if (self.collision):
            return

        # clear
        self.bitmap.fill(color.non)

        # draw snake
        for pos in self.body:
            self.bitmap[pos] = self.color

        