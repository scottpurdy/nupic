# ----------------------------------------------------------------------
#  Copyright (C) 2010 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

from enthought.traits.api import *

import nupic
from nupic.analysis.inspectors.region.RegionInspector import RegionInspector
from nupic.analysis.inspectors.region.tabs import *

def _getSpecParameters(region):
  return region.spec.parameters

def _getSpatialParameters(region):
  return region.getSelf()._spatialSpec

def _getTemporalParameters(region):
  return region.getSelf()._temporalSpec

def _getOtherParameters(region):
  return region.getSelf()._otherSpec

def _getDescription(spec):
  return spec.description

class _SpatialTab(ParametersTab):

  title = 'Spatial'

  @staticmethod
  def isRegionSupported(region):
    """Return True if the tab is appropriate for this region, False otherwise."""

    return not region.getParameter('disableSpatial')

  def __init__(self, region):
    parameters = _getSpatialParameters(region).keys()
    parameters.remove('disableSpatial')

    # We can show this if needed, it's not very useful...
    parameters.remove('sparseCoincidenceMatrix')

    self.allowedParameters = parameters
    ParametersTab.__init__(self, region)

  def _addTraits(self):
    ParametersTab._addTraits(self)

    # The spOverlapDistribution is a multiple value parameter, and by default
    #  these are not presented by the inspector
    #parameters = getSpec(self.region)['parameters']
    parameters = _getSpecParameters(self.region)
    name = 'spOverlapDistribution'
    spec = parameters[name]
    desc = _getDescription(spec)
    self.add_trait(name, List(name=name, desc=desc))
    self.parameters[name] = spec

class _TemporalTab(ParametersTab):

  title = 'Temporal'

  @staticmethod
  def isRegionSupported(region):
    """Return True if the tab is appropriate for this region, False otherwise."""

    return not region.getParameter('disableTemporal')

  def __init__(self, region):
    parameters = _getTemporalParameters(region).keys()
    parameters.remove('disableTemporal')
    self.allowedParameters = parameters
    ParametersTab.__init__(self, region)


class _OtherTab(ParametersTab):

  title = 'Other'

  def __init__(self, region):
    parameters = _getOtherParameters(region).keys()

    parameters += ['breakPdb']
    self.allowedParameters = parameters
    ParametersTab.__init__(self, region)

class CLARegionSimpleInspector(RegionInspector):
  def __init__(self, parent, region, tabChangeCallback=None):
    tabs = defaultTabs[:]
    index = tabs.index(ParametersTab)
    tabs[index] = _OtherTab
    tabs.insert(index, _TemporalTab)
    tabs.insert(index, _SpatialTab)
    RegionInspector.__init__(self, parent, region, tabChangeCallback, tabs)