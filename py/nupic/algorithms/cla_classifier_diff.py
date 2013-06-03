# ----------------------------------------------------------------------
# Copyright (C) 2012 Numenta Inc. All rights reserved.
#
# The information and source code contained herein is the
# exclusive property of Numenta Inc. No part of this software
# may be used, reproduced, stored or distributed in any form,
# without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""CLA classifier diff tool.

This class can be used just like versions of the CLA classifier but internally
creates instances of each CLA classifier. Each record is fed to both
classifiers and the results are checked for differences.
"""

import cPickle as pickle

from nupic.algorithms.CLAClassifier import CLAClassifier
from nupic.bindings.algorithms import FastCLAClassifier

CALLS_PER_SERIALIZE = 100



class CLAClassifierDiff(object):
  """Classifier-like object that diffs the output from different classifiers.

  Instances of each version of the CLA classifier are created and each call to
  compute is passed to each version of the classifier. The results are diffed
  to make sure the there are no differences.

  Optionally, the classifiers can be serialized and deserialized after a
  specified number of calls to compute to ensure that serialization does not
  cause discrepencies between the results.

  TODO: Check internal state as well.
  TODO: Provide option to write output to a file.
  TODO: Provide record differences without throwing an exception.
  """


  __VERSION__ = 'CLAClassifierDiffV1'


  def __init__(self, steps=(1,), alpha=0.001, actValueAlpha=0.3, verbosity=0,
               callsPerSerialize=CALLS_PER_SERIALIZE):
    self._claClassifier = CLAClassifier(steps, alpha, actValueAlpha, verbosity)
    self._fastCLAClassifier = FastCLAClassifier(steps, alpha, actValueAlpha,
                                                verbosity)
    self._calls = 0
    self._callsPerSerialize = callsPerSerialize


  def compute(self, patternNZ, classification, learn, infer):
    result1 = self._claClassifier.compute(patternNZ, classification, learn,
                                          infer)
    result2 = self._fastCLAClassifier.compute(patternNZ, classification, learn,
                                              infer)
    self._calls += 1
    # Check if it is time to serialize and deserialize.
    if self._calls % self._callsPerSerialize == 0:
      self._claClassifier = pickle.loads(pickle.dumps(self._claClassifier))
      self._fastCLAClassifier = pickle.loads(pickle.dumps(
          self._fastCLAClassifier))
    # Assert both results are the same type.
    assert type(result1) == type(result2)
    # Assert that the keys match.
    assert set(result1.keys()) == set(result2.keys())
    # Assert that the values match.
    for k, l in result1.iteritems():
      assert type(l) == type(result2[k])
      for i in xrange(len(l)):
        assert abs(float(l[i]) - float(result2[k][i])) < 0.0000001, (
            'Python CLAClassifier has value %f and C++ FastCLAClassifier has '
            'value %f.' % (l[i], result2[k][i]))
    return result1
