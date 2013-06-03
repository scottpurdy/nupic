/* ---------------------------------------------------------------------
 *  Copyright (C) 2009-2011 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
 */


#include <nta/algorithms/OutSynapse.hpp>
#include <nta/algorithms/Cells4.hpp>
using namespace nta::algorithms::Cells4;
using namespace nta;

bool OutSynapse::invariants(Cells4* cells) const
{
  bool ok = true;
  if (cells) {
    ok &= _dstCellIdx < cells->nCells();
    ok &= _dstSegIdx < cells->__nSegmentsOnCell(_dstCellIdx);
  }
  return ok;
}

namespace nta {
  namespace algorithms {
    namespace Cells4 {
      bool operator==(const OutSynapse& a, const OutSynapse& b)
      {
        return a.equals(b);
      }
    }
  }
}
