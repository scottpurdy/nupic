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
                 ImageChops)

from nupic.regions.ImageSensorFilters.BaseFilter import BaseFilter


class Thicken(BaseFilter):

  """
  Thicken lines by shifting the image around and returning the brightest
  image.
  """

  def __init__(self, shiftSize=1):
    """
    @param stepSize -- number of pixels to shift
    """

    BaseFilter.__init__(self)

    self.shiftSize = shiftSize

  def process(self, image):
    """
    @param image -- The image to process.

    Returns a single image
    """

    BaseFilter.process(self, image)

    newImage = image

    # Shifting by more than one pixel can cause problems, so even if
    # stepSize > 1, get there by thickening by one shift at a time
    for x in xrange(-self.shiftSize,self.shiftSize+1):
      for y in xrange(-self.shiftSize,self.shiftSize+1):
        offsetImage = ImageChops.offset(image,x,y)
        newImage = ImageChops.lighter(newImage,offsetImage)
    return newImage