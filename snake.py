import displayio
import framebufferio
import random
import color
from food import Food
from layer import Layer
from ticker import Ticker
from controller import Controller

class Snake(Layer):
    
    def __init__(self, framebuffer: framebufferio.FramebufferDisplay, container: displayio.Group):
        super().__init__(framebuffer, container)
        self.reset()

    
    def reset(self):
        self._bitmap.fill(color.non)
        self.direction = (1, 0)    # (x, y)
        self.body = [(random.randint(5, self._bitmap.width - 5), random.randint(5, self._bitmap.height - 5))]
        self.length = 5
        self.color = [color.pink] + [color.blue for _ in range(self.length - 1)]
        self.collision = False
        self.speed_fast = 15    # pixel per second
        self.speed_default = 3  # pixel per second
        self.speed = self.speed_default
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
        # poll last controller input
        state = controller.poll()

        # increase speed when button pressed
        self.speed = self.speed_fast if state.button_bottom else self.speed_default

        # abort when no direction is set
        if (state.direction == (0, 0)):
            return

        # abort when player tries to invert direction
        if (self.direction[0] - state.direction[0] in [-2, 2] or self.direction[1] - state.direction[1] in [-2, 2]):
            return
        
        # set new snake direction
        self.direction = state.direction


    def _move(self):
        # set head by direction
        next = (self.body[-1][0] + self.direction[0], self.body[-1][1] + self.direction[1])

        # add next to body
        self.body.append(next)

        # delete snake tail
        if (len(self.body) > self.length):
            self.body.pop(0)


    def _check_collision_food(self, food: Food):
        if (food.position == self.body[-1]):
            self.length += 1
            self.color.append(food.color)
            food.new()


    def _check_collision_border_and_self(self):
        # leave screen x
        if (self.body[-1][0] < 0 or self.body[-1][0] >= self._bitmap.width):
            self.collision = True
        
        # leave screen y
        if (self.body[-1][1] < 0 or self.body[-1][1] >= self._bitmap.height):
            self.collision = True

        # check if head collide with own body
        if (self.body[-1] in self.body[:-1]):
            self.collision = True


    def _render(self):
        # stop render on collision
        if (self.collision):
            return

        # disable auto refresh while drawing the snake
        self._framebuffer.auto_refresh = False

        # clear screen
        self._bitmap.fill(color.non)

        # draw snake
        for i in range(len(self.body)):
            self._bitmap[self.body[-1 - i]] = self.color[i]

        # reenable auto refresh
        self._framebuffer.auto_refresh = True
