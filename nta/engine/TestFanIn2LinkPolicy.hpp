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


#ifndef NTA_TESTFANIN2LINKPOLICY_HPP
#define NTA_TESTFANIN2LINKPOLICY_HPP

#include <string>
#include <nta/engine/Link.hpp>
#include <nta/ntypes/Dimensions.hpp>

namespace nta
{

  class Link;

  class TestFanIn2LinkPolicy : public LinkPolicy
  {
  public:
    TestFanIn2LinkPolicy(const std::string params, Link* link);

    ~TestFanIn2LinkPolicy();

    void setSrcDimensions(Dimensions& dims);

    void setDestDimensions(Dimensions& dims);
  
    const Dimensions& getSrcDimensions() const;

    const Dimensions& getDestDimensions() const;

    void buildProtoSplitterMap(Input::SplitterMap& splitter) const;

    void setNodeOutputElementCount(size_t elementCount);

    void initialize();

    bool isInitialized() const;

private:
    Link* link_;
    
    Dimensions srcDimensions_;
    Dimensions destDimensions_;

    size_t elementCount_;

    bool initialized_;


  }; // TestFanIn2

} // namespace nta


#endif // NTA_TESTFANIN2LINKPOLICY_HPP
