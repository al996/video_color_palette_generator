import cv2
import os
import shutil

def FrameCapture(vidPath, outDir):
      
    # Path to video file
    vidObj = cv2.VideoCapture(vidPath)

    # Output directory
    os.mkdir(outDir)

    frame = 0
    second = 0
    success = 1
  
    while success:
        success, image = vidObj.read()
      
        # Saves the frames each second (24 frame per second)
        if success and frame % 24 == 0:
            path = os.path.join(outDir, "%d.jpg" % second)
            cv2.imwrite(path, image)
            second += 1
        
        frame += 1
  

if __name__ == '__main__':
    # FrameCapture("file.mp4", "directory")