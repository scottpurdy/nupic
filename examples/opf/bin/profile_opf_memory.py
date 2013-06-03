#!/usr/bin/env python
# ----------------------------------------------------------------------
# Copyright (C) 2012 Numenta Inc. All rights reserved.
#
# The information and source code contained herein is the
# exclusive property of Numenta Inc.  No part of this software
# may be used, reproduced, stored or distributed in any form,
# without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""Memory profiling tool."""

import os
import subprocess
import sys
import time



def main(expLocation):
  start = time.time()
  opfRunnerPath = os.path.join(os.getcwd(), os.path.dirname(__file__),
                               'OpfRunExperiment.py')
  expPath = os.path.join(os.getcwd(), expLocation)
  expProc = subprocess.Popen(['python', opfRunnerPath, expPath])
  history = []
  while True:
    if expProc.poll() is not None:
      break
    process = subprocess.Popen(
        "ps -o rss,command | grep OpfRunExperiment | "
        "awk '{sum+=$1} END {print sum}'",
        shell=True, stdout=subprocess.PIPE)
    try:
      stdoutList = process.communicate()[0].split('\n')
      mem = float(stdoutList[0]) * 1024 / 1048576
    except ValueError:
      continue
    history.append((time.time() - start, mem))

  print 'Max memory: ', max([a[1] for a in history])



if __name__ == '__main__':
  if len(sys.argv) != 2:
    print ('Usage: profile_opf_memory.py path/to/experiment/\n'
           '    See OpfRunExperiment.py')
    sys.exit(1)
  main(sys.argv[1])
