# ----------------------------------------------------------------------
#  Copyright (C) 2006-2008 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------
import sys
import random

sys_maxint = sys.maxint

def uint(i):
  """Helper function to convert values to accepted range for PIL

  See: http://www.joachimschipper.nl/SystemError%20when%20using%20PIL

  I modified the function a little to be more efficient and use
  a sys_maxint global variable instead of looking up sys.maxint
  every time.
  """
  i = int(i)
  if sys_maxint < i <= 2 * sys_maxint + 1:
    return int((i & sys_maxint) - sys_maxint - 1)
  else:
    return i


class BaseFilter(object):
  # Save the lookup on the sys.maxint because it will be called a LOT

  def __init__(self, seed=None, reproducible=False):
    """
    seed -- Seed for the random number generator. A specific random number
      generator instance is always created for each filter, so that they do
      not affect each other.
    reproducible -- Seed the random number generator with a hash of the image
      pixels on each call to process(), in order to ensure that the filter
      always generates the same output for a particular input image.
    """

    if seed is not None and reproducible:
      raise RuntimeError("Cannot use 'seed' and 'reproducible' together")

    self.random = random.Random()
    if seed is not None:
      self.random.seed(seed)

    self.reproducible = reproducible

    self.mode = 'gray'
    self.background = 0

  def process(self, image):
    """
    @param image -- The image to process.

    Returns a single image, or a list containing one or more images.
    Post filtersIt can also return an additional raw output numpy array
    that will be used as the output of the ImageSensor
    """

    if self.reproducible:
      # Seed the random instance with a hash of the image pixels
      self.random.seed(hash(image.tostring()))

  def getOutputCount(self):
    """
    Return the number of images returned by each call to process().

    If the filter creates multiple simultaneous outputs, return a tuple:
    (outputCount, simultaneousOutputCount).
    """

    return 1

  def update(self, mode=None, background=None):
    """
    Accept new parameters from ImageSensor and update state.
    """

    if mode is not None:
      self.mode = mode

    if background is not None:
      self.background = background