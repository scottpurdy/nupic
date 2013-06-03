# ----------------------------------------------------------------------
#  Copyright (C) 2006-2008 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

from enthought.traits.api import *
from enthought.traits.ui.api import *

from nupic.analysis.inspectors.region.RegionInspector import RegionInspector
from nupic.analysis.inspectors.region.tabs import *
from nupic.ui.enthought import alignCenter


class _DataTab(RegionInspectorTab):

  # Traits
  outputFile = File(label='Output File')
  flushFile = Button(label='Flush File')
  closeFile = Button(label='Close File')

  def __init__(self, region):

    RegionInspectorTab.__init__(self, region)

    self.traits_view = View(
      Group(
        Item('outputFile', style='text'),
        alignCenter(
          Item('flushFile', show_label=False),
          Item('closeFile', show_label=False)
        )
      ),
      title='Data'
    )


class VectorFileEffectorInspector(RegionInspector):
  def __init__(self, parent, region, tabChangeCallback=None):
    tabs = [_DataTab, InputsTab, HelpTab]
    RegionInspector.__init__(self, parent, region, tabChangeCallback, tabs)