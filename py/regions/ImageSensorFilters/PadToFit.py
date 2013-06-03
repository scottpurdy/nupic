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


class PadToFit(BaseFilter):

  """
  ** DEPRECATED ** Pad the image so that it fits the specified size.
  """

  def __init__(self, width, height):
    """
    ** DEPRECATED **
    @param width -- Target width, in pixels.
    @param height -- Target height, in pixels.
    """

    BaseFilter.__init__(self)

    self.width = width
    self.height = height

  def process(self, image):
    """
    @param image -- The image to process.

    Returns a single image, or a list containing one or more images.
    """

    BaseFilter.process(self, image)

    if image.size == (self.width, self.height):
      return image

    if image.size[0] > self.width or image.size[1] > self.height:
      raise RuntimeError('Image is larger than target size')

    newImage = Image.new(image.mode, (self.width, self.height),
      self.background)
    xPad = self.width - image.size[0]
    yPad = self.height - image.size[1]
    newImage.paste(image, (xPad/2, yPad/2))
    return newImage