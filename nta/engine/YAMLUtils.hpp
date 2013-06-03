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
#ifndef NTA_YAML_HPP
#define NTA_YAML_HPP


#include <nta/types/types.hpp>
#include <nta/ntypes/Value.hpp>
#include <nta/ntypes/Collection.hpp>
#include <nta/engine/Spec.hpp>

namespace nta
{

  namespace YAMLUtils
  {
    /* 
     * For converting default values
     */
    Value toValue(const std::string& yamlstring, NTA_BasicType dataType);

    /* 
     * For converting param specs for Regions and LinkPolicies
     */
    ValueMap toValueMap(
      const char* yamlstring, 
      Collection<ParameterSpec>& parameters,
      const std::string & nodeType = "",
      const std::string & regionName = ""
      );


  } // namespace YAMLUtils
} // namespace nta

#endif //  NTA_YAML_HPP

