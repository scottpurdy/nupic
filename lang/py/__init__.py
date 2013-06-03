# ----------------------------------------------------------------------
#  Copyright (C) 2010 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------
import sys

# Jython doesn't yet support modules written in C/C++, like engine_internal
if not sys.platform.startswith('java'):
  from nupic.bindings import engine_internal

import os
rootDir = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "../../../.."))
