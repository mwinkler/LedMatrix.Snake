import framebufferio
import displayio
import color

class Layer():

   def __init__(self, framebuffer: framebufferio.FramebufferDisplay, container: displayio.Group):
      self._framebuffer = framebuffer
      self._bitmap = displayio.Bitmap(framebuffer.width, framebuffer.height, color.count)
      self._tile = displayio.TileGrid(self._bitmap, pixel_shader=color.palette)
      container.append(self._tile)