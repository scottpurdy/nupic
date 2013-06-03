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
 * DirectoryTest
 */

#ifndef NTA_REGEX_TEST_HPP
#define NTA_REGEX_TEST_HPP

//----------------------------------------------------------------------

#include <nta/test/Tester.hpp>

//----------------------------------------------------------------------

namespace nta 
{

  struct regexTest : public Tester
  {
    virtual ~regexTest() {}
    virtual void RunTests();
  };
}

#endif // NTA_REGEX_TEST_HPP
