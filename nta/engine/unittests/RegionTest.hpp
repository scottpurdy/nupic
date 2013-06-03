/**
 * ----------------------------------------------------------------------
 *  Copyright (C) 2010 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
*/

/** @file
 * Region unit tests
 */

#ifndef NTA_REGION_TEST_HPP
#define NTA_REGION_TEST_HPP

//----------------------------------------------------------------------

#include <nta/test/Tester.hpp>

//----------------------------------------------------------------------

namespace nta {

  struct RegionTest : public Tester
  {
    virtual ~RegionTest() {}
    virtual void RunTests();
    void testWithNodeType(const std::string& nodeType);
  };
}

#endif // NTA_REGION_TEST_HPP
