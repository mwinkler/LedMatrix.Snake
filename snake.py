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
        self.direction = (0, 0)    # (x, y)
        self.color = color.rnd()
        self.body = [self.head]
        self.length = 5
        self.collision = False
        self.speed = 3  # pixel per second
        self.ticker = Ticker()

    
    def process_controller(self, controller: Controller):
        
        self.speed = 10 if controller.button_bottom else 3

        # ignore when no direction is set
        if (controller.direction == (0, 0)):
            return

        # prevent reverse direction
        if (self.direction[0] - controller.direction[0] in [-2, 2] or self.direction[1] - controller.direction[1] in [-2, 2]):
            return
        
        self.direction = controller.direction


    def move(self):
        # do nothing, if not enough ticks are elapsed
        if (self.ticker.elapsed() < 1000.0 / self.speed):
            return

        # reset ticker
        self.ticker.reset()

        # set head by direction
        self.head = (self.head[0] + self.direction[0], self.head[1] + self.direction[1])

        # add head to body
        self.body.append(self.head)


    def check_collision(self):
        self.collision = self.__check_collision(None)
        if (self.collision):
            self.reset()
        return self.collision


    def check_food(self, food: Food):
        if (food.position == self.head):
            self.length += 1
            food.new_position()


    def __check_collision(self, object: list[tuple[int, int]]):
        # border x
        if (self.head[0] < 0 or self.head[0] >= self.bitmap.width):
            return True
        
        # border y
        if (self.head[1] < 0 or self.head[1] >= self.bitmap.height):
            return True

        return False


    def render(self):
        # stop render on collion
        if (self.collision):
            return

        # delete snake tail
        if (len(self.body) > self.length):
            snake_tail = self.body.pop(0)
            self.bitmap[snake_tail] = color.non
        
        # render snake head
        self.bitmap[self.head] = self.color

        