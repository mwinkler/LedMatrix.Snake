import framebufferio
import displayio
import color

class Layer():

     def __init__(self, framebuffer: framebufferio.FramebufferDisplay) -> None:
        self.framebuffer = framebuffer
        self.bitmap = displayio.Bitmap(framebuffer.width, framebuffer.height, color.count)
        self.tile = displayio.TileGrid(self.bitmap, pixel_shader=color.palette)
        
        framebuffer.root_group.append(self.tile)