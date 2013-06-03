# ----------------------------------------------------------------------
#  Copyright (C) 2006-2008 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""
This file defines Block1DOFPictureExplorer, an explorer for
PictureSensor.
"""

from nupic.regions.PictureSensor import PictureSensor

#+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
# Block1DOFPictureExplorer

class Block1DOFPictureExplorer(PictureSensor.PictureExplorer):
  """
  Presents each category at an Nx1 "block" of shifted positions
  centered upon the centroid of the canvas, where N is 2R+1
  (where R is the radialLength); each such presentation is
  spaced radialStep pixels apart in both X and Y dimensions.
  """

  @classmethod
  def queryRelevantParams(klass):
    """
    Returns a sequence of parameter names that are relevant to
    the operation of the explorer.

    May be extended or overridden by sub-classes as appropriate.
    """
    return ( 'radialLength', 'radialStep', )

  def initSequence(self, state, params):
    self._presentNextBlockPosn(state, params)

  def updateSequence(self, state, params):
    self._presentNextBlockPosn(state, params)


  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  # Internal helper method(s)

  def _presentNextBlockPosn(self, state, params):
    """
    Compute the appropriate category and block position
    deterministically based on the current iteration count.
    """
    # Compute iteration indices
    edgeLen = 2 * params['radialLength'] + 1
    numBlocksPerCat = edgeLen
    numCats = self._getNumCategories()
    numBlocks = numBlocksPerCat * numCats
    blockCounter = self._getIterCount() % numBlocks
    catIndex = blockCounter // numBlocksPerCat
    blockCatIndex = blockCounter % numBlocksPerCat
    # Compute position within onion block
    posnX = ((blockCatIndex % edgeLen) - params['radialLength']) * params['radialStep']

    # Override default state
    state['posnX'] = posnX
    state['posnY'] = 0
    state['velocityX'] = 0
    state['velocityY'] = 0
    state['angularPosn'] = 0
    state['angularVelocity'] = 0
    state['catIndex'] = catIndex