import board
import displayio
import adafruit_imageload
import time
from adafruit_matrixportal.matrix import Matrix
import random

# init display
FIELD_WIDTH = 32
FIELD_HEIGHT = 32
matrix = Matrix(width=FIELD_WIDTH, height=FIELD_HEIGHT)

# load image
#displayio.OnDiskBitmap()
sprite_sheet, palette = adafruit_imageload.load("tiles.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)
palette.make_transparent(0)

# create group and tile group
tiles = list(map(lambda i: displayio.TileGrid(sprite_sheet, pixel_shader=palette, tile_width=4, default_tile=i), range(5)))

group = displayio.Group(scale=1)

for tile in tiles:
    group.append(tile)
    
# show
matrix.display.show(group)

#tile.transpose_xy = True

while True:
    for tile in tiles:
        tile.x = min(FIELD_HEIGHT - 4, max(0, tile.x + random.randrange(-1, 2)))
        tile.y = min(FIELD_HEIGHT - 4, max(0, tile.y + random.randrange(-1, 2)))
    time.sleep(0.05)
