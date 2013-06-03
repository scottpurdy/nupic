# ----------------------------------------------------------------------
#  Copyright (C) 2006-2008 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""
## @file

nupic.math is a package containing modules related to mathematical, probabilistic
and statistical data structures and simple algorithms.

The primary sub-modules include (use help on these modules for additional
online documentation):

nupic.bindings.math
A module containing many low-level mathematical data structures and algorithms.
This module is a set of Python bindings for the Numenta C++ math libraries.
Because of this, some calling conventions may more closely reflect the underlying
C++ architecture than a typical Python module.
All classes, functions and constants of nupic.bindings.math are pre-imported
into nupic.math, and thus are accessible from nupic.math.
The module contains the following important and frequently used classes:
  SparseMatrix
  SparseTensor
  TensorIndex
  Domain

nupic.math.stats
Module of statistical data structures and functions used in learning algorithms
and for analysis of HTM network inputs and outputs.
"""

import sys
import math as coremath # The core Python module.

# bitstringToArray/CMultiArgMax are not part of NuPIC2
from nupic.bindings.math import (GetNTAReal,
                                 GetNumpyDataType,
                                 SparseMatrix,  SparseTensor,
                                 TensorIndex, Domain)
from nupic.bindings.math import lgamma, erf

def choose(n, c):
  return int(round(coremath.exp(logChoose(n, c))))

def logChoose(n, c):
  return lgamma(n+1) - lgamma(c+1) - lgamma(n-c+1)


# __all__ affects what symbols match "*"
# set __all__ so that "from math import *" doesn't clobber "sys"

__all__ = [
    "GetNTAReal", "GetNumpyDataType",
    "SparseMatrix", "SparseTensor", "TensorIndex", "Domain", "choose", "logChoose"]


__all__.extend(["CMultiArgMax", "bitstringToArray",
    "pickByDistribution", "ConditionalProbabilityTable2D", "MultiIndicator", "Indicator"])