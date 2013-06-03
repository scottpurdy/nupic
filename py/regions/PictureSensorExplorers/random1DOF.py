# ----------------------------------------------------------------------
#  Copyright (C) 2006-2008 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""
This file defines RandomPictureExplorer, an explorer for
PictureSensor.
"""

# Third-party imports
import numpy

# Local imports
from nupic.regions.PictureSensor import PictureSensor

#+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
# RandomPictureExplorer

class RandomPictureExplorer(PictureSensor.PictureExplorer):
  """
  Presents smoothly varying sequences of randomly selected
  categories that sweep across the canvas at particular
  velocities.
  """

  @classmethod
  def queryRelevantParams(klass):
    """
    Returns a sequence of parameter names that are relevant to
    the operation of the explorer.

    May be extended or overridden by sub-classes as appropriate.
    """
    return ( 'width', 'height',
             'sweepOffMode', 'maxOffset',
             'minVelocity', 'maxVelocity',
             'minAngularPosn', 'maxAngularPosn',
             'minAngularVelocity', 'maxAngularVelocity',
           )

  def initSequence(self, state, params):
    """
    Create the state associated with a new sequence.

    @param state: a dict containing the default values for new
           sequence state.  This dict will contain the following keys
           (additional keys may be added by the method implementation):
             catIndex - the 0-based index of the category
                        that will be used for the sequence;
             posnX - the initial X position of the pattern's reference
                        point for the new sequence;
             posnY - the initial Y position of the pattern's reference
                        point for the new sequence;
             velocityX - the initial horizontal velocity of the
                        pattern's reference point for the new sequence;
             velocityY - the initial vertical velocity of the
                        pattern's reference point for the new sequence;
             angularPosn - the initial angular position (in degrees) of
                        the pattern for the new sequence;
             angularVelocity - the initial angular velocity (in degrees
                        per iteration) of the pattern for the new sequence;

    Must be overridden by sub-classes, and must not invoke this base class method.
    """
    iteration = self._getIterCount()

    patternSize = state['patternSize']
    slopX = (params['width']  - patternSize) // 2
    slopY = 0
    if params['sweepOffMode']:
      slopX = abs(slopX)
      slopY = abs(slopY)
    if params['maxOffset'] != -1:
      slopX = min(abs(slopX), params['maxOffset'])
      slopY = min(abs(slopY), params['maxOffset'])
    posnX = self._rng.choice(xrange(-slopX, slopX + 1))
    posnY = self._rng.choice(xrange(-slopY, slopY + 1))
    # Choose a category random
    catIndex = self._chooseCategory()
    velocityX = self._rng.choice([-1, +1]) \
              * self._rng.choice(xrange(params['minVelocity'], params['maxVelocity'] + 1))
    velocityY = self._rng.choice([-1, +1]) \
              * self._rng.choice(xrange(params['minVelocity'], params['maxVelocity'] + 1))
    # Choose rotational params
    angularPosn = params['minAngularPosn'] + self._rng.random() \
                * (params['maxAngularPosn'] - params['minAngularPosn'])
    angularVelocity = params['minAngularVelocity'] + self._rng.random() \
                * (params['maxAngularVelocity'] - params['minAngularVelocity'])

    # Make sure we don't allow stationary (no velocity)
    if params['maxVelocity'] > 0:
      if velocityX == 0 and velocityY == 0:
        velocityX, velocityY = self._rng.choice(numpy.array(
                               [(-1, -1), (-1, 1), (1, -1), (1, 1)], dtype=int) \
                               * max(1, params['minVelocity']))

    # Override default state
    state['posnX'] = posnX
    state['posnY'] = posnY
    state['catIndex'] = catIndex
    state['velocityX'] = velocityX
    state['velocityY'] = velocityY
    state['angularPosn'] = angularPosn
    state['angularVelocity'] = angularVelocity


  def updateSequence(self, state, params):
    """
    Update the state associated with an existing sequence.

    @param state: dict containing the
    @returns: None

    Must be overridden by sub-classes, and must not invoke this base class method.
    """
    state['posnX'] += state['velocityX']
    state['posnY'] += state['velocityY']
    # Apply angular rotation (expressed in degrees)
    angularPosn = state['angularPosn'] + state['angularVelocity']
    rotations = angularPosn / 360.0
    netRotations = rotations - round(rotations)
    angularPosn = netRotations * 360.0
    state['angularPosn'] = angularPosn