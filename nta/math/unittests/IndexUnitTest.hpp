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
 * Declaration of class IndexUnitTest
 */

//----------------------------------------------------------------------

#include <nta/test/Tester.hpp>
#include <nta/math/Index.hpp>

//----------------------------------------------------------------------

#ifndef NTA_INDEX_UNIT_TEST_HPP
#define NTA_INDEX_UNIT_TEST_HPP

namespace nta {

  //----------------------------------------------------------------------
  class IndexUnitTest : public Tester
  {
  public:
    IndexUnitTest() {}
    virtual ~IndexUnitTest() {}

    // Run all appropriate tests
    virtual void RunTests();

  private:
    typedef Index<UInt, 1> I1;
    typedef Index<UInt, 2> I2;
    typedef Index<UInt, 3> I3;
    typedef Index<UInt, 4> I4;
    typedef Index<UInt, 5> I5;
    typedef Index<UInt, 6> I6;

    //void unitTestFixedIndex();
    //void unitTestDynamicIndex();

    // Default copy ctor and assignment operator forbidden by default
    IndexUnitTest(const IndexUnitTest&);
    IndexUnitTest& operator=(const IndexUnitTest&);

  }; // end class IndexUnitTest
    
  //----------------------------------------------------------------------
} // end namespace nta

#endif // NTA_INDEX_UNIT_TEST_HPP



