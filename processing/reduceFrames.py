import os
import PIL
from PIL import Image
import glob

def ReduceFrames(dirPath, outPath):
    path = os.path.join(dirPath, "*.jpg")
    for filename in glob.glob(path):
        idx = os.path.basename(filename).split('.')[0]
        if (int(idx) - 3) % 12 == 0:
            picture = Image.open(filename)
            id = int((int(idx) - 3) / 12)
            picture.save(outPath + "/" + str(id) + ".jpg", optimize=True,quality=30)

  

if __name__ == '__main__':
    ReduceFrames("SpiritedAway", "SpiritedAwayReduced")
  