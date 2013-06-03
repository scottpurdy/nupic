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
 * ArrayBase unit tests
 */

#ifndef NTA_ARRAY_TEST_HPP
#define NTA_ARRAY_TEST_HPP

#include <nta/test/Tester.hpp>

#include <map>

namespace nta
{
  struct ArrayTestParameters
  {
    NTA_BasicType dataType;
    unsigned int dataTypeSize;
    int allocationSize; //We intentionally use an int instead of a size_t for
                        //these tests.  This is so that we can check test usage
                        //by a naive user who might use an int and accidentally
                        //pass negative values.
    std::string dataTypeText;
    bool testUsesInvalidParameters;
    
    ArrayTestParameters() :
      dataType((NTA_BasicType) -1),
      dataTypeSize(0),
      allocationSize(0),
      dataTypeText(""),
      testUsesInvalidParameters(true) {}
      
    ArrayTestParameters(NTA_BasicType dataTypeParam,
                        unsigned int dataTypeSizeParam,
                        int allocationSizeParam,
                        std::string dataTypeTextParam,
                        bool testUsesInvalidParametersParam) :
      dataType(dataTypeParam),
      dataTypeSize(dataTypeSizeParam),
      allocationSize(allocationSizeParam),
      dataTypeText(dataTypeTextParam),
      testUsesInvalidParameters(testUsesInvalidParametersParam) { }
  };

  struct ArrayTest : public Tester
  {
    virtual ~ArrayTest() {}
    virtual void RunTests();
        
private:
    std::map<std::string,ArrayTestParameters> testCases_;

    typedef std::map<std::string,ArrayTestParameters>::iterator
      TestCaseIterator;
    
#ifdef NTA_INSTRUMENTED_MEMORY_GUARDED
    void testMemoryOperations();
#endif

    void testArrayCreation();
    void testBufferAllocation();
    void testBufferAssignment();
    void testBufferRelease();
    void testArrayTyping();
  };
}

#endif // NTA_ARRAY_TEST_HPP
