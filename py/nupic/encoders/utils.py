# ----------------------------------------------------------------------
#  Copyright (C) 2010 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------




############################################################################
def bitsToString(array):
  """Returns a string representing a numpy array of 0's and 1's"""
  s = ""
  for i in xrange(len(array)):
    if array[i] == 0:
      s += "."
    else:
      s += "*"
  return s