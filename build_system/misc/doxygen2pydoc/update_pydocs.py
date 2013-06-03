#!/usr/bin/env python

# ----------------------------------------------------------------------
#  Copyright (C) 2006,2007 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""
## @file
"""

import os, sys
import tempfile
import shutil

Path_ = os.path.dirname(__file__)
sys.path.insert(0, Path_)
from doxy2swig import main as doxy2swig

Copyright_ = \
"""
// ----------------------------------------------------------------------
//  Copyright (C) 2006,2007 Numenta Inc. All rights reserved.
//
//  The information and source code contained herein is the
//  exclusive property of Numenta Inc. No part of this software
//  may be used, reproduced, stored or distributed in any form,
//  without explicit written authorization from Numenta Inc.
// ----------------------------------------------------------------------

"""

def ConvertAll(listing, output):
  """Reads each XML file listed by filename in 'listing', 
  and writes the converted swig-compatible pydocs to 'output'
  (which must be an output stream).
  """
  output.write(Copyright_)

  tempFile, tempName = tempfile.mkstemp()
  del tempFile # Close the temporary file.

  if not hasattr(listing, "__iter__"): listing = (listing, )
  for inputName in listing:
    print inputName, tempName
    doxy2swig(inputName, tempName)
    output.write(file(tempName).read())

  os.unlink(tempName)

def Doxygen(path, doxyfile, output):
  pushd = os.getcwd()
  os.chdir(path)
  retCode = os.system("doxygen %s > xml.doxylog" % doxyfile)
  assert retCode == 0
  moveTo = os.path.join(pushd, output)
  if not os.path.samefile(moveTo, output):
    try: shutil.rmtree(moveTo)
    except: pass
    shutil.move(output, moveTo)
  os.chdir(pushd)

# Run from the command-line.
if __name__ == "__main__":
  prepend = "xml"
  # Updating doxygen docs.
  Doxygen(sys.argv[1], os.path.join(Path_, "xml.doxyfile"), prepend)

  # Getting list of files to convert.
  listingFilename = sys.argv[2]
  listing = [x.rstrip() for x in file(listingFilename).readlines() if
    not x.startswith("#")]
  if prepend: listing = [os.path.join(prepend, x) for x in listing]

  # Opening output stream.
  if len(sys.argv) > 3: output = file(sys.argv[3], "w")
  else: output = sys.stdout

  ConvertAll(listing, output)


  

  
