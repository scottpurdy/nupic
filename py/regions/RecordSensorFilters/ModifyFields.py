# ----------------------------------------------------------------------
#  Copyright (C) 2010 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""
This file defines the 'starBlock' explorer.

"""

import numpy

#############################################################################
# AddNoise RecordSensor filter

class ModifyFields:
  """
  This RecordSensor filter adds noise to the input

  """

  #############################################################################
  def __init__(self, fields=[], operation='setToZero', seed=-1):
    """ Construct the filter

    Parameters:
    -------------------------------------------------
    fields:     List of field names to modify
    operation:  Operation to perform on the fields, options include:
                 - setToZero: set fields to all 0's.

    """

    assert operation in ['setToZero']

    self.operation = operation

    # If fields is a simple string, make it a list
    if not hasattr(fields, '__iter__'):
      fields = [fields]
    self.fields = fields

    if seed != -1:
      numpy.random.seed(seed)


  ########################################################################
  def process(self, encoder, data):
    """ Modify the data in place, adding noise
    """

    if len(self.fields) == 0:
      return

    # Impelement self.operation on each named field
    for field in self.fields:
      (offset, width) = encoder.getFieldDescription(field)

      if self.operation == 'setToZero':
        data[offset: offset+width] = 0

      else:
        assert (False)