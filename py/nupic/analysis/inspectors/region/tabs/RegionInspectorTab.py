# ----------------------------------------------------------------------
#  Copyright (C) 2006-2008 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

from enthought.traits.api import HasTraits, Str
from enthought.traits.ui.api import Handler
import numpy
import nupic

class RegionInspectorTab(HasTraits):

  """
  RegionInspectorTab is the base class for tabs which are used by RegionInspector.

  Each tab is HasTraits object and can implement isRegionSupported(), __init__(),
  update(), switchRegion(), and handleKeyEvent(). RegionInspector, which contains
  the tabs, is a RuntimeListener and is called whenever the network changes.
  It calls update() on the active tab. It also calls update() on the tab after
  __init__(), so that the tab can get any data it needs in order to set up its
  initial display. It calls switchRegion() when changing to a different baby
  region within a multiregion, or a different region within a region.

  RegionInspector gets a callback when the user switches tabs, so it knows which
  tab is active. It automatically calls update() with no arguments when
  switching to a tab if any changes to the network have occurred since that
  tab was last visible. It also only calls switchRegion() on the active tab, but
  calls switchRegion() when switching to a tab if the region has changed since the
  tab was last visible.

  In the creation of the view, the handler is automatically set to
  RegionInspectorTabHandler, and the buttons are automatically set to NoButtons.
  """

  @staticmethod
  def isRegionSupported(region):
    """Return True if the tab is appropriate for this region, False otherwise."""

    return True

  # Parameters
  plotSize = (430, 150)  # (width, height) of matplotlib plots
  toolbarSize = 35  # Shorter dimension of matplotlib toolbar

  # Traits
  spacer = Str

  def __init__(self, region):

    self.region = region

  def __setattr__(self, name, value):
    """Only update traits when their value changes."""

    #if name == 'coincImages':
    #  from dbgp.client import brk; brk(port=9011)
    if hasattr(self, name):
      currentValue = getattr(self, name)
      if isinstance(currentValue, numpy.ndarray):
        if numpy.alltrue(currentValue == value):
          return
      else:
        try:
          if type(currentValue) == type(value) and currentValue == value:
            return
        except ValueError:  # Can occur with numpy array inside a collection
          pass


    HasTraits.__setattr__(self, name, value)

  def update(self, methodName=None, elementName=None, args=None, kwargs=None):
    """
    Passed through by RegionInspector only if this tab is visible.

    Extra arguments (optional) are passed by the wrapped methods,
    and they can be used to avoid unnecessary updating.

    @param methodName -- Class method that was called.
    @param elementName -- Name of RuntimeElement.
    @param args -- Positional arguments passed to the method.
    @param kwargs -- Keyword arguments passed to the method.
    """

    pass

  def switchRegion(self, region):
    """Switch to a different region within the same region or multiregion."""

    self.region = region
    # Some inspectors may wish to override this method to skip the update
    self.update()

  def setVisible(self, visible):
    """
    Called when this tab becomes visible or hidden in response to the user
    switching tabs.

    visible -- True if the tab is becoming visible, or False if it is becoming
      hidden.
    """

    pass

  def handleKeyEvent(self, evt):
    """
    Handle a key event.

    If an event is not handled, call the parent class to handle it.
    """

    evt.Skip()


class RegionInspectorTabHandler(Handler):
  #def __init__(self, *args, **kw):
  #  from dbgp.client import brk; brk(port=9011)
  #  Handler.__init__(self, *args, **kw)

  def setattr(self, info, object, name, value):
    """Send parameters and execute commands to the RuntimeRegion."""

    Handler.setattr(self, info, object, name, value)
    if info.ui.history:
      # Clear automatic undo history
      info.ui.history.clear()
    if type(value) is unicode:
      value = str(value)

    ns = object.region.spec
    if name in ns.parameters and ns.parameters[name].accessMode == 'ReadWrite':
      # Settable parameter
      object.region.setParameter(name, value)
    elif name in ns.commands:
      object.region.executeCommand([name, str(value)])
    else:

      if hasattr(object.region.getSelf(), name):
        print 'Executing unknown command command:', name
        object.region.executeCommand([name, str(value)])