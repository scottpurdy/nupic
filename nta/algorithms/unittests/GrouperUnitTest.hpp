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
 * Notes
 */

//----------------------------------------------------------------------

#include <nta/test/Tester.hpp>
#include <nta/algorithms/Grouper.hpp>

//----------------------------------------------------------------------

#ifndef NTA_GROUPER_UNIT_TEST_HPP
#define NTA_GROUPER_UNIT_TEST_HPP

namespace nta {

  //----------------------------------------------------------------------
  class GrouperUnitTest : public Tester
  {
  public:
    GrouperUnitTest() {}
    virtual ~GrouperUnitTest() {}

    // Run all appropriate tests
    virtual void RunTests();

  private:
    //void doOneTestCase(const std::string& tcName, bool diagnose =false);
    //void testInference(Grouper& g, bool diagnose=false);
    //void testTBI(bool diagnose=false);
    //void testSaveReadState();

    // Default copy ctor and assignment operator forbidden by default
    GrouperUnitTest(const GrouperUnitTest&);
    GrouperUnitTest& operator=(const GrouperUnitTest&);

  }; // end class GrouperUnitTest
    
  //----------------------------------------------------------------------
} // end namespace nta

#endif // NTA_GROUPER_UNIT_TEST_HPP



