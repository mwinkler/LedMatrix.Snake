import framebufferio
import displayio
from color import Color

class Layer():

     def __init__(self, framebuffer: framebufferio.FramebufferDisplay) -> None:
        self.framebuffer = framebuffer
        self.bitmap = displayio.Bitmap(framebuffer.width, framebuffer.height, Color.count)
        self.tile = displayio.TileGrid(self.bitmap, pixel_shader=Color.palette)
        self.group = displayio.Group(scale=1)
        
        self.group.append(self.tile)
        framebuffer.show(self.group)
        
        