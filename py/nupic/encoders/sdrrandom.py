# ----------------------------------------------------------------------
#  Copyright (C) 2011 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

from base import *
import random
from nupic.data.fieldmeta import FieldMetaType

############################################################################
class SDRRandomEncoder(Encoder):
  """Generate a random encoding

  Each  encoding is an SDR in which w out of n bits are turned on.

  """

  ############################################################################
  def __init__(self, n, w, name="random", verbosity=0):
    """
    n is  total bits in output
    w is the number of bits that are turned on for each rep
    """

    self.n = n
    self.w = w
    self.verbosity = verbosity
    self.description = [(name, 0)]
    self.name = name

  ############################################################################
  def getDecoderOutputFieldTypes(self):
    """ [Encoder class virtual method override]
    """
    return (FieldMetaType.string,)

  ############################################################################
  def getWidth(self):
    return self.n

  ############################################################################
  def getDescription(self):
    return self.description

  ############################################################################
  def getScalars(self, input):
    """ See method description in base.py """
    return numpy.array([0])

  ############################################################################
  def getBucketIndices(self, input):
    """ See method description in base.py """
    return [0]

  ############################################################################
  def encodeIntoArray(self, input, output):
    """ See method description in base.py """
    output[0:self.n] = 0
    output[0:self.n][random.sample(xrange(self.n), self.w)] = 1

    if self.verbosity >= 2:
      print "input:", input, "index:", index, "output:", output
      print "decoded:", self.decodedToStr(self.decode(output))


  ############################################################################
  def decode(self, encoded, parentFieldName=''):
    """ See the function description in base.py
    """

    if parentFieldName != '':
      fieldName = "%s.%s" % (parentFieldName, self.name)
    else:
      fieldName = self.name
    return ({fieldName: ([[0, 0]], 'rand')}, [fieldName])


  ############################################################################
  def getBucketInfo(self, buckets):
    """ See the function description in base.py
    """

    return [EncoderResult(value=0, scalar=0,
                         encoding=numpy.zeros(self.n))]

  ############################################################################
  def topDownCompute(self, encoded):
    """ See the function description in base.py
    """

    return EncoderResult(value=0, scalar=0,
                         encoding=numpy.zeros(self.n))

  ############################################################################
  def closenessScores(self, expValues, actValues, **kwargs):
    """ See the function description in base.py

    kwargs will have the keyword "fractional", which is ignored by this encoder
    """

    return numpy.array([0])

############################################################################
def testSDRRandomEncoder():
  print "Testing RandomEncoder...",

  fieldWidth = 25
  bitsOn = 10

  s = SDRRandomEncoder(n=fieldWidth, w=bitsOn, name="foo")

  for i in range(100):
    out = s.encode(0)
    assert out.shape == (fieldWidth,)
    assert out.sum() == bitsOn
    #print out

  x = s.decode(out)
  print x
  assert isinstance(x[0], dict)
  assert "foo" in x[0]

  print "passed"


################################################################################
if __name__=='__main__':

  # Run all tests
  testSDRRandomEncoder()