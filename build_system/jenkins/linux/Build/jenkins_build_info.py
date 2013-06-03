#!/usr/bin/env python
# ----------------------------------------------------------------------
#  Copyright (C) 2006-2011 Numenta Inc. All rights reserved.
#
#  The information and src code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

import sys
import os
import time
import socket
import json

if __name__ == '__main__':

  arch = sys.argv[1]
  tag = sys.argv[2]
  dir = sys.argv[3]
  curtime = time.ctime()
  hostname = socket.gethostname()
  assertions = True

  # This file is a human readable file containing build information
  buildinfo = os.path.join(dir, "..", tag, 'nta', 'eng', '.buildinfo')
  os.system('touch %s' %buildinfo)
  file = open(buildinfo, 'w')
  print >> file, "==============================="
  print >> file, "Timestamp: %s" %curtime
  print >> file, "Arch: %s" %arch
  print >> file, "Buildhost: %s" %hostname
  print >> file, "Tag: %s" %tag
  print >> file, "Assertions: %s" %assertions
  print >> file, "==============================="
  file.close()

  # This file is a JSON formatted build info file (currently used for
  # naming model checkpoints in S3)
  jsonbuildnumber = os.path.join(dir, "..", tag, 'nta', 'eng', '.build.json')
  to_dump = {}
  to_dump["tag"] = tag
  file = open(jsonbuildnumber, 'w')
  json.dump(to_dump,file)
  file.close()
  
  # This file is required by the old Java web app and Java tests
  buildnumber = os.path.join(dir, "..", tag, 'nta', 'eng', '.build.number')
  file = open(buildnumber, 'w')
  print >> file, tag[0:7],
  print >> file, " ",
  print >> file, curtime[0:11]
  file.close()


  # Create build-SHA file (file with same name as release hash tag)
  # Used for Chef deployment
  buildSHAName = os.path.join(dir,"..",tag,'nta','eng','build-%s'%(tag))
  print "Writing file: ",buildSHAName
  file = open(buildSHAName, 'w')
  print >> file, tag,
  file.close()

