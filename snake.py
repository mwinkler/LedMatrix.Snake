import displayio
import random
import color
from layer import Layer

class Snake(Layer):
    
    def __init__(self, width: int, height: int, container: displayio.Group) -> None:
        super().__init__(width, height, container)

        self.reset()

    
    def reset(self):
        self.head = (random.randint(5, self.bitmap.width - 5), random.randint(5, self.bitmap.height - 5)) # (x, y)
        self.direction = (0, 0)    # (x, y)
        self.color = color.rnd()
        self.body = [self.head]  # array with all
        self.length = 5

    
    def set_direction(self, direction: tuple[int, int]):
        # prevent reverse direction
        #if (self.direction[0] - direction[0] in [-2, 0] or self.direction[1] - direction[1] in [-2, 0]):
        #    return
        if (direction == (0, 0)):
            return
        
        self.direction = direction


    def move(self):
        # delete snake tail
        if (len(self.body) > self.length):
            snake_tail = self.body.pop(0)
            self.bitmap[snake_tail] = color.non

        # set new snake head position and add to body
        self.head = (self.head[0] + self.direction[0], self.head[1] + self.direction[1])
        self.body.append(self.head)

        # render snake head
        self.bitmap[self.head] = self.color

        