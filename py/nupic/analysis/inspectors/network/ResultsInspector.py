# ----------------------------------------------------------------------
#  Copyright (C) 2010 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

from enthought.traits.api import *
from enthought.traits.ui.api import *

from nupic.analysis.inspectors.network import NetworkInspector
from nupic.ui.enthought import InferenceResultsEditor

from nupic.engine import Network

def _getElements(net):
  return net.regions.values()

def _getElement(net, name):
  return net.regions[name]

def _hasParameter(region, name):
  return name in region.spec.parameters

def _getOutput(region, name):
  a = region.getOutputData(name)
  return [float(v) for v in a]

def _getSelf(region):
  return region.getSelf()

class ResultsInspector(NetworkInspector):

  """
  ResultsInspector shows the inference results of a RuntimeNetwork.
  """

  @staticmethod
  def isNetworkSupported(network):
    """
    Return True if the inspector is appropriate for this network. Otherwise,
    return a string specifying why the inspector is not supported.
    """

    if not isinstance(network, Network):
      return False

    for region in network.regions.values():
      if 'categoriesOut' in region.spec.outputs:
        return True

  @staticmethod
  def getNames():
    """
    Return the short and long names for this inspector. The short name appears
    in the dropdown menu, and the long name is used as the window title.
    """

    return ('results', 'Inference Results')

  # Traits
  inferenceResults = List

  def __init__(self, parent, network, numTopResults=5):
    NetworkInspector.__init__(self, parent, network)

    self.classifier = None

    # Find the classifier
    for element in _getElements(network):
      if 'categoriesOut' in element.spec.outputs:
        self.classifier = element
        break
    else:
      import warnings
      warnings.warn("No classifier found (no region with 'categoriesOut')",
          stacklevel=1)

    # Get the categoryInfo from the sensor
    sensor = _getElement(network, 'sensor')
    self.categoryInfo = _getSelf(sensor).getParameter('categoryInfo') \
        if _hasParameter(sensor, 'categoryInfo') else []

    # Truncate numTopResults based on number of categories
    numTopResults = min(numTopResults, len(self.categoryInfo))
    numTopResults = max(3, numTopResults)  # Absolute minimum
    self.numTopResults = numTopResults

    # Create the view
    self.traits_view = View(
      Item('inferenceResults', show_label=False,
        editor=InferenceResultsEditor(numTopResults=self.numTopResults))
    )

  def update(self, methodName=None, elementName=None, args=None, kwargs=None):
    """
    Called automatically in response to runtime engine activity.

    Extra arguments (optional) are passed by the wrapped methods,
    and they can be used to avoid unnecessary updating.

    @param methodName -- RuntimeElement class method that was called.
    @param elementName -- RuntimeElement name.
    @param args -- Positional arguments passed to the method.
    @param kwargs -- Keyword arguments passed to the method.
    """
    if methodName and methodName != 'run':
      return

    if self.classifier is None:
      return

    # Compile inference results
    inferenceResults = []
    values = _getOutput(self.classifier, 'categoriesOut')
    maxValue = max(values)
    for j in xrange(self.numTopResults):
      value = max(values)
      # Terminate early if there are no categories or results remaining
      if j == len(values) or maxValue <= 0 or value <= 0:
        break
      index = values.index(value)
      values[index] = -1
      if index < len(self.categoryInfo):
        (name, image) = self.categoryInfo[index]
      else:
        name = '%d' % index
        image = None

      inferenceResults.append({
        'barHeight': max(0, value / maxValue),
        'categoryName': name,
        'categoryImage': image
      })
    self.inferenceResults = inferenceResults