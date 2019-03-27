#!/usr/bin/env python3

import os
import subprocess
import sys

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

if len(sys.argv) > 1:
  # print(os.path.isdir(sys.argv[1]))
  # print(os.getcwd())
  os.chdir(sys.argv[1])
  print("Working Directory: " + os.getcwd())
  if os.path.isdir(os.getcwd()):
    for x in os.listdir(os.getcwd()):
      if os.path.isdir(x):
        # dirpath = os.path.join(sys.argv[1], x)
        zipup = subprocess.Popen(['tar', '-cvzf', x + '.tar.gz', x ], stdout=subprocess.PIPE)
        zipup.communicate()
        print(bcolors.OKGREEN + x + ' has been zipped' + bcolors.ENDC)
        del_request = input(bcolors.WARNING + 'Bin original directory? [y/n]: ' + bcolors.ENDC)

        if del_request.lower() == 'y':
          deldir = subprocess.Popen(['mv', x, os.path.expanduser('~/.Trash')])
          deldir.communicate()
          print(bcolors.OKBLUE + x+' has been moved to Bin' + bcolors.ENDC)
        
        

