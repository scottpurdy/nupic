#! /usr/bin/env python
# ----------------------------------------------------------------------
#  Copyright (C) 2011 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

'''
A series of functions useful to serializing data beyond json or pickle
'''

import json
import bz2

#########################################################
def pack(pyObject):
  '''
  Serialize and zip a py object

  Using JSON rather than Pickle due to C* mailing list suggestions:
   - JSON is multi-language friendly
   - Unpickling data can lead to arbitrary code execution
  '''
  return bz2.compress(json.dumps(pyObject))


#########################################################
def unpack(packedData):
  '''
  Unzip and de-serialize a python object
  '''
  return json.loads(bz2.decompress(packedData))