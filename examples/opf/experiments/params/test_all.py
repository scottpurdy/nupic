#!/usr/bin/env python
# ----------------------------------------------------------------------
#  Copyright (C) 2012 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""Script for trying different model parameters for existing experiments."""

import os
from pprint import pprint
import time

from nupic.frameworks.opf import opfhelpers
from nupic.frameworks.opf.client import Client

# Experiment directories relative to "trunk/examples/opf/experiments."
EXPERIMENTS_FILE = 'successful_experiments.txt'


def testAll(experiments):
  experimentsDir = os.path.join(os.path.split(
      os.path.dirname(__file__))[:-1])[0]
  for experiment in experiments:
    experimentBase = os.path.join(os.getcwd(), experimentsDir, experiment)

    config, control = opfhelpers.loadExperiment(experimentBase)

    if control['environment'] == 'opfExperiment':
      experimentTasks = control['tasks']
      task = experimentTasks[0]
      datasetURI = task['dataset']['streams'][0]['source']

    elif control['environment'] == 'grok':
      datasetURI = control['dataset']['streams'][0]['source']

    metricSpecs = control['metrics']

    datasetPath = datasetURI[len("file://"):]
    for i in xrange(1024, 2176, 128):
      #config['modelParams']['tpParams']['cellsPerColumn'] = 16
      config['modelParams']['tpParams']['columnCount'] = i
      config['modelParams']['spParams']['columnCount'] = i
      print 'Running with 32 cells per column and %i columns.' % i
      start = time.time()
      result = runOneExperiment(config, control['inferenceArgs'], metricSpecs,
                                datasetPath)
      print 'Total time: %d.' % (time.time() - start)
      pprint(result)


def runOneExperiment(modelConfig, inferenceArgs, metricSpecs, sourceSpec,
                     sinkSpec=None):
  client = Client(modelConfig, inferenceArgs, metricSpecs, sourceSpec, sinkSpec)
  return client.run().metrics


if __name__ == '__main__':
  # Because of the duration of some experiments, it is often better to do one
  # at a time.
  testAll(('anomaly/temporal/saw_big',))
