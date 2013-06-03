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
 * Definition of the RegionImpl Factory API
 *
 * A RegionImplFactory creates RegionImpls upon request. 
 * Pynode creation is delegated to another class (TBD). 
 * Because all C++ RegionImpls are compiled in to NuPIC, 
 * the RegionImpl factory knows about them explicitly. 
 * 
 */

#ifndef NTA_REGION_IMPL_FACTORY_HPP
#define NTA_REGION_IMPL_FACTORY_HPP

#include <string>
#include <map>
#include <boost/shared_ptr.hpp>

namespace nta
{

  class RegionImpl;
  class Region;
  class DynamicPythonLibrary;
  struct Spec;
  class BundleIO;

  class RegionImplFactory
  {
  public:
    static RegionImplFactory & getInstance();

    // RegionImplFactory is a lightweight object
    ~RegionImplFactory() {};

    // Create a RegionImpl of a specific type; caller gets ownership.
    RegionImpl* createRegionImpl(const std::string nodeType, 
                                 const std::string nodeParams,
                                 Region* region);

    // Create a RegionImpl from serialized state; caller gets ownership. 
    RegionImpl* deserializeRegionImpl(const std::string nodeType,
                                      BundleIO& bundle,
                                      Region* region);



    // Returns nodespec for a specific node type; Factory retains ownership. 
    Spec* getSpec(const std::string nodeType);

    // RegionImplFactory caches nodespecs and the dynamic library reference
    // This frees up the cached information.
    // Should be called only if there are no outstanding
    // nodespec references (e.g. in NuPIC shutdown) or pynodes. 
    void cleanup();

  private:
    RegionImplFactory() {};
    RegionImplFactory(const RegionImplFactory &);

  private:

    // TODO: implement locking for thread safety for this global data structure
    // TODO: implement cleanup

    // getSpec returns references to nodespecs in this cache. 
    // should not be cleaned up until those references have disappeared. 
    std::map<std::string, Spec*> nodespecCache_;

    // Using shared_ptr here to ensure the dynamic python library object
    // is deleted when the factory goes away. Can't use scoped_ptr
    // because it is not initialized in the constructor.
    boost::shared_ptr<DynamicPythonLibrary> pyLib_; 
  };
}


#endif // NTA_REGION_IMPL_FACTORY_HPP
