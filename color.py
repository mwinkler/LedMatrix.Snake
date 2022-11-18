import displayio
import random

palette = displayio.Palette(6)
palette[0] = 0x000000   # black
palette[1] = 0x00FF00   # green
palette[2] = 0xFF0000   # red
palette[3] = 0x0000FF   # blue
palette[4] = 0xFFFF00   # yellow
palette[5] = 0xF136FF   # pink
palette.make_transparent(0)

non = 0
green = 1
red = 2
blue = 3
yellow = 4
pink = 5
count = len(palette)

def rnd():
    return random.randint(1, count - 2)
