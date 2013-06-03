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
  

  buildinfo = os.path.join(dir, "..", tag, 'nta', 'eng', '.buildinfo')
  buildnumber = os.path.join(dir, "..", tag, 'nta', 'eng', '.build.number')
  jsonbuildnumber = os.path.join(dir, "..", tag, 'nta', 'eng', '.build.json')
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

  file = open(buildnumber, 'w')
  print >> file, tag[0:7],
  print >> file, " ",
  print >> file, curtime[0:11]
  file.close()

  to_dump = {}
  to_dump["tag"] = tag
  file = open(jsonbuildnumber, 'w')
  json.dump(to_dump,file)
  file.close()

