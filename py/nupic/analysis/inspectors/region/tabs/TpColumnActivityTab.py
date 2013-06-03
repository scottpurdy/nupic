# ----------------------------------------------------------------------
#  Copyright (C) 2006-2010 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

# Python imports...

# Local imports...
from ColumnActivityTab import ColumnActivityTab
from ColumnActivityTab import kShowTpColumns

################################################################################
class TpColumnActivityTab(ColumnActivityTab):
  """ColumnActivityTab subclass showing TP outputs."""

  ####################################################################
  @staticmethod
  def isRegionSupported(region):
    """Return True if the tab is appropriate for this region, False otherwise.

    @return isRegionSupported  True if this is a supported region.
    """
    return 'CLARegion' in region.type and (not region.getParameter('disableTemporal'))

  ####################################################################
  def __init__(self, region):
    """TpColumnActivityTab constructor.

    @param  region  The RuntimeRegion.
    """
    # Call superclass.  This will init, among other things, self.region...
    super(TpColumnActivityTab, self).__init__(region, kShowTpColumns)