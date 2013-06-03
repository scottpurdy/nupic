#! /usr/bin/env python
# ----------------------------------------------------------------------
#  Copyright (C) 2011 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

import fcntl
import os


class FileLockAcquireException(Exception):
    pass

class FileLockReleaseException(Exception):
    pass


class FileLock(object):
  """ This class implements a global file lock that can be used as a
  a mutex between cooperating processes.

  NOTE: the present implementation's behavior is undefined when multiple
        threads may try ackquire a lock on the same file.
  """

  def __init__(self, filePath):
    """
    Parameters:
    ------------------------------------------------------------------------
    filePath:   Path to a file to be used for locking; The file MUST already exist.
    """

    assert os.path.isabs(filePath), "not absolute path: %r" % filePath

    assert os.path.isfile(filePath), (
            "not a file or doesn't exist: %r" % filePath)

    self.__filePath = filePath

    self.__fp = open(self.__filePath, "r")

    self.__fd = self.__fp.fileno()

    return

  def __enter__(self):
    """ Context Manager protocol method. Allows a FileLock instance to be
    used in a "with" statement for automatic acquire/release

    Parameters:
    ------------------------------------------------------------------------
    retval:     self.
    """
    self.acquire()
    return self


  def __exit__(self, exc_type, exc_val, exc_tb):
    """ Context Manager protocol method. Allows a FileLock instance to be
    used in a "with" statement for automatic acquire/release
    """
    self.release()
    return False


  def acquire(self):
    """ Acquire global lock

    exception: FileLockAcquireException on failure
    """
    try:
      fcntl.flock(self.__fd, fcntl.LOCK_EX)
    except Exception, e:
      e = FileLockAcquireException(
        "FileLock acquire failed on %r" % (self.__filePath), e)
      raise e, None, sys.exc_info()[2]

    return


  def release(self):
    """ Release global lock
    """
    try:
      fcntl.flock(self.__fd, fcntl.LOCK_UN)
    except Exception, e:
      e = FileLockReleaseException(
        "FileLock release failed on %r" % (self.__filePath), e)
      raise e, None, sys.exc_info()[2]

    return