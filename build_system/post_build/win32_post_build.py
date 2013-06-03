#! /usr/bin/env python
# ----------------------------------------------------------------------
#  Copyright (C) 2009 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

import sys
import os
import subprocess

scriptDir = os.path.dirname(__file__)
pyBuildDir = os.path.join(scriptDir, '../pybuild')

def main(trunkDir, builfDir, installDir):
  print "Creating .buildinfo file"
  command = ["python", 
             os.path.join(trunkDir, "build_system/win32/createBuildInfoFile.py"), 
             installDir]

  run(command)

  
  print "Copying files from source directory"
  sys.path = [pyBuildDir] + sys.path
  import install
  
  install.main(os.path.join(trunkDir, "build_system/post_build/files_to_copy.txt"),
               trunkDir,
               installDir,
               debug=False,
               overwrite=True,
               link=False,
               optimizeCopy=False,
               developerOnly=False)
  #command = ["python", 
  #           os.path.join(trunkDir, "build_system/pybuild/install.py"), 
  #           "--overwrite", 
  #           os.path.join(trunkDir, "build_system/post_build/files_to_copy.txt"), 
  #           trunkDir, 
  #           installDir]
  #run(command)

def run(command):
  commandLine = subprocess.list2cmdline(command)
  print "Running: '%s'" % commandLine

  p = subprocess.Popen(commandLine, bufsize=1, 
                       env=os.environ,
                       shell=True,
                       stdin=None, 
                       stdout=sys.stdout,
                       stderr=sys.stderr)

  s = p.wait()

  if s != 0:
    raise Exception("Command failed")

if __name__ == "__main__":
  if len(sys.argv) != 4:
    print "usage: %s trunk-dir build-dir install-dir" % sys.argv[0]
    print sys.argv
    sys.exit(1)  
  
  trunkDir = sys.argv[1]
  buildDir = sys.argv[2]
  installDir = sys.argv[3]
  
  #trunkDir = 'z:/trunk'
  #buildDir = 'c:/nta/build'
  #installDir = 'c:/nta/install'
  
  main(trunkDir, buildDir, installDir)

#python "z:\trunk\build_system\post_build\win32_post_build.py"  "z:\trunk" "c:/nta/build" "c:/nta/install" 