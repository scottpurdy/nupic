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
 * Definitions for TAMUnitTest
 */

//----------------------------------------------------------------------

#include <nta/math/unittests/SparseMatrixUnitTest.hpp>

//----------------------------------------------------------------------

#ifndef NTA_TAM_UNIT_TEST_HPP
#define NTA_TAM_UNIT_TEST_HPP

namespace nta {

  //----------------------------------------------------------------------
  class TAMUnitTest : public SparseMatrixUnitTest
  {
  public:
    TAMUnitTest() 
      : SparseMatrixUnitTest()
    {}

    virtual ~TAMUnitTest()
    {}

    // Run all appropriate tests
    virtual void RunTests();

  private:
    // Default copy ctor and assignment operator forbidden by default
    TAMUnitTest(const TAMUnitTest&);
    TAMUnitTest& operator=(const TAMUnitTest&);

  }; // end class TAMUnitTest
    
  //----------------------------------------------------------------------
} // end namespace nta

#endif // NTA_TAM_UNIT_TEST_HPP



