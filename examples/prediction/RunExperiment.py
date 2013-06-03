# ----------------------------------------------------------------------
#  Copyright (C) 2010-2011 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------
import os
import glob
import sys
import numpy
import random
import traceback

import cProfile
import pstats

from nupic.frameworks.prediction.experiment import Experiment
from nupic.frameworks.prediction import (utils,
                                         helpers)

# Keep GUIs around, so they don't just evaporate
gui = []

# experiment is a global variable so that if you %run RunExperiment.py
# in ipython, the experiment object is available afterwards
experiment = None

def runExperiment(experimentDirectory, experimentOptions):
  o = experimentOptions
  # Clean aggregation datasets if needed
  #if o['clearAggregationDatasets']:
  #helpers.cleanAggregationDatasets()
      
  global experiment

  experiment = Experiment(path=experimentDirectory, runtimeOptions=experimentOptions)
  
  
  
  # Create GUIs as needed
  if not experimentOptions['postProcessOnly']:
    if o['runGUI']:
      # Only import these if the gui is requested, because
      # they import further modules that require a console
      # and exit if there is no console (as in the autobuild)
      from nupic.frameworks.prediction.GUIs import TrainingGUI, InferenceGUI
      if not (o['createNetworkOnly'] or o['runInferenceOnly']):
        gui.append(TrainingGUI(experiment))
      gui.append(InferenceGUI(experiment))
      for i, g in enumerate(gui):
        g.start()
    else:
      experiment.run()

  if experimentOptions['postProcess']:
    from nupic.frameworks.prediction.postprocess import postProcess
    try:
      postProcess(experiment)
      experiment.writeResults()
      if os.environ.has_key('NTA_AMAZON_SYNC_DATA'):
        print "Deleting log files"
        inferenceDir = os.path.join(experimentDirectory,"inference")
        logFiles = glob.glob(os.path.join(inferenceDir,"*.txt"))
        for f in logFiles:
          try:
            os.remove(f)
          except:
            print "Couldn't remove log file:",f
    except Exception, e:
      message = "Post processing has failed, %s" % str(e.args)
      e.args = (message,) +e.args[1:]
      #traceback.print_exc(file=sys.stdout)
      raise 

def profileRunExperiment(*args, **keywords):
  cProfile.runctx(
      "runExperiment(*args, **keywords)",
      globals=globals(),
      locals=dict(args=args, keywords=keywords),
      filename="re.profile"
    )


def usage(parser, message):
  print parser.get_usage()
  print message
  sys.exit(1)


def main():
  random.seed(42)
  numpy.random.seed(42)
  experiments, experimentOptions, otherOptions = Experiment.parseOptions(sys.argv[1:])
  
  print experimentOptions
  print otherOptions
  
  if len(experiments) != 1:
    raise RuntimeError("You must specify exactly one experiment")

  # We want to list all the available checkpoints
  if otherOptions['listAvailableCheckpoints']:
    utils.printAvailableCheckpoints(experiments[0])
    sys.exit()
    
  if len(experiments) != 1:
    usage(parser, "Exactly one experiment may be specified")

  if otherOptions['profilePython']:
    _runExperiment = profileRunExperiment
  else:
    _runExperiment = runExperiment

  _runExperiment(experiments[0], experimentOptions)

  if otherOptions['profilePython']:
    p = pstats.Stats("re.profile")
    p.strip_dirs().sort_stats("cumulative").print_stats(30)


if __name__ == "__main__":
  # "Secret" command-line option for running GUI testing
  if len(sys.argv) == 2 and sys.argv[1] == '-t':
    #sys.argv = [sys.argv[0], 'gym/IRP']
    sys.argv = [sys.argv[0], 'traffic/1', '-g', '-v 3']
  main()


