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
 * Definition of the Internal Output API
 *
*/

#ifndef NTA_OUTPUT_HPP
#define NTA_OUTPUT_HPP

#include <set>
#include <nta/types/types.hpp>
#include <nta/utils/Log.hpp> // temporary, while impl is in this file
namespace nta
{

  class Link;
  class Region;
  class Array;

  class Output
  {
  public:
    Output(Region& region, NTA_BasicType type, bool isRegionLevel);

    ~Output();

    // Outputs need to know their own name
    void setName(const std::string& name);

    const std::string& getName() const;

    void
    initialize(size_t size);

    // does not take ownership
    void
    addLink(Link* link);

    // Called only by Input::removeLink() even
    // if triggered by removing the region that contains us
    void
    removeLink(Link*);

    // We cannot delete a region if there are any outgoing links
    // This allows us to check in Network::removeRegion and 
    // the network destructor;
    bool
    hasOutgoingLinks();

    // important to return a const array so caller can't
    // reallocate the buffer.
    const Array &
    getData() const;

    bool
    isRegionLevel() const;

    Region&
    getRegion() const;

    size_t
    getNodeOutputElementCount() const;

  private:

    Region& region_; // needed for number of nodes
    Array * data_;
    bool isRegionLevel_;
    // order of links never matters, so store as a set
    // this is different from Input, where they do matter
    std::set<Link*> links_;
    std::string name_;
    size_t nodeOutputElementCount_;
  };

}


#endif // NTA_OUTPUT_HPP
