# ----------------------------------------------------------------------
#  Copyright (C) 2011 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------


# CLAModel-specific experiment task callbacks that may be used
# in setup, postIter, and finish callback lists

import os

from nupic.support.fshelpers import makeDirectoryFromAbsolutePath

from clamodel import CLAModel


################################################################################
def claModelControlEnableSPLearningCb(claModel):
  """ Enables learning in the CLA model's Spatial Pooler

  See also claModelControlDisableSPLearningCb.

  claModel:  pointer to a CLAModel instance

  Returns: nothing
  """

  assert isinstance(claModel, CLAModel)

  claModel._getSPRegion().setParameter('learningMode', True)
  return


################################################################################
def claModelControlDisableSPLearningCb(claModel):
  """ Disables learning in the CLA model's Spatial Pooler, while retaining
  the ability to re-enable SP learning in the future.

  See also: claModelControlEnableSPLearningCb.
  See also: modelcallbacks.modelControlFinishLearningCb.

  claModel:  pointer to a CLAModel instance

  Returns: nothing
  """

  assert isinstance(claModel, CLAModel)

  claModel._getSPRegion().setParameter('learningMode', False)
  return


################################################################################
def claModelControlEnableTPLearningCb(claModel):
  """ Enables learning in the CLA model's Temporal Pooler

  See also claModelControlDisableTPLearningCb.

  claModel:  pointer to a CLAModel instance

  Returns: nothing
  """

  assert isinstance(claModel, CLAModel)

  claModel._getTPRegion().setParameter('learningMode', True)
  return


################################################################################
def claModelControlDisableTPLearningCb(claModel):
  """ Disables learning in the CLA model's Temporal Pooler, while retaining
  the ability to re-enable TP learning in the future.

  See also: claModelControlEnableTPLearningCb.
  See also: modelcallbacks.modelControlFinishLearningCb.

  claModel:  pointer to a CLAModel instance

  Returns: nothing
  """

  assert isinstance(claModel, CLAModel)

  claModel._getTPRegion().setParameter('learningMode', False)
  return



################################################################################
class CLAModelPickleSPInitArgs(object):
  """ Saves FDRCSpatial2 initialization args
  """
  def __init__(self, filePath):
    """
    filePath: path of file where SP __init__ args are to be saved
    """

    self.__filePath = filePath

    return


  def __call__(self, claModel):

    import pickle

    # Get the SP args dictionary
    assert isinstance(claModel, CLAModel)

    spRegion = claModel._getSPRegion().getSelf()

    sfdr = spRegion._sfdr

    initArgsDict = sfdr._initArgsDict


    # Write it out to a file as json
    absFilePath = os.path.abspath(self.__filePath)

    absDir = os.path.dirname(absFilePath)
    makeDirectoryFromAbsolutePath(absDir)

    with open(absFilePath, 'wb') as pickleFile:
      pickle.dump(initArgsDict, pickleFile)

    return



################################################################################
class CLAModelPickleTPInitArgs(object):
  """ Saves TP10X2 initialization args
  """
  def __init__(self, filePath):
    """
    filePath: path of file where TP __init__ args are to be saved
    """

    self.__filePath = filePath

    return


  def __call__(self, claModel):

    import pickle

    # Get the TP args dictionary
    assert isinstance(claModel, CLAModel)

    tpRegion = claModel._getTPRegion().getSelf()

    tfdr = tpRegion._tfdr

    initArgsDict = tfdr._initArgsDict


    # Write it out to a file as json
    absFilePath = os.path.abspath(self.__filePath)

    absDir = os.path.dirname(absFilePath)
    makeDirectoryFromAbsolutePath(absDir)

    with open(absFilePath, 'wb') as pickleFile:
      pickle.dump(initArgsDict, pickleFile)

    return