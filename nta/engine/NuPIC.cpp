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

/* @file Implementation of NuPIC init/shutdown operations */

// TODO -- thread safety
// TODO -- add license check

#include <nta/engine/NuPIC.hpp>
#include <nta/engine/RegionImplFactory.hpp>
#include <nta/utils/Log.hpp>
#include <apr-1/apr_general.h>

namespace nta
{

std::set<Network*> NuPIC::networks_;
bool NuPIC::initialized_ = false;

void NuPIC::init()
{
  if (isInitialized())
    return;
  
  // internal consistency check. Nonzero should be impossible. 
  NTA_CHECK(networks_.size() == 0) << "Internal error in NuPIC::init()";
  
  // Initialize APR
  int argc=1;
  const char *argv[1] = {"NuPIC"};
  // TODO: move to OS::initialize()?
  int result = apr_app_initialize(&argc, (const char* const **)&argv, 0 /*env*/);
  if (result) 
    NTA_THROW << "Error initializing APR (code " << result << ")";

  initialized_ = true;
}


void NuPIC::shutdown()
{
  if (!isInitialized())
  {
    NTA_THROW << "NuPIC::shutdown -- NuPIC has not been initialized";
  }

  if (networks_.size() > 0)
  {
    NTA_THROW << "NuPIC::shutdown -- cannot shut down NuPIC because " 
              << networks_.size() << " networks still exist.";
  }

  RegionImplFactory::getInstance().cleanup();
  initialized_ = false;
}


void NuPIC::registerNetwork(Network* net)
{
  if (!isInitialized())
  {
    NTA_THROW << "Attempt to create a network before NuPIC has been initialized -- call NuPIC::init() before creating any networks";
  }

  std::set<Network*>::iterator n = networks_.find(net);
  // This should not be possible
  NTA_CHECK(n == networks_.end()) << "Internal error -- double registration of network";
  networks_.insert(net);

}

void NuPIC::unregisterNetwork(Network* net)
{
  std::set<Network*>::iterator n = networks_.find(net);
  NTA_CHECK(n != networks_.end()) << "Internal error -- network not registered";
  networks_.erase(n);
}

bool NuPIC::isInitialized()
{
  return initialized_;
}

}

