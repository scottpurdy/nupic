# ----------------------------------------------------------------------
#  Copyright (C) 2006-2008 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

from nupic.regions.ImageSensorExplorers.BaseExplorer import BaseExplorer
from nupic.regions.ImageSensorExplorers.SpiralSweep import SpiralSweep

class PatrolSweep(SpiralSweep):

  """
  This explorer generates multiple presentations for each image in a patrol-like
  path around the original image. For example, if the patrol radius is 2 then
  instead of the image being centered at (0,0) multiple presentations will be
  generated at the following offsets :


  (-2, -2) (-2, 0) (-2, 2)

  (-2, 0)    I     (2, 0)

  (-2, 2)  (0, 2)  (2, 2)


  PatrolSweep sub-classes SpiralSweep, which is provides general-purpose logic
  for explorers that generate multiple translated presentations of each image.
  It overrides the __init__ method where it generates the particular "patrol"
  list of offsets (where SpiralSweep generates a spiral-like list of offsets)
  """

  def __init__(self, radius=1, *args, **kwargs):
    """
    radius - the radius of the Patrol sweep
    """

    assert(radius >= 1)
    SpiralSweep.__init__(self, radius, *args, **kwargs)
    r = radius
    self.offsets = [(r, 0),  (r, r),   (0, r),  (-r, r),
                    (-r, 0), (-r, -r), (0, -r), (r, -r)]
    self.index = 0