import board
import displayio
import adafruit_imageload
from adafruit_matrixportal.matrix import Matrix

# init display
matrix = Matrix(width=32, height=32)

# load image
#displayio.OnDiskBitmap()
sprite_sheet, palette = adafruit_imageload.load("tiles.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)
palette.make_transparent(0)

# create tile group
tile = displayio.TileGrid(sprite_sheet, pixel_shader=palette)

# show
matrix.display.root_group.append(tile)
matrix.display.show()

