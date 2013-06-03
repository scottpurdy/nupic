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
This module implements an in-memory cache for keys retrieved from off-world
databases.

It is a fixed sized least-recently-used cache, when the cache size reaches
a limit the oldest 20% of keys are removed.

Key age is updated each time it is accessed
'''

import math

from ordereddict.OrderedDict import OrderedDict

class KeyCache(object):

  def __init__(self, keyLimit = 1000):

    # We'll need to hold data internally
    self.internalDict = OrderedDict()

    # Set our limit
    self.keyLimit = keyLimit

  def set(self, key, value):
    '''
    This will accept a new value to add to the cache also checking for old keys
    '''

    # Set up our internal structure
    self.internalDict[key] = value

    # Garbage Collection
    if len(self.internalDict) > self.keyLimit:
      self._garbageCollectKeys()

  def get(self, key):
    '''
    This method will return a key if it exists in the cache, otherwise it will
    return None.

    Each time a key is accessed it will also update the key's age.
    '''

    rv = self.internalDict.get(key)
    if rv:
      # Update position in dict
      self.internalDict[key] = self.internalDict.pop(key)

    return rv

  def _garbageCollectKeys(self):
    '''
    If we're ever over our key limit, clean out old keys
    '''

    keysToRemove = int(math.floor(self.keyLimit * .2))

    for i in range(keysToRemove):
        self.internalDict.popitem(False)