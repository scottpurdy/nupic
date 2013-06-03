#!/usr/bin/env python
# ----------------------------------------------------------------------
# Copyright (C) 2012 Numenta Inc. All rights reserved.
#
# The information and source code contained herein is the
# exclusive property of Numenta Inc.  No part of this software
# may be used, reproduced, stored or distributed in any form,
# without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""Unit tests for the FastCLAClassifier.

This test extends the test for the Python CLAClassifier to ensure that both
classifiers and their tests stay in sync.
"""

import os
import sys
import unittest2 as unittest

from nupic.bindings.algorithms import FastCLAClassifier

# Add the tests path to sys.path so we can import cla_classifier_test.
testPath = os.path.join(os.getcwd(), __file__)
for _ in xrange(5):
  testPath = os.path.split(testPath)[0]
sys.path.append(testPath)

# Don't import the CLAClassifierTest directly or the unittest.main() will pick
# it up and run it.
from py.nupic.algorithms import cla_classifier_test



class FastCLAClassifierTest(cla_classifier_test.CLAClassifierTest):
  """Unit tests for FastCLAClassifier class."""


  def setUp(self):
    self._classifier = FastCLAClassifier



if __name__ == '__main__':
  unittest.main()
