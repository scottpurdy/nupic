#! /usr/bin/env python
# ----------------------------------------------------------------------
#  Copyright (C) 2011 Numenta Inc, All rights reserved,
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc, No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------


'''
DEVELOPER SPECIFIC CONFIGURATION FILE

Copy to devconf.py to enable.

This file should not be checked in, and should be added to your svn/git ignore lists
'''
from nupic.support.features_list import FEATURES_LIST

###############################################################################
# Features

FEATURES = {
  'ADD': [
    'increased_awesomeness',
    ],
  'REMOVE': [
    'bad_feature',
  ]
}


# All features in a given group must appear in the features.py file

validFeatureNames = [f['name'] for f in FEATURES_LIST]
for groupName, features in FEATURES.iteritems():
  for feature in features:
    if feature not in validFeatureNames:
      raise Exception('The feature "%s" is not a recognized feature name. Please '
                      'check your spelling and/or add it to '
                      'nupic/support/features_list.py' % feature)
      
###############################################################################