import csv
import os
import PIL
from PIL import Image
import glob
import numpy as np
import webcolors
from colorthief import ColorThief
import datetime
import colorsys

def get_hsv(rgb):
    r, g, b = rgb
    return colorsys.rgb_to_hsv(r, g, b)

def ColorPalette(writer, dirPath):
    path = os.path.join(dirPath, "*.jpg")
    for filename in glob.glob(path):
        idx = os.path.basename(filename).split('.')[0]
        color_thief = ColorThief(filename)
        palette = color_thief.get_palette(color_count=5)
        palette.sort(key=get_hsv)
        row =[idx, str(datetime.timedelta(seconds=int(idx)*60))]
        for color in palette:
            row.append(webcolors.rgb_to_hex(color))
        writer.writerow(row)
  

if __name__ == '__main__':
    f = open('color_palette.csv', 'w', encoding='UTF8')
    writer = csv.writer(f)
    
    header = ["id", "time", "color_1", "color_2", "color_3", "color_4", "color_5"]
    writer.writerow(header)

    ColorPalette(writer, "SpiritedAway")

    f.close()
        