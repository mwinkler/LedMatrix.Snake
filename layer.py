import framebufferio
import displayio
import color

class Layer():

   def __init__(self, width: int, height: int, container: displayio.Group):
      self.bitmap = displayio.Bitmap(width, height, color.count)
      self.tile = displayio.TileGrid(self.bitmap, pixel_shader=color.palette)
      container.append(self.tile)