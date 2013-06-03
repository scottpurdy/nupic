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


class ScaleToFit(BaseFilter):

  """
  ** DEPRECATED ** Scale the image to fit the specified size.
  """

  def __init__(self, width, height, scaleHeightTo=None, scaleWidthTo=None, pad=False):
    """
    ** DEPRECATED **
    @param width -- Target width, in pixels.
    @param height -- Target height, in pixels.
    @param pad -- Whether to pad the image with the background color in order
      to fit the specified size exactly.
    """

    BaseFilter.__init__(self)

    self.width = width
    self.height = height
    self.pad = pad
    self.scaleHeightTo = scaleHeightTo
    self.scaleWidthTo = scaleWidthTo

  def process(self, image):
    """
    @param image -- The image to process.

    Returns a single image, or a list containing one or more images.
    """

    BaseFilter.process(self, image)

    if image.size == (self.width, self.height):
      return image

    # Resize the image
    targetRatio = self.width / float(self.height)
    imageRatio = image.size[0] / float(image.size[1])
    if self.scaleHeightTo:
      ySize = self.scaleHeightTo
      scaleFactor = self.scaleHeightTo / float(image.size[1])
      xSize = int(scaleFactor * image.size[0])
    elif self.scaleWidthTo:
      xSize = self.scaleWidthTo
      scaleFactor = self.scaleWidthTo / float(image.size[0])
      ySize = int(scaleFactor * image.size[1])
    else:
      if imageRatio > targetRatio:
        xSize = self.width
        scaleFactor = self.width / float(image.size[0])
        ySize = int(scaleFactor * image.size[1])
      else:
        ySize = self.height
        scaleFactor = self.height / float(image.size[1])
        xSize = int(scaleFactor * image.size[0])

    if (xSize, ySize) < image.size:
      image = image.resize((xSize, ySize),Image.ANTIALIAS)
    else:
      image = image.resize((xSize, ySize),Image.BICUBIC)

    # Pad the image if necessary
    if self.pad and image.size != (self.width, self.height):
      paddedImage = Image.new('L', (self.width, self.height),
        self.background)
      alpha = Image.new('L', (self.width, self.height))
      paddedImage.putalpha(alpha)
      paddedImage.paste(image,
        ((self.width - image.size[0])/2, (self.height - image.size[1])/2))
      image = paddedImage

    return image