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


#ifndef NTA_ENV_TEST_HPP
#define NTA_ENV_TEST_HPP

#include <nta/os/Env.hpp>
#include <nta/test/Tester.hpp>

namespace nta {
  
  class EnvTest : public Tester {
public:
    EnvTest();
    virtual ~EnvTest();
    
    virtual void RunTests();
  };
} // namespace nta


#endif // NTA_ENV_TEST_HPP
