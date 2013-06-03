/**
 * ----------------------------------------------------------------------
 * Copyright (C) 2012 Numenta Inc. All rights reserved.
 *
 * The information and source code contained herein is the
 * exclusive property of Numenta Inc. No part of this software
 * may be used, reproduced, stored or distributed in any form,
 * without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
*/

/** @file
 * Definitions for FastCLAClassifierTest
 *
 * The FastCLAClassifier class is primarily tested in the Python unit tests
 * but this file provides an easy way to check for memory leaks.
 */

#ifndef NTA_FAST_CLA_CLASSIFIER_TEST
#define NTA_FAST_CLA_CLASSIFIER_TEST

#include <nta/test/Tester.hpp>

namespace nta
{

  class FastCLAClassifierTest : public Tester
  {
  public:
    FastCLAClassifierTest() {}

    virtual ~FastCLAClassifierTest() {}

    // Run all appropriate tests.
    virtual void RunTests();

  private:
    void testBasic();

  }; // end class FastCLAClassifierTest

} // end namespace nta

#endif // NTA_FAST_CLA_CLASSIFIER_TEST
