#!/usr/bin/env python
# ----------------------------------------------------------------------
# Copyright (C) 2013 Numenta Inc. All rights reserved.
#
# The information and source code contained herein is the
# exclusive property of Numenta Inc.  No part of this software
# may be used, reproduced, stored or distributed in any form,
# without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""Tests for the C++ implementation of the temporal pooler."""

import unittest2 as unittest

from nupic.research.TP10X2 import TP10X2

import tp_test

tp_test.TP = TP10X2

TP10X2Test = tp_test.TPTest



if __name__ == '__main__':
  unittest.main()
