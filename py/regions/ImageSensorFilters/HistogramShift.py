# ----------------------------------------------------------------------
#  Copyright (C) 2006-2008 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""
## @file
"""

import random

import numpy
from PIL import Image

from nupic.regions.ImageSensorFilters.BaseFilter import BaseFilter, uint

class HistogramShift(BaseFilter):
  """
  Shifts the image histogram randomly in any direction, given a difficulty level.
  """
  def __init__(self, difficulty = 0.5, seed=None, reproducible=False):
    """
    @param difficulty -- Value between 0.0 and 1.0 that dictates how far
      to shift the image histogram. The direction will be random, and a random offset will be added.
    @param seed -- Seed value for random number generator, to produce
      reproducible results.
    @param reproducible -- Whether to seed the random number generator based
      on a hash of the image pixels upon each call to process().
    'seed' and 'reproducible' cannot be used together.
    """
    BaseFilter.__init__(self, seed, reproducible)

    if difficulty < 0.0 or difficulty > 1.0:
        raise RuntimeError("difficulty must be between 0.0 and 1.0")
    self.difficulty = difficulty
    #Maximum histogram shift - half the grayscale band (0-255)
    self.maxOffset = 128

  def process(self, image):
    """
    @param image -- The image to process.

    Returns a single image, or a list containing one or more images.
    """
    BaseFilter.process(self, image)
    #Create numpy array from image grayscale data and resize to image dimensions
    imageArray = numpy.array(image.split()[0].getdata())
    imageArray.resize(image.size[1], image.size[0])
    #Calculate offset from difficulty level
    offset = self.difficulty*(self.maxOffset)
    #Add random change to offset within window size
    halfWindowSize = 0.1*offset
    offset = (offset - halfWindowSize) + halfWindowSize*self.random.random()*((-1)**self.random.randint(1, 2))
    #Apply random direction
    offset *= ((-1)**self.random.randint(1, 2))
    imageArray += offset
    #Recreate PIL image
    newImage = Image.new("L", image.size)
    newImage.putdata([uint(p) for p in imageArray.flatten()])
    newImage.putalpha(image.split()[1])
    return newImage