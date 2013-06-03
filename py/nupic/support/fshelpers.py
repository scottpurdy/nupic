# ----------------------------------------------------------------------
#  Copyright (C) 2011 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------


# This script contains file-system helper functions


import os



###############################################################################
def makeDirectoryFromAbsolutePath(absDirPath):
  """ Makes directory for the given directory path with default permissions.
  If the directory already exists, it is treated as success.

  absDirPath:   absolute path of the directory to create.

  Returns:      absDirPath arg

  Exceptions:         OSError if directory creation fails
  """

  assert os.path.isabs(absDirPath)

  try:
    os.makedirs(absDirPath)
  except OSError, e:
    if e.errno != os.errno.EEXIST:
      raise

  return absDirPath