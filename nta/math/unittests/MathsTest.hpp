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
 * Declarations for maths unit tests
 */

//----------------------------------------------------------------------

#include <nta/test/Tester.hpp>
//#include <nta/foundation/TRandom.hpp>

//----------------------------------------------------------------------

#ifndef NTA_MATHS_TEST_HPP
#define NTA_MATHS_TEST_HPP

namespace nta {

  //----------------------------------------------------------------------
  class MathsTest : public Tester
  {
  public:
    MathsTest() {
      //rng_ = new TRandom("maths_test");
    }
    virtual ~MathsTest() {
      //delete rng_;
    }

    // Run all appropriate tests
    virtual void RunTests();

  private:
    //void unitTestNearlyZero();
    //void unitTestNearlyEqual();
    //void unitTestNearlyEqualVector();
    //void unitTestNormalize();
    //void unitTestVectorToStream();
    //void unitTestElemOps();
    //void unitTestWinnerTakesAll();
    //void unitTestScale();
    //void unitTestQSI();
    //
    //// Use our own random number generator for reproducibility
    //TRandom *rng_;
		
    // Default copy ctor and assignment operator forbidden by default
    MathsTest(const MathsTest&);
    MathsTest& operator=(const MathsTest&);

  }; // end class MathsTest
    
  //----------------------------------------------------------------------
} // end namespace nta

#endif // NTA_MATHS_TEST_HPP



