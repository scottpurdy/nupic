# ----------------------------------------------------------------------
#  Copyright (C) 2006-2008 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""
This file defines HorizontalPictureExplorer, an explorer for
PictureSensor.
"""

# Third-party imports
import numpy

# Local imports
from nupic.regions.PictureSensorExplorers.random import RandomPictureExplorer

#+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
# HorizontalPictureExplorer

class HorizontalPictureExplorer(RandomPictureExplorer):
  """
  Specialization of 'random' explorer that allows horizontal
  sweeps only.
  """

  def initSequence(self, state, params):
    # Invoke base class
    super(HorizontalPictureExplorer, self).initSequence(state, params)
    # Force vertical velocity to be zero
    state['velocityY'] = 0
    # Make sure we don't allow stationary (no velocity)
    if state['velocityX'] == 0:
      state['velocityX'] = self._rng.choice(numpy.array([-1, 1], dtype=int) \
                         * max(1, params['minVelocity']))