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
 * Collection unit tests
 */

#ifndef NTA_COLLECTION_TEST_HPP
#define NTA_COLLECTION_TEST_HPP

#include <nta/test/Tester.hpp>

namespace nta
{
  struct CollectionTest : public Tester
  {
    void testEmptyCollection();
    void testCollectionWith_1_Item();
    void testCollectionWith_2_Items();
    void testCollectionWith_137_Items();
    void testCollectionAddRemove();

    virtual void RunTests();        
  };
}

#endif // NTA_COLLECTION_TEST_HPP


