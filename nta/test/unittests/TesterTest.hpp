/**
* ----------------------------------------------------------------------
 *  Copyright (C) 2006,2007 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 *
 * ----------------------------------------------------------------------
 */

/** @file 
Unit tester tester.
*/

#ifndef _H_TESTER_TEST_H
#define _H_TESTER_TEST_H

#include <nta/test/Tester.hpp>

namespace nta {
	
  /** Tests the unit tester interface.
   *
   */
  class TesterTest : public Tester  {
		
  public:
    // Constructors and destructors
    TesterTest();
    virtual ~TesterTest();
		
    // Run all appropriate tests
    virtual void RunTests();
		
  };
	
} // end namespace nta

#endif // __TesterTest_hpp__
