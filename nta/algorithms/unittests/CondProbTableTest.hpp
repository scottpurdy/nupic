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

//----------------------------------------------------------------------

#ifndef NTA_COND_PROB_TABLE_TEST_HPP
#define NTA_COND_PROB_TABLE_TEST_HPP

namespace nta {
  class CondProbTable;

  //----------------------------------------------------------------------
  class CondProbTableTest : public Tester
  {
  public:
    CondProbTableTest();
    virtual ~CondProbTableTest();

    // Run all appropriate tests
    virtual void RunTests();

  private:
    // Compare 2 vectors using printed output, this works even for round-off errors
    void testVectors(const std::string& testName, const std::vector<Real>& v1,
                const std::vector<Real>& v2);
                
    // Run tests on the given table
    void testTable (const std::string& testName, CondProbTable& table, 
      const std::vector<std::vector<Real> > & rows);
    
    // Size of the table we construct
    Size numRows() {return 4;}
    Size numCols() {return 3;}
  
    // Default copy ctor and assignment operator forbidden by default
    CondProbTableTest(const CondProbTableTest&);
    CondProbTableTest& operator=(const CondProbTableTest&);

  }; // end class OnlineKMeansCDTest
    
  //----------------------------------------------------------------------
} // end namespace nta

#endif // NTA_COND_PROB_TABLE_TEST_HPP



