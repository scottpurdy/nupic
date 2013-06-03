# ----------------------------------------------------------------------
#  Copyright (C) 2011-12 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""
Collection of utilities to process input data
"""

import datetime
# Workaround for this error: 
#  "ImportError: Failed to import _strptime because the import lockis held by 
#     another thread"
import _strptime

# These are the supported timestamp formats to parse. The first is used for
# serializing datetimes. Functions in this file rely on specific formats from
# this tuple so be careful when changing the indices for existing formats.
DATETIME_FORMATS = ('%Y-%m-%d %H:%M:%S.%f', '%Y-%m-%d %H:%M:%S:%f',
                    '%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d',
                    '%m/%d/%Y %H:%M', '%m/%d/%y %H:%M')


#############################################################################
def parseTimestamp(s):
  """Parses a textual datetime format and return a Python datetime object.

  The supported format is: yyyy-mm-dd h:m:s.ms

  The time component is optional
  hours are 00..23 (no AM/PM)
  minutes are 00..59
  seconds are 00..59
  micro-seconds are 000000..999999
  """
  s = s.strip()
  for pattern in DATETIME_FORMATS:
    try:
      return datetime.datetime.strptime(s, pattern)
    except ValueError:
      pass
  raise ValueError('The provided timestamp %s is malformed. The supported '
                   'formats are: [%s]' % (s, ', '.join(DATETIME_FORMATS)))


#############################################################################
def serializeTimestamp(t):
  return t.strftime(DATETIME_FORMATS[0])


#############################################################################
def serializeTimestampNoMS(t):
  return t.strftime(DATETIME_FORMATS[2])


#############################################################################
def parseBool(s):
  l = s.lower()
  if l in ("true", "t", "1"):
    return True
  if l in ("false", "f", "0"):
    return False
  raise Exception("Unable to convert string '%s' to a boolean value" % s)


#############################################################################
def floatOrNone(f):
  if f == 'None':
    return None
  return float(f)


#############################################################################
def intOrNone(i):
  if i.strip() == 'None' or i.strip() == 'NULL':
    return None
  return int(i)


#############################################################################
def escape(s):
  """Escape commas, tabs, newlines and dashes in a string

  Commas are encoded as tabs
  """
  if s is None:
    return ''
  
  assert isinstance(s, basestring), \
        "expected %s but got %s; value=%s" % (basestring, type(s), s)
  s = s.replace('\\', '\\\\')
  s = s.replace('\n', '\\n')
  s = s.replace('\t', '\\t')
  s = s.replace(',', '\t')
  return s


#############################################################################
def unescape(s):
  """Unescapes a string that may contain commas, tabs, newlines and dashes

  Commas are decoded from tabs
  """
  #assert isinstance(s, str)
  assert isinstance(s, basestring)
  s = s.replace('\t', ',')
  s = s.replace('\\,', ',')
  s = s.replace('\\n', '\n')
  s = s.replace('\\\\', '\\')

  return s

