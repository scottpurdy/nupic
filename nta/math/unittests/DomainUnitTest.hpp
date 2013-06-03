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
 * Declaration of class DomainUnitTest
 */

//----------------------------------------------------------------------

#include <nta/test/Tester.hpp>
#include <nta/math/Domain.hpp>

//----------------------------------------------------------------------

#ifndef NTA_DOMAIN_UNIT_TEST_HPP
#define NTA_DOMAIN_UNIT_TEST_HPP

namespace nta {

  //----------------------------------------------------------------------
  class DomainUnitTest : public Tester
  {
  public:
    DomainUnitTest() {}
    virtual ~DomainUnitTest() {}

    // Run all appropriate tests
    virtual void RunTests();

  private:

    // Default copy ctor and assignment operator forbidden by default
    DomainUnitTest(const DomainUnitTest&);
    DomainUnitTest& operator=(const DomainUnitTest&);

  }; // end class DomainUnitTest
    
  //----------------------------------------------------------------------
} // end namespace nta

#endif // NTA_DOMAIN_UNIT_TEST_HPP



