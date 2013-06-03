# ----------------------------------------------------------------------
#  Copyright (C) 2006-2008 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

import os

from nupic.regions.ImageSensorExplorers.BaseExplorer import BaseExplorer


class ImageSweep(BaseExplorer):

  """
  This explorer is like Flash, but it sends a reset signal whenever the
  directory changes.
  """

  def next(self, seeking=False):
    """
    Go to the next position (next iteration).

    seeking -- Boolean that indicates whether the explorer is calling next()
      from seek(). If True, the explorer should avoid unnecessary computation
      that would not affect the seek command. The last call to next() from
      seek() will be with seeking=False.
    """

    self.position['reset'] = False
    prevImage = self.position['image']

    # Iterate through the filters
    for i in xrange(self.numFilters):
      self.position['filters'][i] += 1
      if self.position['filters'][i] < self.numFilterOutputs[i]:
        if not seeking:
          # Center the image
          self.centerImage()
        return
      self.position['filters'][i] = 0
    # Go to the next image
    self.position['image'] += 1
    if self.position['image'] == self.numImages:
      self.position['image'] = 0
    if not seeking:
      # Center the image
      self.centerImage()

    image = self.position['image']
    if not self.getImageInfo(prevImage)['imagePath'] or \
        (os.path.split(self.getImageInfo(image)['imagePath'])[0] !=
        os.path.split(self.getImageInfo(prevImage)['imagePath'])[0]):
      self.position['reset'] = True

  def getNumIterations(self, image):
    """
    Get the number of iterations required to completely explore the input space.

    Explorers that do not wish to support this method should not override it.

    image -- If None, returns the sum of the iterations for all the loaded
      images. Otherwise, image should be an integer specifying the image for
      which to calculate iterations.

    ImageSensor takes care of the input validation.
    """

    if image is not None:
      return self.numFilteredVersionsPerImage
    else:
      return self.numFilteredVersionsPerImage * self.numImages