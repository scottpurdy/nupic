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
 * Definitions for SpatialPoolerUnitTest
 */

//----------------------------------------------------------------------

#include <nta/test/Tester.hpp>
//#include <nta/foundation/TRandom.hpp>

//----------------------------------------------------------------------

#ifndef NTA_SPATIAL_POOLER_UNIT_TEST_HPP
#define NTA_SPATIAL_POOLER_UNIT_TEST_HPP

namespace nta {

  //----------------------------------------------------------------------
  class SpatialPoolerUnitTest : public Tester
  {
  public:
    SpatialPoolerUnitTest() {
      //rng_ = new TRandom("spatial_pooler_test");
    }
    virtual ~SpatialPoolerUnitTest() {
      //delete rng_;
    }

    // Run all appropriate tests
    virtual void RunTests();

  private:
    //void unitTestConstruction();
    //void unitTestDot();
    //void unitTestDotMaxD();
    //void unitTestProduct();
    //void unitTestProductMaxD();
    //void unitTestGaussian();                    
    //void unitTestPruning();
    //
    //// Use our own random number generator for reproducibility
    //TRandom *rng_;

    // Default copy ctor and assignment operator forbidden by default
    SpatialPoolerUnitTest(const SpatialPoolerUnitTest&);
    SpatialPoolerUnitTest& operator=(const SpatialPoolerUnitTest&);

  }; // end class SpatialPoolerUnitTest
    
  //----------------------------------------------------------------------
} // end namespace nta

#endif // NTA_SPATIAL_POOLER_UNIT_TEST_HPP



