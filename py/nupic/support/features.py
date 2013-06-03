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
This module implements the Feature Flags system.

Summary:

  Based on the environment your program is run in you may want various features
  to be displayed and others not.

  Based on the type of user who is using Grok you may want them to see various
  features and not others.

  These two things can be accomplished using Feature Flags.

  Feature Flags wrap sections of code in IF/THEN blocks to isolate functionality
  from running code.

  This allows you to inline new features without branching files into file.py and
  file2.py.

  This also allows you to release un-tested, underdevelopment, or experimental
  features directly to production with confidence that those code paths won't
  get run until such time as they are 'released' to a group of users for testing
  or to all users for a launch.

  DEV NOTE: To set personal Feature Flag over-rides copy conf/devconf-example.py
            to devconf.py and edit as desired.

'''
import os
import sys
import imp

from nupic.support.features_list import FEATURES_LIST
from nupic.support.feature_groups import GROUPS

class Features(object):
  '''
  This class can be used to retrieve available and calculated features for
  a given combination of running environment and user

  The class is for documentation purposes as all the methods are statically
  accessible.

  Modeled after Ron's excellent Configuration class
  '''

  ###############################################################################
  @staticmethod
  def hasFeature(feature, group = False, addList = False, removeList = False):
    '''
    This is the primary method of the class that will return True or False
    based on the current environment and user.

    This is the 'Flag' part of Feature Flags.
    '''

    return (feature in Features.getFeatures(group, addList, removeList))

  @staticmethod
  def getFeatures(group = False, addList = False, removeList = False):
    '''
    Returns a list of all the active features for the current env/user

    groups:         This is a list of groups the current user belongs to
    addList:        A list of one-off features to add
    removeList:     A list of one-off features to remove
    '''

    # Calculate groups
    if group:
      featureList = Features._getFeaturesForGroup(group)
    else:
      featureList = Features._getFeaturesForGroup('BASE')

    # Calculate user one-offs
    if addList:
      featureList.extend(addList)
    if removeList:
      for item in removeList:
        if item in featureList:
          featureList.remove(item)

    # Caclulate developer configuration
    if 'TRUNK' in os.environ:
      confDir = os.path.join(os.environ['TRUNK'], 'conf')
      confFilepath = os.path.join(confDir, 'developer.py')
      if os.path.exists(confFilepath):
        sys.path.append(confDir)
        import developer
        featureList.extend(developer.FEATURES['ADD'])
        for item in developer.FEATURES['REMOVE']:
          if item in featureList:
            featureList.remove(item)

    return featureList

  @staticmethod
  def _getFeaturesForGroup(group):
    '''
    Using feature_groups.py calculate the set of features available to the given
    group
    '''
    return GROUPS[group]

  @staticmethod
  def getAllFeatures():
    '''
    Returns a list of all known features (essentially the contents of feature_list.py)
    '''
    for feature in FEATURES_LIST:
      print feature['name'] + '\t\t' + feature['description']

  @staticmethod
  def getAllGroups():
    '''
    Returns a list of all known feature groups
    '''
    return [group for group, features in GROUPS.iteritems()]