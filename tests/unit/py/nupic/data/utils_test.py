#!/usr/bin/env python
# ----------------------------------------------------------------------
# Copyright (C) 2012 Numenta Inc, All rights reserved,
#
# The information and source code contained herein is the
# exclusive property of Numenta Inc, No part of this software
# may be used, reproduced, stored or distributed in any form,
# without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""Unit tests for nupic.data.utils."""

from datetime import datetime

from nupic.data import utils
from nupic.support.unittesthelpers.testcasebase import (TestCaseBase,
                                                        unittest)


class UtilsTest(TestCaseBase):
  """Utility unit tests."""

  def testParseTimestamp(self):
    expectedResults = (
        ('2011-09-08 05:30:32:920000', datetime(2011, 9, 8, 5, 30, 32, 920000)),
        ('2011-09-08 05:30:32.920000', datetime(2011, 9, 8, 5, 30, 32, 920000)),
        ('2011-09-08 5:30:32:92', datetime(2011, 9, 8, 5, 30, 32, 920000)),
        ('2011-09-08 5:30:32', datetime(2011, 9, 8, 5, 30, 32)),
        ('2011-09-08 5:30', datetime(2011, 9, 8, 5, 30)),
        ('2011-09-08', datetime(2011, 9, 8)))
    for timestamp, dt in expectedResults:
      self.assertEqual(utils.parseTimestamp(timestamp), dt)

  def testSerializeTimestamp(self):
    self.assertEqual(
        utils.serializeTimestamp(datetime(2011, 9, 8, 5, 30, 32, 920000)),
        '2011-09-08 05:30:32.920000')

  def testSerializeTimestampNoMS(self):
    self.assertEqual(
        utils.serializeTimestampNoMS(datetime(2011, 9, 8, 5, 30, 32, 920000)),
        '2011-09-08 05:30:32')


if __name__ == '__main__':
  unittest.main()
