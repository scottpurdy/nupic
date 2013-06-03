# ----------------------------------------------------------------------
#  Copyright (C) 2009 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

from nupic.analysis.inspectors.region.RegionInspector import RegionInspector
from nupic.analysis.inspectors.region.PictureSensorInspector import _MiniImagesTab

class MiniPictureSensorInspector(RegionInspector):
  def __init__(self, parent, region, tabChangeCallback=None):
    tabs = [_MiniImagesTab]
    RegionInspector.__init__(self, parent, region, tabChangeCallback, tabs)