import cv2
import os
import shutil

def FrameCapture(vidPath, outDir):
      
    # Path to video file
    vidObj = cv2.VideoCapture(vidPath)

    # Output directory
    os.mkdir(outDir)

    frame = 0
    idx = 0
    success = 1
  
    while success:
        success, image = vidObj.read()
      
        # Saves the frames each 5 seconds (24 frame per second)
        if success and frame % 120 == 0:
            path = os.path.join(outDir, "%d.jpg" % idx)
            cv2.imwrite(path, image)
            idx += 1
        
        frame += 1
  

if __name__ == '__main__':
    FrameCapture("SpiritedAway.mp4", "SpiritedAway")