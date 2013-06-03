#!/usr/bin/env python
# ----------------------------------------------------------------------
# Copyright (C) 2012 Numenta Inc. All rights reserved.
#
# The information and source code contained herein is the
# exclusive property of Numenta Inc.  No part of this software
# may be used, reproduced, stored or distributed in any form,
# without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""Unit tests for the clamodel module."""

import unittest2 as unittest

from nupic.frameworks.opf.clamodel import CLAModel


class CLAModelTest(unittest.TestCase):
  """CLAModel unit tests."""

  def testRemoveUnlikelyPredictionsEmpty(self):
    result = CLAModel._removeUnlikelyPredictions({}, 0.01, 3)
    self.assertDictEqual(result, {})

  def testRemoveUnlikelyPredictionsSingleValues(self):
    result = CLAModel._removeUnlikelyPredictions({1: 0.1}, 0.01, 3)
    self.assertDictEqual(result, {1: 0.1})
    result = CLAModel._removeUnlikelyPredictions({1: 0.001}, 0.01, 3)
    self.assertDictEqual(result, {1: 0.001})

  def testRemoveUnlikelyPredictionsLikelihoodThresholds(self):
    result = CLAModel._removeUnlikelyPredictions({1: 0.1, 2: 0.001}, 0.01, 3)
    self.assertDictEqual(result, {1: 0.1})
    result = CLAModel._removeUnlikelyPredictions({1: 0.001, 2: 0.002}, 0.01, 3)
    self.assertDictEqual(result, {2: 0.002})
    result = CLAModel._removeUnlikelyPredictions({1: 0.002, 2: 0.001}, 0.01, 3)
    self.assertDictEqual(result, {1: 0.002})

  def testRemoveUnlikelyPredictionsMaxPredictions(self):
    result = CLAModel._removeUnlikelyPredictions({1: 0.1, 2: 0.2, 3: 0.3},
                                                 0.01, 3)
    self.assertDictEqual(result, {1: 0.1, 2: 0.2, 3: 0.3})
    result = CLAModel._removeUnlikelyPredictions(
        {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.4}, 0.01, 3)
    self.assertDictEqual(result, {2: 0.2, 3: 0.3, 4: 0.4})

  def testRemoveUnlikelyPredictionsComplex(self):
    result = CLAModel._removeUnlikelyPredictions(
        {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.004}, 0.01, 3)
    self.assertDictEqual(result, {1: 0.1, 2: 0.2, 3: 0.3})
    result = CLAModel._removeUnlikelyPredictions(
        {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.4, 5: 0.005}, 0.01, 3)
    self.assertDictEqual(result, {2: 0.2, 3: 0.3, 4: 0.4})
    result = CLAModel._removeUnlikelyPredictions(
        {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.004, 5: 0.005}, 0.01, 3)
    self.assertDictEqual(result, {1: 0.1, 2: 0.2, 3: 0.3})


if __name__ == '__main__':
  unittest.main()
