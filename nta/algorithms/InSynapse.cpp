/* ---------------------------------------------------------------------
 *  Copyright (C) 2009-2011 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
 */

#include <iomanip>
#include <nta/algorithms/InSynapse.hpp>

using namespace nta::algorithms::Cells4;

inline void InSynapse::print(std::ostream& outStream) const
{
  outStream << _srcCellIdx << ',' << std::setprecision(4) << _permanence;
}

//--------------------------------------------------------------------------------

namespace nta {
  namespace algorithms {
    namespace Cells4 {

      std::ostream& operator<<(std::ostream& outStream, const InSynapse& s)
      {
        s.print(outStream);
        return outStream;
      }
    }
  }
}
