#! /usr/local/bin/python

# ----------------------------------------------------------------------
#  Copyright (C) 2006,2007 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""
## @file

This package contains modules for analyzing HTM networks
and their inputs and outputs.

Import packages, modules, functions and classes include:

"""
import nupic

__all__ = [
    "inferenceanalysis",
    "InferenceAnalysis",
    "ClassifyInference",
    "CompareClassifications",
    "ReadInference",
  ]

# The inspectors rely on wxPython and TraitsUI,
# which are not included on all platforms
try:
  import wx
  import enthought.traits
except ImportError:
  pass
else:
  from nupic.analysis._inspect import inspect, loadInspectors, saveInspectors