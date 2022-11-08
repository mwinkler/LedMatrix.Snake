import board
import displayio
import adafruit_imageload
import time
from adafruit_matrixportal.matrix import Matrix

# init display
matrix = Matrix(width=32, height=32)

# load image
#displayio.OnDiskBitmap()
sprite_sheet, palette = adafruit_imageload.load("tiles.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)
palette.make_transparent(0)

# create group and tile group
group = displayio.Group()
tile = displayio.TileGrid(sprite_sheet, pixel_shader=palette)
group.append(tile)

# show
#print(dir(matrix.display))
matrix.display.show(group)
#matrix.display.root_group.append(tile)
#matrix.display.show()

while True:
    time.sleep(1)