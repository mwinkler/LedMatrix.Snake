import displayio
import random

palette = displayio.Palette(5)
palette[0] = 0x000000   # black
palette[1] = 0x00FF00   # green
palette[2] = 0xFF0000   # red
palette[3] = 0x0000FF   # blue
palette[4] = 0xFFFF00   # yellow
palette.make_transparent(0)

non = palette[0]
green = palette[1]
red = palette[2]
blue = palette[3]
yellow = palette[4]
count = len(palette)

def rnd():
    return random.randint(1, count - 1)
