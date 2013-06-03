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
 * Network unit tests
 */

#ifndef NTA_NETWORK_TEST_HPP
#define NTA_NETWORK_TEST_HPP

//----------------------------------------------------------------------

#include <nta/test/Tester.hpp>

//----------------------------------------------------------------------

namespace nta {

  struct NetworkTest : public Tester
  {
    virtual ~NetworkTest() {}
    virtual void RunTests();
    void test_nupic_auto_initialization();
    void test_region_access();
    void test_network_initialization();
    void test_network_modification();
    void test_phases();

  };
}

#endif // NTA_NETWORK_TEST_HPP
