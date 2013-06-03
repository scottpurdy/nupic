# ----------------------------------------------------------------------
#  Copyright (C) 2011 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

# This file contains utility functions that are used
# internally by the prediction framework. It should not be
# imported by description files. (see helpers.py)


import logging
import inspect

def createLogger(obj):
  """Helper function to create a logger object for the current object with
  the standard Numenta prefix """
  if inspect.isclass(obj):
    myClass = obj
  else:
    myClass = obj.__class__
  logger = logging.getLogger(".".join(
    ['com.numenta', myClass.__module__, myClass.__name__]))
  return logger