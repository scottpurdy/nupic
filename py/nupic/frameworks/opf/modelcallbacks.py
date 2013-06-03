# ----------------------------------------------------------------------
#  Copyright (C) 2011 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------


# Generic model experiment task callbacks that may be used
# in setup, postIter, and finish callback lists



################################################################################
def modelControlFinishLearningCb(model):
  """ Passes the "finish learning" command to the model.  NOTE: Upon completion
  of this command, learning may not be resumed on the given instance of
  the model (e.g., the implementation may prune data structures that are
  necessary for learning)

  model:  pointer to the Model instance

  Returns: nothing
  """

  model.finishLearning()
  return