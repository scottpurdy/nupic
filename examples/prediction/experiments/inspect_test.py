# ----------------------------------------------------------------------
#  Copyright (C) 2010 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

from nupic.engine import *
import os, sys

os.chdir(sys.argv[1] + '/networks')

for name in ('trained_l1.nta', 'trained.nta'):
  if os.path.exists(name):
    break

n = Network(name)
n.inspect()