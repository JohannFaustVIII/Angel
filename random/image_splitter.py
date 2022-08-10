from PIL import Image
from itertools import product
import os
import sys

def tile(filename, dir_out, d):
    name, ext = os.path.splitext(filename)
    img = Image.open(filename)
    w, h = img.size
    
    grid = product(range(0, h-h%d, d), range(0, w-w%d, d))
    for i, j in grid:
        box = (j, i, j+d, i+d)
        out = os.path.join(dir_out, f'result_{i}_{j}{ext}')
        print(out)
        img.crop(box).save(out)

input = sys.argv[1]
dir_out = sys.argv[2]
d = 600

print(input)
print(dir_out)

tile(input, dir_out, 600)