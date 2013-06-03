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
                 ImageChops,
                 ImageEnhance,
                 ImageMath,)

from nupic.regions.ImageSensorFilters.BaseFilter import BaseFilter


class Contrast(BaseFilter):

  """
  Modify the contrast of the image.
  """

  def __init__(self, factor=1.0, scaleTowardCenter=False):
    """
    Parameters
    ----------
    factor: float
      How much contrast to produce in the output image relative
      to the input image. A factor of 0 returns a solid gray image,
      a factor of 1.0 returns the original image, and higher values
      return higher-contrast images.

    scaleTowardCenter: bool
      If False (the default), uses PIL.ImageEnhance.Contrast.
      If True, scales the pixel values toward 0.5.
    """

    BaseFilter.__init__(self)

    if factor < 0:
      raise ValueError("'factor' must be nonnegative")

    self.factor = factor
    self.scaleTowardCenter = scaleTowardCenter
    if scaleTowardCenter and not (0.0 <= factor <= 1.0):
      raise ValueError("scaleTowardCenter only supports contrast factors "
          "between 0 and 1, inclusive.")

  def process(self, image):
    """
    @param image -- The image to process.

    Returns a single image, or a list containing one or more images.
    """
    BaseFilter.process(self, image)

    base, alpha = image.split()

    if self.scaleTowardCenter:
      scale = float(self.factor)
      assert base.mode == "L"
      maxValue = 255 # TODO: Determine how to get maximum value __allowed__.
      offset = ((1.0 - self.factor) / 2.0) * maxValue
      newImage = ImageMath.eval(
          "convert(convert(gray, 'F') * scale + offset, mode)",
          gray=base,
          scale=scale,
          offset=offset,
          mode=base.mode,
        )
    else:
      contrastEnhancer = ImageEnhance.Contrast(image.split()[0])
      newImage = contrastEnhancer.enhance(self.factor)

    newImage.putalpha(alpha)

    return newImage