import framebufferio
import displayio
import random
from layer import Layer
import color


class Food(Layer):

    def __init__(self, framebuffer: framebufferio.FramebufferDisplay, container: displayio.Group):
        super().__init__(framebuffer, container)
        self.new()

    def new(self):
        self.position = (random.randint(0, self._bitmap.width - 1), random.randint(0, self._bitmap.height - 1))
        self.color = color.rnd()
        self._bitmap.fill(color.non)
        self._bitmap[self.position] = self.color
