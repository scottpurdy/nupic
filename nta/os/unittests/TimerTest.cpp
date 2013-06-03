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


#include "TimerTest.hpp"
#include <nta/utils/Log.hpp>
#include <nta/os/Timer.hpp>
#include <math.h> // fabs



using namespace nta;

static void spinABit()
{
  // Use up some time. We don't know how much, but it should be 
  // measurable as > 0; structured so that the compiler 
  // won't optimize away the loop
  int j = 0;
  int k = 1;
  for (int i = 0; i < 100000; i ++)
  {
    j += i;
    k += 1;
    j -= k;
  }
  NTA_DEBUG << "Timer test: j = " << j;
}

void TimerTest::RunTests() 
{
// Tests are minimal because we have no way to run performance-sensitive tests in a controlled
// environment.

  Timer t1;
  Timer t2(/* startme= */ true);

  TEST(!t1.isStarted());
  TEST(t1.getElapsed() == 0.0);
  TEST(t1.getStartCount() == 0);
  TESTEQUAL("[Elapsed: 0 Starts: 0]", t1.toString());
  
  spinABit();


  TEST(t2.isStarted());
  TEST(t2.getStartCount() == 1);
  TEST(t2.getElapsed() > 0);
  Real64 t2elapsed = t2.getElapsed();

  t1.start();

  spinABit();
  t1.stop();
  t2.stop();
  TEST(t1.getStartCount() == 1);
  TEST(t1.getElapsed() > 0);
  TEST(t2.getElapsed() > t2elapsed);
  TEST(t2.getElapsed() > t1.getElapsed());

  t1.start();
  t1.stop();
  TEST(t1.getStartCount() == 2);

}




