# ----------------------------------------------------------------------
#  Copyright (C) 2010 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""
This file defines HorizBlock a horizontal-only block explorer.
"""

from nupic.regions.PictureSensor import PictureSensor

#+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
# BlockPictureExplorer

class BlockPictureExplorer(PictureSensor.PictureExplorer):
  """
  A base plugin class that implements "explorer" functionality for
  specific categories; this functionality controls the manner in
  which pictures are swept.

  To add support for a new type of explorer to the PictureSensor,
  perform the following:

  1. Derive a sub-class from this PictureExplorer base class;
  2. Implement the following mandatory methods:
     initSequence() - create initial state for a new sequence
     updateSequence()  - update state of an existing sequence
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
    self._presentNextPosn(state, params)

  def updateSequence(self, state, params):
    self._presentNextPosn(state, params)


  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  # Internal helper method(s)

  def _presentNextPosn(self, state, params):
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