/*
 * ----------------------------------------------------------------------
 *  Copyright (C) 2010 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
 */


#include <nta/engine/LinkPolicy.hpp>
#include <nta/engine/LinkPolicyFactory.hpp>
#include <nta/engine/TestFanIn2LinkPolicy.hpp>
#include <nta/engine/UniformLinkPolicy.hpp>
#include <nta/utils/Log.hpp>

namespace nta
{


LinkPolicy* LinkPolicyFactory::createLinkPolicy(const std::string policyType, 
                                             const std::string policyParams,
                                             Link* link)
{
  LinkPolicy *lp = NULL;
  if (policyType == "TestFanIn2")
  {
    lp = new TestFanIn2LinkPolicy(policyParams, link);
  } else if (policyType == "UniformLink")
  {
    lp = new UniformLinkPolicy(policyParams, link);
  } else if (policyType == "UnitTestLink")
  {
    // When unit testing a link policy, a valid Link* is required to be passed
    // to the link policy's constructor.  If you pass NULL, other portions of
    // NuPIC may try to dereference it (e.g. operator<< from NTA_THROW).  So we
    // allow for a UnitTestLink link policy which doesn't actually provide
    // anything.  This way, you can create a dummy link like so:
    //
    // Link dummyLink("UnitTestLink", "", "", "");
    //
    // and pass this dummy link to the constructor of the real link policy
    // you wish to unit test.
  } else if (policyType == "TestSplit")
  {
    NTA_THROW << "TestSplit not implemented yet";
  } else if (policyType == "TestOneToOne")
  {
    NTA_THROW << "TestOneToOne not implemented yet";
  } else {
    NTA_THROW << "Unknown link policy '" << policyType << "'";
  }
  return lp;
}



}

