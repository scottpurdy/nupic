# ----------------------------------------------------------------------
#  Copyright (C) 2006-2008 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""
This file defines CenterPictureExplorer, an explorer for
PictureSensor.
"""

from nupic.regions.PictureSensor import PictureSensor

#+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
# CenterPictureExplorer

class CenterPictureExplorer(PictureSensor.PictureExplorer):
  """
  Presents a single instance of each category at the
  center of the canvas.
  """

  def initSequence(self, state, params):
    self._presentAtCenter(state)

  def updateSequence(self, state, params):
    self._presentAtCenter(state)


  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  # Internal helper method(s)

  def _presentAtCenter(self, state):
    """
    Compute the next category to present based on the iteration
    count, and present that category at the center of the canvas.
    """
    # Override default state
    state['posnX'] = 0
    state['posnY'] = 0
    state['velocityX'] = 0
    state['velocityY'] = 0
    state['angularPosn'] = 0
    state['angularVelocity'] = 0
    state['catIndex'] = self._getIterCount() % self._getNumCategories()