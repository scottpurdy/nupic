# ----------------------------------------------------------------------
#  Copyright (C) 2010 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""
This file defines the 'starBlock' explorer.

"""

import numpy

#############################################################################
# AddNoise RecordSensor filter

class AddNoise:
  """
  This RecordSensor filter adds noise to the input

  """

  #############################################################################
  def __init__(self, noise=0.0, seed=-1):
    """ Construct the filter

    Parameters:
    -------------------------------------------------
    noise: Amount of noise to add, from 0 to 1.0

    """
    self.noise = noise
    if seed != -1:
      numpy.random.seed(seed)


  ########################################################################
  def process(self, encoder, data):
    """ Modify the data in place, adding noise
    """

    if self.noise == 0:
      return

    inputSize = data.size
    flipBits = numpy.random.randint(0, inputSize, self.noise*inputSize)
    data[flipBits] = numpy.logical_not(data[flipBits])