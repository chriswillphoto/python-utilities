#!/usr/bin/env python3

import cv2
import sys
import os

if len(sys.argv) > 1:
  print(sys.argv)

  if sys.argv[1][-3:] == 'mp4':
    vidObj = cv2.VideoCapture(os.path.abspath(sys.argv[1]))
    count = 0
    success = 1

    while success:
      success, image = vidObj.read()
      
      if count == 100:
        cv2.imwrite("frame.jpg", image)

      count += 1