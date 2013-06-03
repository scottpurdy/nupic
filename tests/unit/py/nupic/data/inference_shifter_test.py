#!/usr/bin/env python
# ----------------------------------------------------------------------
# Copyright (C) 2012, Numenta Inc. All rights reserved.
#
# The information and source code contained herein is the
# exclusive property of Numenta Inc.  No part of this software
# may be used, reproduced, stored or distributed in any form,
# without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""Unit tests for InferenceShifter."""

from nupic.data.inference_shifter import InferenceShifter
from nupic.frameworks.opf.opfutils import InferenceElement, ModelResult
from nupic.support.unittesthelpers.testcasebase import (TestCaseBase,
                                                        unittest)


class TestInferenceShifter(TestCaseBase):

  def _shiftAndCheck(self, inferences, expectedOutput):
    inferenceShifter = InferenceShifter()
    for inference, expected in zip(inferences, expectedOutput):
      inputResult = ModelResult(inferences=inference)
      outputResult = inferenceShifter.shift(inputResult)
      self.assertEqual(outputResult.inferences, expected)

  def testNoShift(self):
    for element in (InferenceElement.anomalyScore,
                    InferenceElement.classification,
                    InferenceElement.classConfidences):
      inferences = [
          {element: 1},
          {element: 2},
          {element: 3},
      ]
      expectedOutput = [
          {element: 1},
          {element: 2},
          {element: 3},
      ]
      self._shiftAndCheck(inferences, expectedOutput)

  def testNoShiftMultipleValues(self):
    for element in (InferenceElement.anomalyScore,
                    InferenceElement.classification,
                    InferenceElement.classConfidences):
      inferences = [
          {element: [1, 2, 3]},
          {element: [4, 5, 6]},
          {element: [5, 6, 7]},
      ]
      expectedOutput = [
          {element: [1, 2, 3]},
          {element: [4, 5, 6]},
          {element: [5, 6, 7]},
      ]
      self._shiftAndCheck(inferences, expectedOutput)

  def testSingleShift(self):
    for element in (InferenceElement.prediction,
                    InferenceElement.encodings):
      inferences = [
          {element: 1},
          {element: 2},
          {element: 3},
      ]
      expectedOutput = [
          {element: None},
          {element: 1},
          {element: 2},
      ]
      self._shiftAndCheck(inferences, expectedOutput)

  def testSingleShiftMultipleValues(self):
    for element in (InferenceElement.prediction,
                    InferenceElement.encodings):
      inferences = [
          {element: [1, 2, 3]},
          {element: [4, 5, 6]},
          {element: [5, 6, 7]},
      ]
      expectedOutput = [
          {element: [None, None, None]},
          {element: [1, 2, 3]},
          {element: [4, 5, 6]},
      ]
      self._shiftAndCheck(inferences, expectedOutput)

  def testMultiStepShift(self):
    for element in (InferenceElement.multiStepPredictions,
                    InferenceElement.multiStepBestPredictions):
      inferences = [
          {element: {2: 1}},
          {element: {2: 2}},
          {element: {2: 3}},
          {element: {2: 4}},
      ]
      expectedOutput = [
          {element: {2: None}},
          {element: {2: None}},
          {element: {2: 1}},
          {element: {2: 2}},
      ]
      self._shiftAndCheck(inferences, expectedOutput)

  def testMultiStepShiftMultipleValues(self):
    for element in (InferenceElement.multiStepPredictions,
                    InferenceElement.multiStepBestPredictions):
      inferences = [
          {element: {2: [1, 11]}},
          {element: {2: [2, 12]}},
          {element: {2: [3, 13]}},
          {element: {2: [4, 14]}},
      ]
      expectedOutput = [
          {element: {2: None}},
          {element: {2: None}},
          {element: {2: [1, 11]}},
          {element: {2: [2, 12]}},
      ]
      self._shiftAndCheck(inferences, expectedOutput)

  def testDifferentMultiStepsShift(self):
    for element in (InferenceElement.multiStepPredictions,
                    InferenceElement.multiStepBestPredictions):
      inferences = [
          {element: {2: 1, 3: 5}},
          {element: {2: 2, 3: 6}},
          {element: {2: 3, 3: 7}},
          {element: {2: 4, 3: 8}},
      ]
      expectedOutput = [
          {element: {2: None, 3: None}},
          {element: {2: None, 3: None}},
          {element: {2: 1, 3: None}},
          {element: {2: 2, 3: 5}},
      ]
      self._shiftAndCheck(inferences, expectedOutput)

  def testDifferentMultiStepsShiftMultipleValues(self):
    for element in (InferenceElement.multiStepPredictions,
                    InferenceElement.multiStepBestPredictions):
      inferences = [
          {element: {2: [1, 11], 3: [5, 15]}},
          {element: {2: [2, 12], 3: [6, 16]}},
          {element: {2: [3, 13], 3: [7, 17]}},
          {element: {2: [4, 14], 3: [8, 18]}},
      ]
      expectedOutput = [
          {element: {2: None, 3: None}},
          {element: {2: None, 3: None}},
          {element: {2: [1, 11], 3: None}},
          {element: {2: [2, 12], 3: [5, 15]}},
      ]
      self._shiftAndCheck(inferences, expectedOutput)


if __name__ == '__main__':
  unittest.main()
