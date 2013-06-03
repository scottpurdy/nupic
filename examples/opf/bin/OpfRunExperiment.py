# ----------------------------------------------------------------------
# Copyright (C) 2011-2013 Numenta Inc. All rights reserved.
#
# The information and source code contained herein is the
# exclusive property of Numenta Inc. No part of this software
# may be used, reproduced, stored or distributed in any form,
# without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""This script is a command-line client of Online Prediction Framework (OPF).
It executes a single expiriment.
"""


import sys

from nupic.frameworks.opf.experiment_runner import (runExperiment,
                                                    initExperimentPrng)
import nupic.support



def main():
  """Run according to options in sys.argv"""
  # Init the NuPic logging configuration from the nupic-logging.conf configuration
  # file. This is found either in the NTA_CONF_DIR directory (if defined) or
  # in the 'conf' subdirectory of the NuPic install location.
  nupic.support.initLogging(verbose=True)

  # Initialize PRNGs
  initExperimentPrng()

  # Run it!
  runExperiment(sys.argv[1:])



if __name__ == "__main__":
  main()
