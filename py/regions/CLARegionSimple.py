# ----------------------------------------------------------------------
#  Copyright (C) 2010 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------


from nupic.regions.CLARegion import CLARegion, _getAdditionalSpecs

gDefaultTemporalImp = 'simple'

class CLARegionSimple(CLARegion):

  """
  Subclass of CLARegion that uses the simple TP
  """

  #############################################################################
  def __init__(self,
                temporalImp='simple',
               **kwargs):

    # Call parent
    CLARegion.__init__(self, temporalImp=temporalImp, **kwargs)


  #############################################################################
  @classmethod
  def getSpec(cls):
    """Return the Spec for CLARegion.

    The parameters collection is constructed based on the parameters specified
    by the variosu components (spatialSpec, temporalSpec and otherSpec)
    """

    spec = cls.getBaseSpec()
    s, t, o = _getAdditionalSpecs(temporalImp=gDefaultTemporalImp)
    spec['parameters'].update(s)
    spec['parameters'].update(t)
    spec['parameters'].update(o)

    #from dbgp.client import brk; brk(port=9011)
    return spec