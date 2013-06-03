# ----------------------------------------------------------------------
#  Copyright (C) 2010 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""
This test trains and tests on data generated from a second order markov source model.  

If things are working correctly then, you should do as well as a 2-grams model


"""

import imp
from nupic.frameworks.prediction.helpers import importBaseDescription

config = dict(
              sensorVerbosity=0,
              spVerbosity=0,
              tpVerbosity=0,
              ppVerbosity=0,
              
              dataSetPackage = 'secondOrder2',

              iterationCountTrain=3000,
              iterationCountTest=250,
              trainTPRepeats = 1,
              
              spNumActivePerInhArea = 5,
              
              trainTP=True,
              tpNCellsPerCol = 10, 

              tpInitialPerm = 0.11,
              tpPermanenceInc = 0.05,
              tpPermanenceDec = 0.10,
              tpGlobalDecay = 0.05,
              tpMaxAge = 100,
              tpPAMLength = 1,
              #tpMaxSeqLength = 3,
              
              tpTimingEvery = 250
              )
              
mod = importBaseDescription('../base/description.py', config)
locals().update(mod.__dict__)



