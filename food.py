import framebufferio
import random
from layer import Layer
from color import Color


class Food(Layer):

    def __init__(self, framebuffer: framebufferio.FramebufferDisplay) -> None:
        super().__init__(framebuffer)
        self.new_position()

    def new_position(self):
        self.position = (random.randint(0, self.framebuffer.width - 1), random.randint(0, self.framebuffer.height - 1))
        self.color = Color.random()

    def render(self):
        self.bitmap[self.position] = self.color
