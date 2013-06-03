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

#ifndef NTA_TIMER_TEST_HPP
#define NTA_TIMER_TEST_HPP

#include <nta/test/Tester.hpp>

/**
 * @todo This is the original Timer test before Timer and ProfilingTimer
 * were split. Need to split the unit test as well. 
 */
namespace nta {
  
  class TimerTest : public Tester {
public:
    TimerTest() {};
    virtual ~TimerTest() {};
    
    virtual void RunTests();
  };
} // namespace nta


#endif // NTA_TIMER_TEST_HPP
