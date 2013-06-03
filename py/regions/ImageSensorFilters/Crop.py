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

from PIL import Image

from nupic.regions.ImageSensorFilters.BaseFilter import BaseFilter


class Crop(BaseFilter):

  """
  Crop the image.
  """

  def __init__(self, box):
    """
    @param box -- 4-tuple specifying the left, top, right, and bottom coords.
    """

    BaseFilter.__init__(self)

    if box[2] <= box[0] or box[3] <= box[1]:
      raise RuntimeError('Specified box has zero width or height')

    self.box = box

  def process(self, image):
    """
    @param image -- The image to process.

    Returns a single image, or a list containing one or more images.
    """

    BaseFilter.process(self, image)

    if self.box[2] > image.size[0] or self.box[3] > image.size[1]:
      raise RuntimeError('Crop coordinates exceed image bounds')

    return image.crop(self.box)