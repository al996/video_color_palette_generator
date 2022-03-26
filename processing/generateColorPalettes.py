import csv
import os
import PIL
from PIL import Image
import glob
import numpy as np
import webcolors
from colorthief import ColorThief
import datetime

def palette(img):
    """
    Return palette in descending order of frequency
    """
    arr = np.asarray(img)
    palette, index = np.unique(asvoid(arr).ravel(), return_inverse=True)
    palette = palette.view(arr.dtype).reshape(-1, arr.shape[-1])
    count = np.bincount(index)
    order = np.argsort(count)
    return palette[order[::-1]]

def asvoid(arr):
    """View the array as dtype np.void (bytes)
    This collapses ND-arrays to 1D-arrays, so you can perform 1D operations on them.
    http://stackoverflow.com/a/16216866/190597 (Jaime)
    http://stackoverflow.com/a/16840350/190597 (Jaime)
    Warning:
    >>> asvoid([-0.]) == asvoid([0.])
    array([False], dtype=bool)
    """
    arr = np.ascontiguousarray(arr)
    return arr.view(np.dtype((np.void, arr.dtype.itemsize * arr.shape[-1])))

def ColorPalette(writer, dirPath):
    path = os.path.join(dirPath, "*.jpg")
    for filename in glob.glob(path):
        idx = os.path.basename(filename).split('.')[0]
        color_thief = ColorThief(filename)
        palette = color_thief.get_palette(color_count=5)
        row =[idx, str(datetime.timedelta(seconds=int(idx)*5))]
        for color in palette:
          row.append(webcolors.rgb_to_hex(color))
        print(row)
        writer.writerow(row)
  

if __name__ == '__main__':
    f = open('color_palette.csv', 'w', encoding='UTF8')
    writer = csv.writer(f)
    
    header = ["id", "time", "color_1", "color_2", "color_3", "color_4", "color_5"]
    writer.writerow(header)

    ColorPalette(writer, "SpiritedAway")

    f.close()
        