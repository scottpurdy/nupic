# ----------------------------------------------------------------------
#  Copyright (C) 2010 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

from scalar import ScalarEncoder, testScalarEncoder
from adaptivescalar import AdaptiveScalarEncoder, testAdaptiveScalarEncoder
from date import DateEncoder, testDateEncoder
from log import LogEncoder, testLogEncoder
from category import CategoryEncoder, testCategoryEncoder
from sdrcategory import SDRCategoryEncoder, testSDRCategoryEncoder
from sdrrandom import SDRRandomEncoder, testSDRRandomEncoder
from nonuniformscalar import NonUniformScalarEncoder, testNonUniformScalarEncoder
from delta import DeltaEncoder,testDeltaEncoder
from scalarspace import ScalarSpaceEncoder,testScalarSpaceEncoder
# multiencoder must be imported last because it imports * from this module!
from multi import MultiEncoder, testMultiEncoder
from utils import bitsToString



if __name__ == "__main__":
  testScalarEncoder()
  testCategoryEncoder()
  testDateEncoder()
  testLogEncoder()
  testMultiEncoder()
  testSDRCategoryEncoder()
  testSDRRandomEncoder()
  testAdaptiveScalarEncoder()
  testDeltaEncoder()
  testScalarSpaceEncoder()