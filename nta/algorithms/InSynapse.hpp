/* ---------------------------------------------------------------------
 *  Copyright (C) 2009-2011 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
 */

#ifndef NTA_INSYNAPSE_HPP
#define NTA_INSYNAPSE_HPP

#include <nta/types/types.hpp>

#include <ostream>
#include <fstream>

using namespace nta;

//--------------------------------------------------------------------------------

namespace nta {
  namespace algorithms {
    namespace Cells4 {


      //--------------------------------------------------------------------------------
      //--------------------------------------------------------------------------------
      /**
       * The type of synapse contained in a Segment. It has the source cell index
       * of the synapse, and a permanence value. The source cell index is between
       * 0 and nCols * nCellsPerCol.
       */
      class InSynapse
      {
      private:
        UInt _srcCellIdx;
        Real _permanence;

      public:
        inline InSynapse()
          : _srcCellIdx((UInt) -1),
            _permanence(0)
        {}

        inline InSynapse(UInt srcCellIdx, Real permanence)
          : _srcCellIdx(srcCellIdx),
            _permanence(permanence)
        {}

        inline InSynapse(const InSynapse& o)
          : _srcCellIdx(o._srcCellIdx),
            _permanence(o._permanence)
        {}

        inline InSynapse& operator=(const InSynapse& o)
        {
          _srcCellIdx = o._srcCellIdx;
          _permanence = o._permanence;
          return *this;
        }

        inline UInt srcCellIdx() const { return _srcCellIdx; } const
        inline Real& permanence() const { return _permanence; }
        inline Real& permanence() { return _permanence; }

        inline void print(std::ostream& outStream) const;
      };

      //--------------------------------------------------------------------------------
#ifndef SWIG
      std::ostream& operator<<(std::ostream& outStream, const InSynapse& s);
#endif

      // end namespace
    }
  }
}

#endif // NTA_INSYNAPSE_HPP
