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

/** @file
 * Declarations for Buffer unit tests
 */

#ifndef NTA_BUFFER_TEST_HPP
#define NTA_BUFFER_TEST_HPP

//----------------------------------------------------------------------

#include <nta/test/Tester.hpp>

//----------------------------------------------------------------------

#include <nta/types/types.hpp>
namespace nta 
{
  //----------------------------------------------------------------------
  class BufferTest : public Tester
  {
  
  public:
     BufferTest() {}
    
    // Run all appropriate tests
    virtual void RunTests();

  private:
    // Default copy ctor and assignment operator forbidden by default
    BufferTest(const BufferTest&);
    BufferTest& operator=(const BufferTest&);
    
    void testReadBytes_SmallBuffer();
    void testReadBytes_VariableSizeBuffer(Size buffSize);
    void testWriteBytes();
    void testComplicatedSerialization();
    void testEvenMoreComplicatedSerialization();
    void testArrayMethods();

  }; // end class BufferTest
    
    //----------------------------------------------------------------------
} // end namespace nta

#endif // NTA_BUFFER_TEST_HPP
