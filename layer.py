import displayio
import color
import helper

class Layer():

   def __init__(self):
      self.bitmap = displayio.Bitmap(helper.matrix.display.width, helper.matrix.display.height, color.count)
      self.tile = displayio.TileGrid(self.bitmap, pixel_shader=color.palette)
      helper.framegroup.append(self.tile)