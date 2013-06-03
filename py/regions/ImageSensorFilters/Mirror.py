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
from PIL import ImageOps

from nupic.regions.ImageSensorFilters.BaseFilter import BaseFilter

class Mirror(BaseFilter):
  """
  Mirrors the image.
  """
  def __init__(self, seed=None, reproducible=False, both=False):
    """
    @param seed -- Seed value for random number generator, to produce
      reproducible results.
    @param reproducible -- Whether to seed the random number generator based
      on a hash of the image pixels upon each call to process().
    'seed' and 'reproducible' cannot be used together.
    both -- Whether to also pass through the original image.
    """
    BaseFilter.__init__(self, seed, reproducible)
    self.both = both

  def process(self, image):
    """
    @param image -- The image to process.

    Returns a single image, or a list containing one or more images.
    """
    BaseFilter.process(self, image)
    newImage = ImageOps.mirror(image)
    if not self.both:
      return newImage
    else:
      return [image, newImage]


  def getOutputCount(self):
    """
    Return the number of images returned by each call to process().

    If the filter creates multiple simultaneous outputs, return a tuple:
    (outputCount, simultaneousOutputCount).
    """

    return 1 + int(self.both)