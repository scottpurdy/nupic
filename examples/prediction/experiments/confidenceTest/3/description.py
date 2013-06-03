# ----------------------------------------------------------------------
#  Copyright (C) 2010 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""
Problem case:
1.) learn a-b-c  (2X, b-c probability = 0.2 after seeing a)
2.) learn b-c, ends up using same b-c connections as #1, (11X)
3.) learn a-b-d  (4X, b-d probability = 0.4 after seeing a)
4.) learn a-b-e  (3X, b-e probability = 0.4 after seeing a)

Without startCell mode, when we see a-b, we will predict c with 
highest probability because of #2, when in fact we should predict d:
inputPredScore_at1        :  1.0
inputPredScore_at2        :  0.222222222222
inputPredScore_at3        :  0.0
inputPredScore_at4        :  0.0


If we use startCell mode, we shouldn't have this problem and should get the
following scores:
inputPredScore_at1        :  1.0
inputPredScore_at2        :  0.444444444444
inputPredScore_at3        :  0.0
inputPredScore_at4        :  0.0

"""


from nupic.frameworks.prediction.helpers import importBaseDescription

config = dict(
              sensorVerbosity=0,
              spVerbosity=0,
              tpVerbosity=0,
              ppVerbosity=2,
              
              filenameTrain = 'confidence/confidence3.csv',
              filenameTest = 'confidence/confidence3.csv',

              iterationCountTrain=None,
              iterationCountTest=None,
              trainTPRepeats = 5,
              
              trainTP=True,
              )
              
mod = importBaseDescription('../base/description.py', config)
locals().update(mod.__dict__)


