# ----------------------------------------------------------------------
#  Copyright (C) 2006-2008 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

from nupic.regions.ImageSensorExplorers.BaseExplorer import BaseExplorer


class EyeMovements(BaseExplorer):

  """
  This explorer flashes each image nine times, shifted by one pixel each time,
  simulating "eye movements".
  """

  def __init__(self, shift=1, aggregate='sum', *args, **kwargs):
    """
    @param shift -- Number of pixels to move from the center ("radius" of the
      eye movement square).

    @param aggregate -- A function that's used by inference analysis to
      aggregate the results of different eye movement presentations. Valid
      values are 'sum', 'average', 'product' and 'max'. The default is 'sum'.
    """

    BaseExplorer.__init__(self, *args, **kwargs)
    assert aggregate in ('sum', 'average', 'max', 'product')
    self.aggregate_func = aggregate
    self.shift = shift

  def first(self):
    """
    Set up the position.

    BaseExplorer picks image 0, offset (0,0), etc., but explorers that wish
    to set a different first position should extend this method. Such explorers
    may wish to call BaseExplorer.first(center=False), which initializes the
    position tuple but does not call centerImage() (which could cause
    unnecessary filtering to occur).
    """

    BaseExplorer.first(self)
    self.eyeMovementIndex = 0

  def next(self, seeking=False):
    """
    Go to the next position (next iteration).

    seeking -- Boolean that indicates whether the explorer is calling next()
      from seek(). If True, the explorer should avoid unnecessary computation
      that would not affect the seek command. The last call to next() from
      seek() will be with seeking=False.
    """

    # Iterate through eye movement positions
    self.eyeMovementIndex += 1
    if self.eyeMovementIndex < 9:
      self.centerImage()
      if self.eyeMovementIndex in (1, 2, 3):
        self.position['offset'][1] -= self.shift
      elif self.eyeMovementIndex in (5, 6, 7):
        self.position['offset'][1] += self.shift
      if self.eyeMovementIndex in (1, 7, 8):
        self.position['offset'][0] -= self.shift
      elif self.eyeMovementIndex in (3, 4, 5):
        self.position['offset'][0] += self.shift
      self.position['reset'] = False
    else:
      self.eyeMovementIndex = 0
      # Iterate through the filters
      for i in xrange(self.numFilters):
        self.position['filters'][i] += 1
        if self.position['filters'][i] < self.numFilterOutputs[i]:
          self.centerImage()
          return
        self.position['filters'][i] = 0
      # Go to the next image
      self.position['image'] += 1
      if self.position['image'] == self.numImages:
        self.position['image'] = 0
      self.position['reset'] = True
      self.centerImage()

  def getNumIterations(self, image):
    """
    Get the number of iterations required to completely explore the input space.

    image -- If None, returns the sum of the iterations for all the
      loaded images. Otherwise, image should be an integer specifying the
      image for which to calculate iterations.

    ImageSensor takes care of the input validation.
    """

    if image is not None:
      return self.numFilteredVersionsPerImage * 9
    else:
      return self.numFilteredVersionsPerImage * 9 * self.numImages