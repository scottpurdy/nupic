# ----------------------------------------------------------------------
# Copyright (C) 2012 Numenta Inc. All rights reserved.
#
# The information and source code contained herein is the
# exclusive property of Numenta Inc.  No part of this software
# may be used, reproduced, stored or distributed in any form,
# without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""Module providing a factory for instantiating a CLA classifier."""

from nupic.algorithms.CLAClassifier import CLAClassifier
from nupic.algorithms.cla_classifier_diff import CLAClassifierDiff
from nupic.bindings.algorithms import FastCLAClassifier
from nupic.support.configuration import Configuration



class CLAClassifierFactory(object):
  """Factory for instantiating CLA classifiers."""


  @staticmethod
  def create(*args, **kwargs):
    impl = kwargs.pop('implementation', None)
    if impl is None:
      impl = Configuration.get('nupic.opf.claClassifier.implementation')
    if impl == 'py':
      return CLAClassifier(*args, **kwargs)
    elif impl == 'cpp':
      return FastCLAClassifier(*args, **kwargs)
    elif impl == 'diff':
      return CLAClassifierDiff(*args, **kwargs)
    else:
      raise ValueError('Invalid classifier implementation (%s). Value must be '
                       '"py" or "cpp".')
