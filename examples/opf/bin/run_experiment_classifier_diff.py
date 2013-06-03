#!/usr/bin/env python
# ----------------------------------------------------------------------
# Copyright (C) 2012-2013 Numenta Inc. All rights reserved.
#
# The information and source code contained herein is the
# exclusive property of Numenta Inc. No part of this software
# may be used, reproduced, stored or distributed in any form,
# without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""This script is a command-line client of Online Prediction Framework (OPF).
It executes a single experiment and diffs the results for the CLAClassifier and
FastCLAClassifier.
"""

import sys

from nupic.algorithms.cla_classifier_diff import CLAClassifierDiff
from nupic.algorithms.cla_classifier_factory import CLAClassifierFactory
from nupic.frameworks.opf.experiment_runner import (runExperiment,
                                                    initExperimentPrng)
from nupic.support import initLogging



def main():
  """Run according to options in sys.argv and diff classifiers."""
  # Init the NuPic logging configuration from the nupic-logging.conf
  # configuration file. This is found either in the NTA_CONF_DIR directory
  # (if defined) or in the 'conf' subdirectory of the NuPic install location.
  initLogging(verbose=True)

  # Initialize PRNGs
  initExperimentPrng()

  # Mock out the creation of the CLAClassifier.
  @staticmethod
  def _mockCreate(*args, **kwargs):
    kwargs.pop('implementation', None)
    return CLAClassifierDiff(*args, **kwargs)
  CLAClassifierFactory.create = _mockCreate

  # Run it!
  runExperiment(sys.argv[1:])



if __name__ == "__main__":
  main()
