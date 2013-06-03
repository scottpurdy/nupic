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
 * Watcher unit tests
 */

#ifndef NTA_WATCHER_TEST_HPP
#define NTA_WATCHER_TEST_HPP

#include <nta/test/Tester.hpp>

namespace nta
{
  struct WatcherTest : public Tester
  {
    virtual void RunTests();
  };
}

#endif // NTA_WATCHER_TEST_HPP
