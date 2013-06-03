# ----------------------------------------------------------------------
#  Copyright (C) 2010 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------


from nupic.frameworks.prediction.helpers import importBaseDescription

config = dict(
      #sensorVerbosity=3,
      iterationCount = 25000,
      spPeriodicStats = 0,

      #numAValues = 25,
      #numBValues = 25,

      #encodingFieldStyleA = 'contiguous',    
      #encodingFieldWidthA = 50,
      #encodingOnBitsA =     5,

      #encodingFieldStyleB = 'contiguous',    
      #encodingFieldWidthB = 25,       
      #encodingOnBitsB =     5,        

      b0Likelihood = None,
    )
            
mod = importBaseDescription('../base/description.py', config)
locals().update(mod.__dict__)


