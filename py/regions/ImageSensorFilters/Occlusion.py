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

from PIL import Image

import numpy
from nupic.regions.ImageSensorFilters.BaseFilter import BaseFilter, uint


class Occlusion(BaseFilter):

  """
  Add randomly-generated rectangles to the image.
  """

  def __init__(self, numRectangles=4, seed=None, reproducible=False):
    """
    @param numRectangles -- Number of rectangles to add.
    @param seed -- Seed value for random number generator, to produce
      reproducible results.
    @param reproducible -- Whether to seed the random number generator based
      on a hash of the image pixels upon each call to process().
    'seed' and 'reproducible' cannot be used together.
    """

    BaseFilter.__init__(self, seed, reproducible)

    self.numRectangles = numRectangles

  def process(self, image):
    """
    @param image -- The image to process.

    Returns a single image, or a list containing one or more images.
    """

    BaseFilter.process(self, image)

    s = min(image.size)
    sizeRange = [int(0.1 * s), int(0.4 * s)]

    newArray = numpy.array(image.split()[0].getdata())
    newArray.resize(image.size[1],image.size[0])
    for j in xrange(self.numRectangles):
      # Generate random rectange
      size = (self.random.randint(sizeRange[0], sizeRange[1]),
        self.random.randint(sizeRange[0], sizeRange[1]))
      loc = [self.random.randint(0,image.size[1]),
             self.random.randint(0,image.size[0])]
      # Move the location so that the rectangle is centered on it
      loc[0] -= size[0]/2
      loc[1] -= size[1]/2
      # Generate random color
      color = self.random.randint(0,255)
      # Add the rectangle to the image
      newArray[max(0,loc[0]):min(newArray.shape[0], loc[0]+size[0]), \
        max(0,loc[1]):min(newArray.shape[1],loc[1]+size[1])] = color
    newImage = Image.new("L", image.size)
    newImage.putdata([uint(p) for p in newArray.flatten()])
    newImage.putalpha(image.split()[1])
    return newImage