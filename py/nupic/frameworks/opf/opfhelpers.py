# ----------------------------------------------------------------------
#  Copyright (C) 2011, 2012 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

# This file contains utility functions that are may be imported
# by clients of the framework. Functions that are used only by
# the prediction framework should be in opfutils.py
#
# TODO: Rename as helpers.py once we're ready to replace the legacy
#       helpers.py

import imp
import os

import expdescriptionapi
import opfutils


def loadExperiment(path):
  """Loads the experiment description file from the path.

  Args:
    path: The path to a directory containing a description.py file or the file
        itself.
  Returns:
    (config, control)
  """
  if not os.path.isdir(path):
    path = os.path.dirname(path)
  descriptionPyModule = loadExperimentDescriptionScriptFromDir(path)
  expIface = getExperimentDescriptionInterfaceFromModule(descriptionPyModule)
  return expIface.getModelDescription(), expIface.getModelControl()


def loadExperimentDescriptionScriptFromDir(experimentDir):
  """ Loads the experiment description python script from the given experiment
  directory.

  experimentDir:  experiment directory path

  Returns:        modudle of the loaded experiment description scripts
  """
  descriptionScriptPath = os.path.join(experimentDir, "description.py")
  module = _loadDescriptionFile(descriptionScriptPath)
  return module


def getExperimentDescriptionInterfaceFromModule(module):
  """
  module:     imported description.py module

  Returns:        An expdescriptionapi.DescriptionIface-based instance that
                  represents the experiment description
  """
  result = module.descriptionInterface
  assert isinstance(result, expdescriptionapi.DescriptionIface), \
         "expected DescriptionIface-based instance, but got %s" % type(result)

  return result


g_descriptionImportCount = 0

def _loadDescriptionFile(descriptionPyPath):
  """Loads a description file and returns it as a module.

  descriptionPyPath: path of description.py file to load
  """
  global g_descriptionImportCount

  if not os.path.isfile(descriptionPyPath):
    raise RuntimeError(("Experiment description file %s does not exist or " + \
                        "is not a file") % (descriptionPyPath,))

  mod = imp.load_source("pf_description%d" % g_descriptionImportCount,
                        descriptionPyPath)
  g_descriptionImportCount += 1

  if not hasattr(mod, "descriptionInterface"):
    raise RuntimeError("Experiment description file %s does not define %s" % \
                       (descriptionPyPath, "descriptionInterface"))

  if not isinstance(mod.descriptionInterface, expdescriptionapi.DescriptionIface):
    raise RuntimeError(("Experiment description file %s defines %s but it " + \
                        "is not DescriptionIface-based") % \
                            (descriptionPyPath, name))

  return mod
