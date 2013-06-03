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


class CenteredMultipleScales(BaseFilter):

  """
  Create scaled versions of the original image and centers them.
  """

  def __init__(self, scales=[1], background=0, simultaneous=False):
    """
    @param scales -- List of factors used for scaling. scales = [.5, 1] returns
      two images, one half the size of the original in each dimension, and one
      which is the original image.
    @param scales -- Background pixel value.
    @param simultaneous -- Whether the images should be sent out of the sensor
      simultaneously.
    """

    BaseFilter.__init__(self)

    self.scales = scales
    self.background = background
    self.simultaneous = simultaneous

  def process(self, image):
    """
    @param image -- The image to process.

    Returns a single image, or a list containing one or more images.
    """

    BaseFilter.process(self, image)

    mode = image.mode;
    originalSize = image.size;
    sizes = [(int(round(image.size[0]*s)), int(round(image.size[1]*s)))
      for s in self.scales]

    resizedImages = []
    for size in sizes:
      if size < image.size:
        resizedImage = image.resize(size,Image.ANTIALIAS)
      else:
        resizedImage = image.resize(size,Image.BICUBIC)
      x = (originalSize[0] - size[0])/2
      y = (originalSize[1] - size[1])/2
      newImage = Image.new(mode,originalSize,self.background)
      newImage.paste(resizedImage,(x,y))
      resizedImages.append(newImage)

    if not self.simultaneous:
      return resizedImages
    else:
      return [resizedImages]

  def getOutputCount(self):
    """
    Return the number of images returned by each call to process().

    If the filter creates multiple simultaneous outputs, return a tuple:
    (numOutputs, numSimultaneousOutputs).
    """

    if not self.simultaneous:
      return len(self.scales)
    else:
      return (1, len(self.scales))