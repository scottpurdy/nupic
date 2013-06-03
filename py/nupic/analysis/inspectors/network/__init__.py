# ----------------------------------------------------------------------
#  Copyright (C) 2006-2008 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""
This file exports all NetworkInspectors.
"""

import os
import glob
import nupic

# Import NetworkInspector and NetworkInspectorHandler
from nupic.analysis.inspectors.network.NetworkInspector import *

# Create networkInspectors as a list of all network inspector subclasses

files = [os.path.splitext(os.path.split(x)[1])[0] for x in
             glob.glob(os.path.join(os.path.split(__file__)[0], '*.py'))]
files.remove('__init__')
files.remove('NetworkInspector')

#files = [(f, f[:-1]) for f in files if f.endswith('2')]
files = [(f, f) for f in files]

for f in files:
  exec('from nupic.analysis.inspectors.network.%s import %s' % (f[0], f[1]))
networkInspectors = map(eval, [f[1] for f in files])