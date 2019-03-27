#!/usr/bin/env python3

import os
import subprocess
import sys
import zipfile
import cv2
from shutil import copyfile

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

if sys.version_info[0] < 3:
  raise Exception("Must be using Python 3")

if sys.argv[1]:
  if os.path.isdir(sys.argv[1]):

    extrafile = False

    dontzip = ['zip', '.']
    filepath = ''
    if len(sys.argv) > 2:
      if os.path.isfile(sys.argv[2]):
        dontzip.append(os.path.basename(sys.argv[2]))
        filepath = os.path.abspath(sys.argv[2])
        extrafile = True
      print(dontzip, filepath)

    os.chdir(sys.argv[1])

    for x in os.walk(os.getcwd()):
      if len(x[2]) > 0:
        os.chdir(x[0])
        print(os.getcwd())
        if extrafile:
          copyfile(filepath, os.getcwd()+ "/" + dontzip[2])
          

        for f in x[2]:
          if f[-3:] not in dontzip and f[0] not in dontzip and f not in dontzip:
            with zipfile.ZipFile( f + '.zip', 'w', zipfile.ZIP_DEFLATED) as myzip:
                if extrafile:
                  myzip.write(dontzip[2])   
                myzip.write(f)
            myzip.close()

            print(bcolors.OKBLUE + "zipped: " + bcolors.ENDC + f)

          if f[-3:] == 'mp4':
            vidObj = cv2.VideoCapture(f)
            count = 0
            success = 1
            framegrab = 60

            while success:
              success, image = vidObj.read()
              
              if not success and count < 60:
                print('Video is shorter than 60 frames -- Lower framegrab variable')

              if count == framegrab:
                cv2.imwrite(f+".jpg", image)
                print(bcolors.OKBLUE + "screenshot captured: " + bcolors.ENDC + f)
                success = False

              count += 1
        print("------")