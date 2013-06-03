# ----------------------------------------------------------------------
#  Copyright (C) 2012 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

## This file defines parameters for a prediction experiment.

import os
from nupic.frameworks.opf.expdescriptionhelpers import importBaseDescription

# the sub-experiment configuration
config = \
{ 
  'dataSource': 'file://' + os.path.join(os.path.dirname(__file__), 
                                         '../datasets/simple_0.csv'),
                                         
  'windowSize': 25,
  'modelParams': { 
    'sensorParams': { 
      'verbosity': 0,
      'encoders': {
        'timestamp_timeOfDay': None,
        'timestamp_dayOfWeek': None,
        'field2': None,
      }
    },
    'clParams': {
      'clVerbosity': 0,
    }
  }
}

mod = importBaseDescription('../base/description.py', config)
locals().update(mod.__dict__)
