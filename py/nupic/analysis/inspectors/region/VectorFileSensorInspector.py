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
from nupic.ui.enthought import alignCenter, FileOrDirectoryEditor

class _DataTab(ParametersTab):

  # Traits which aren't added by ParametersTab
  loadFile = File
  appendFile = File

  def _createView(self):
    """Set up the view for the traits."""

    self.traits_view = View(
      Group(
        Group(
          alignCenter(
            Item('loadFile', show_label=False,
              editor=FileOrDirectoryEditor(buttonLabel="Load file...")),
            Item('appendFile', show_label=False,
              editor=FileOrDirectoryEditor(buttonLabel="Append file..."))
          ),
          label='Data',
          show_border=True
        ),
        Group(
          Item('position'),
          Item('repeatCount'),
          Item('scalingMode'),
          Item('activeOutputCount', style='readonly'),
          Item('maxOutputVectorCount', style='readonly'),
          Item('vectorCount', style='readonly'),
          Item('recentFile', style='readonly'),
          label='Parameters',
          show_border=True
        )
      ),
      title='Data'
    )

class VectorFileSensorInspector(RegionInspector):
  def __init__(self, parent, region, tabChangeCallback=None):
    tabs = [_DataTab, OutputsTab, HelpTab]
    RegionInspector.__init__(self, parent, region, tabChangeCallback, tabs)