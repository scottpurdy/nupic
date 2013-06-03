# ----------------------------------------------------------------------
#  Copyright (C) 2010 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------
from nupic.encoders import DeltaEncoder,AdaptiveScalarEncoder
from base import *
#from nupic.encoders import DeltaEncoder


class ScalarSpaceEncoder(Encoder):
  """An encoder that can be used to permute the encodings through different spaces
  These include absolute value,delta, log space, etc.
  """
  SPACE_ABSOLUTE="absolute"
  SPACE_DELTA="delta"
  def __init__(self):
    pass
  def __new__(self, w, minval=None, maxval=None, periodic=False, n=0, radius=0,
                resolution=0, name=None, verbosity=0, clipInput=False, space="absolute"):
    self._encoder = None
    if space == "absolute":
      ret = AdaptiveScalarEncoder(w,minval,maxval,periodic,n,radius,
                                            resolution,name,verbosity,clipInput)
    else:
      ret = DeltaEncoder(w,minval,maxval,periodic,n,radius,resolution,name,verbosity,clipInput)
    return ret


def testScalarSpaceEncoder():
  # Run all tests
  sse = ScalarSpaceEncoder(1,1,2,False,2,1,1,None,0,False,"delta")
  assert sse.isDelta()
  sse = ScalarSpaceEncoder(1,1,2,False,2,1,1,None,0,False,"absolute")
  assert not sse.isDelta()
  print "scalarSpaceEncoder test passed"

###############################################################################
if __name__ == '__main__':
  testScalarSpaceEncoder()