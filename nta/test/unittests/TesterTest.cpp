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

#include <iostream>
#include <stdexcept>
#include <nta/test/Tester.hpp>
#include "TesterTest.hpp"

namespace nta {

template <class T> const T& Max( const T& t1, const T& t2) { return (t1 > t2) ? t1 : t2; }
template <class T> const T& Min( const T& t1, const T& t2) { return (t1 < t2) ? t1 : t2; }
    
TesterTest::TesterTest()
{
}

TesterTest::~TesterTest()
{
}

// Run all appropriate tests
void TesterTest::RunTests()
{
  TESTEQUAL2("Integer test, should succeed",1,1);
  TESTEQUAL2("Double test, should succeed",23.42,23.42);
  TESTEQUAL2("String test, should succeed","Numenta","Numenta");
  
  // These are probably the only tests in our test suite that should fail!
  TESTEQUAL2("Integer test, should fail",1,0);
  TESTEQUAL2("Double test, should fail",23.42,23.421);
  TESTEQUAL2("String test, should fail","Numenta","Numenta ");
  
  // Test functions in Common
  TESTEQUAL2("Max test", 23.3, Max(23.2, 23.3));
  TESTEQUAL2("Min test", 23.2, Min(23.2, 23.3));
  TESTEQUAL2("Max test", 'b', Max('a', 'b'));
  TESTEQUAL2("Min test", 'a', Min('a', 'b'));
  
  // Now throw an exception to see if we catch it
  throw std::runtime_error("This exception should get caught.");
}

} // end namespace nta

