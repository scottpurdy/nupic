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

/**
 * @file
 */


#ifndef NTA_RANDOM_TEST_HPP
#define NTA_RANDOM_TEST_HPP

#include <nta/utils/Random.hpp>
#include <nta/test/Tester.hpp>

namespace nta {
  
  class RandomTest : public Tester {
public:
    RandomTest();
    virtual ~RandomTest();
    
    virtual void RunTests();
  };
} // namespace nta


#endif // NTA_RANDOM_TEST_HPP
