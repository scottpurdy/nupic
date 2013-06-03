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

from nupic.analysis.inspectors.region.tabs import RegionInspectorTab

class HelpTab(RegionInspectorTab):

  """
  Displays the RegionHelp text.
  """

  regionHelp = Str

  def __init__(self, region):

    RegionInspectorTab.__init__(self, region)

    #self.regionHelp = getRegionHelp(region)
    self.regionHelp = str(region.spec)
    self.traits_view = View(
      Item('regionHelp', style='custom', show_label=False),
      title='Help'
    )