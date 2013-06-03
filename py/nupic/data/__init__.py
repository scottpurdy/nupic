# ----------------------------------------------------------------------
#  Copyright (C) 2010 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""A data source for the prediction framework has a getNext() method.
FileSource is a base class for file-based sources. There are two
 sub-classes:

TextFileSource - can read delimited text files (e.g. CSV files)
StandardSource - can read a binary file of marshaled Python objects
"""

SENTINEL_VALUE_FOR_MISSING_DATA = None

from functionsource import FunctionSource
