#! /usr/bin/env python
# ----------------------------------------------------------------------
#  Copyright (C) 2008-2009 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------


import os
import sys

# assumes build_system/pybuild is in sys.path
# assumes that logging has already been initialized with utils.initlog()
import manifest

def createRelease(releaseName, trunkDir, installDir, tmpDir="/tmp"):
  """Create the release for to this standalone app. 
  Copies files from installDir into a temporary dir, and returns
  the name of the temporary dir."""


  # Get a temp directory to hold the release. 
  baseName = os.path.join(tmpDir, "%s-release" % releaseName)
  for i in xrange(0, 10):
    releaseDir = baseName + str(i)
    if not os.path.exists(releaseDir):
      break
  if os.path.exists(releaseDir):
    raise Exception("unable to find release directory in tmpDir %s" % tmpDir)

  print "Creating release in %s" % releaseDir


  # install from the manifest
  manifestFile = os.path.join(trunkDir, "release", "%s_release" % releaseName, "manifests", "%s_release.manifest" % releaseName)
  manifest.installFromManifest(manifestFile, installDir, releaseDir, level=0, overwrite=False, destdirExists=False, allArchitectures=False)
  print "Finished creating release %s" % releaseName
  return releaseDir

