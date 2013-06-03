# ----------------------------------------------------------------------
#  Copyright (C) 2006,2007 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

import sys
import os
import platform

def getArch() :
  """
  Return the NuPIC architecture name.
  Note that this is redundant with the calculation in configure.ac
  """
  if sys.platform == "linux2":
    #
    # platform.processor() vs. platform.machine() is a bit of a mystery
    # On linux systems, they ultimately translate to uname -p and uname -m, respectively.
    # These options and their possible results aren't clearly documented. 
    # uname -p doesn't exist in some versions of uname (debian 3.x)
    # and returns "unknown" on others (Ubuntu). Python translates "unknown" to "". 
    # uname -p may also return "athlon" or other random words. 
    # 
    cpu = platform.machine()
    if cpu not in ["i686", "i386", "x86_64"]:
      cpu = platform.processor()
    if cpu in ["i686", "i386"]:
      return "linux32"
    elif cpu == "x86_64":
      return "linux64"
    else:
      raise Exception("Unknown cpu for linux system. platform.machine() = %s; platform.processor() = %s" % (platform.machine(), platform.processor()))
  elif sys.platform == "darwin":
    cpu = platform.processor()
    if cpu == "powerpc":
      raise Exception("Unsupported CPU %s for darwin system" %(cpu));
    else:
      return "darwin64"

  elif sys.platform == "win32":
    return "win32"
  else:
    raise Exception("Unknown os %s" % sys.platform)

