import displayio
import random
from layer import Layer
import color


class Food(Layer):

    def __init__(self, field_width: int, field_height: int, container: displayio.Group):
        super().__init__(field_width, field_height, container)
        self.new_position()

    def new_position(self):
        self.position = (random.randint(0, self.bitmap.width - 1), random.randint(0, self.bitmap.height - 1))
        self.color = color.rnd()
        self.bitmap.fill(color.non)
        self.bitmap[self.position] = self.color
