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

/** @file 
 * Definition of the LinkPolicyFactory API
 */

#ifndef NTA_LINKPOLICY_FACTORY_HPP
#define NTA_LINKPOLICY_FACTORY_HPP

#include <string>

namespace nta
{

  class LinkPolicy; 
  class Link;
  class Region;

  class LinkPolicyFactory
  {
  public:


    // LinkPolicyFactory is a lightweight object
    LinkPolicyFactory() {};
    ~LinkPolicyFactory() {};

    // Create a LinkPolicy of a specific type; caller gets ownership.
    LinkPolicy* createLinkPolicy(const std::string policyType, 
                               const std::string policyParams,
                               Link* link);

  private:

  };

} // namespace nta


#endif // NTA_LINKPOLICY_FACTORY_HPP
