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
 * Definition of the LinkPolicy class
 */

#ifndef NTA_LINKPOLICY_HPP
#define NTA_LINKPOLICY_HPP

#include <string>
#include <nta/engine/Input.hpp> // SplitterMap definition

// LinkPolicy is an interface class subclassed by all link policies
namespace nta 
{


  class Dimensions;

  class LinkPolicy
  {
    // Subclasses implement this constructor:
    //    LinkPolicy(const std::string params, const Dimensions& srcDimensions,
    //               const Dimensions& destDimensions);

  public:
    virtual ~LinkPolicy() {};
    virtual void setSrcDimensions(Dimensions& dims) = 0;
    virtual void setDestDimensions(Dimensions& dims) = 0;
    virtual const Dimensions& getSrcDimensions() const = 0;
    virtual const Dimensions& getDestDimensions() const = 0;
    // initialization is probably unnecessary, but it lets
    // us do a sanity check before generating the splitter map. 
    virtual void initialize() = 0;
    virtual bool isInitialized() const = 0;
    virtual void setNodeOutputElementCount(size_t elementCount) = 0;


    // A "protoSplitterMap" specifies which source output nodes send 
    // data to which dest input nodes. 
    // if protoSplitter[destNode][x] == srcNode for some x, then 
    // srcNode sends its output to destNode. 
    //
    virtual void buildProtoSplitterMap(Input::SplitterMap& splitter) const = 0;

  };


} // namespace nta

#endif // NTA_LINKPOLICY_HPP
