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
{ 'modelParams': { 'clParams': { 'clVerbosity': 0},
                   'inferenceType': 'NontemporalMultiStep',
                   'sensorParams': { 'encoders': { 'consumption': { 'clipInput': True,
                                                                    'fieldname': u'consumption',
                                                                    'n': 28,
                                                                    'name': u'consumption',
                                                                    'type': 'AdaptiveScalarEncoder',
                                                                    'w': 21},
                                                   'timestamp_dayOfWeek': None,
                                                   'timestamp_timeOfDay': { 'fieldname': u'timestamp',
                                                                            'name': u'timestamp_timeOfDay',
                                                                            'timeOfDay': ( 21,
                                                                                           8),
                                                                            'type': 'DateEncoder'},
                                                   'timestamp_weekend': None},
                                     'verbosity': 0},
                   'spParams': { 'spVerbosity': 0},
                   'tpParams': { 'activationThreshold': 14,
                                 'minThreshold': 12,
                                 'verbosity': 1}}}

mod = importBaseDescription('../hotgym/description.py', config)
locals().update(mod.__dict__)
