/**
 * ----------------------------------------------------------------------
 *  Copyright (C) 2006,2007 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
*/

/** @file
 * Definitions for NearestNeighborUnitTest
 */

//----------------------------------------------------------------------

#include <nta/math/unittests/SparseMatrixUnitTest.hpp>

//----------------------------------------------------------------------

#ifndef NTA_NEAREST_NEIGHBOR
#define NTA_NEAREST_NEIGHBOR

namespace nta {

  //----------------------------------------------------------------------
  class NearestNeighborUnitTest : public SparseMatrixUnitTest
  {
  public:
    NearestNeighborUnitTest()
      : SparseMatrixUnitTest()
    {}

    virtual ~NearestNeighborUnitTest()
    {}
    
    // Run all appropriate tests
    virtual void RunTests();

  private:
    //void unit_test_rowLpDist();
    //void unit_test_LpDist();
    //void unit_test_LpNearest();
    //void unit_test_dotNearest();

    // Default copy ctor and assignment operator forbidden by default
    NearestNeighborUnitTest(const NearestNeighborUnitTest&);
    NearestNeighborUnitTest& operator=(const NearestNeighborUnitTest&);

  }; // end class NearestNeighborUnitTest
    
  //----------------------------------------------------------------------
} // end namespace nta

#endif // NTA_NEAREST_NEIGHBOR



