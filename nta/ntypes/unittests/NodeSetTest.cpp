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
 * Implementation of BasicType test
 */

#include "NodeSetTest.hpp"
#include <nta/ntypes/NodeSet.hpp>

using namespace nta;

void NodeSetTest::RunTests()
{
  NodeSet ns(4);
  
  TEST(ns.begin() == ns.end());
  ns.allOn();
  NodeSet::const_iterator i = ns.begin();
  TEST(*i == 0);
  ++i;
  TEST(*i == 1);
  ++i;
  TEST(*i == 2);
  ++i;
  TEST(*i == 3);
  ++i;
  TEST(i == ns.end());
  
  ns.allOff();
  TEST(ns.begin() == ns.end());
  
  ns.add(1);
  ns.add(3);
  i = ns.begin();
  TEST(*i == 1);
  ++i;
  TEST(*i == 3);
  ++i;
  TEST(i == ns.end());

  ns.add(4);
  i = ns.begin();
  TEST(*i == 1);
  ++i;
  TEST(*i == 3);
  ++i;
  TEST(*i == 4);
  ++i;
  TEST(i == ns.end());
  
  SHOULDFAIL(ns.add(5));
  
  ns.remove(3);
  i = ns.begin();
  TEST(*i == 1);
  ++i;
  TEST(*i == 4);
  ++i;
  TEST(i == ns.end());

  // this should have no effect since 3 has already been removed
  ns.remove(3);
  i = ns.begin();
  TEST(*i == 1);
  ++i;
  TEST(*i == 4);
  ++i;
  TEST(i == ns.end());

}
