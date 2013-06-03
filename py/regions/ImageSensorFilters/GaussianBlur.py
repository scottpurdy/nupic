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

from PIL import (Image,
                 ImageEnhance)

from nupic.regions.ImageSensorFilters.BaseFilter import BaseFilter


class GaussianBlur(BaseFilter):

  """
  Apply a Gaussian blur to the image.
  """

  def __init__(self, level=1):
    """
    @param level -- Number of times to blur.
    """

    BaseFilter.__init__(self)

    self.level = level

  def process(self, image):
    """
    @param image -- The image to process.

    Returns a single image, or a list containing one or more images.
    """

    BaseFilter.process(self, image)

    mask = image.split()[1]
    for i in xrange(self.level):
      sharpness_enhancer = ImageEnhance.Sharpness(image.split()[0])
      image = sharpness_enhancer.enhance(0.0)
    image.putalpha(mask)
    return image