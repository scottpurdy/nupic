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
 * PathTest
 */

#ifndef NTA_PATH_TEST_HPP
#define NTA_PATH_TEST_HPP

//----------------------------------------------------------------------

#include <nta/test/Tester.hpp>

//----------------------------------------------------------------------

namespace nta {

  struct PathTest : public Tester
  {
    virtual ~PathTest() {}
    virtual void RunTests();
  };
}

#endif // NTA_PATH_TEST_HPP
