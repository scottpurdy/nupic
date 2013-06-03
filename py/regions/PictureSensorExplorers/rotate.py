# ----------------------------------------------------------------------
#  Copyright (C) 2006-2008 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""
This file defines RotatePictureExplorer, an explorer for
PictureSensor.
"""

from nupic.regions.PictureSensor import PictureSensor

#+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
# RotatePictureExplorer

class RotatePictureExplorer(PictureSensor.PictureExplorer):

  @classmethod
  def queryRelevantParams(klass):
    """
    Returns a sequence of parameter names that are relevant to
    the operation of the explorer.

    May be extended or overridden by sub-classes as appropriate.
    """
    return ( 'numRepetitions',
             'minAngularPosn', 'maxAngularPosn',
             'minAngularVelocity', 'maxAngularVelocity',
           )

  def notifyParamUpdate(self, params):
    """
    A callback that will be invoked if/when any of the explorer's
    relevant parameters have their values changed.

    @param params: a dict containing the new values of all parameters
                   that are relevant to the explorer's operation
                   (as specified by a call to queryRelevantParams()).
    """
    # Parameter checks
    if params['minAngularVelocity'] != params['maxAngularVelocity']:
      raise NotImplementedError("'rotate' explorer currently supports " \
            "only a fixed angular velocity; i.e., 'minAngularVelocity' (%d) " \
            "must be identical to 'maxAngularVelocity' (%d)" \
            % (params['minAngularVelocity'], params['maxAngularVelocity']))
    super(RotatePictureExplorer, self).notifyParamUpdate(params)

  def initSequence(self, state, params):
    self._presentNextRotation(state, params)

  def updateSequence(self, state, params):
    self._presentNextRotation(state, params)


  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  # Internal helper method(s)

  def _presentNextRotation(self, state, params):
    """
    Compute the appropriate category and rotational angle
    deterministically based on the current iteration count.
    """

    # These don't change
    state['posnX'] = 0
    state['posnY'] = 0
    state['velocityX'] = 0
    state['velocityY'] = 0
    state['angularVelocity'] = params['minAngularVelocity']

    # These do change
    sequenceLength = 1 + int((params['maxAngularPosn'] - params['minAngularPosn'])
                             / params['minAngularVelocity'])
    state['catIndex'] = self._getIterCount() / (sequenceLength * params['numRepetitions'])
    seqIndex = self._getIterCount() % (sequenceLength * params['numRepetitions'])
    state['angularPosn'] = params['maxAngularPosn'] \
                           - state['angularVelocity'] * seqIndex