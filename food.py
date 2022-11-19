import random
from layer import Layer
import color

class Food(Layer):

    def __init__(self):
        super().__init__()
        self.new()

    def new(self):
        self.position = (random.randint(0, self.bitmap.width - 1), random.randint(0, self.bitmap.height - 1))
        self.color = color.rnd()
        self.bitmap.fill(color.non)
        self.bitmap[self.position] = self.color
