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

/* @file NuPIC init/shutdown operations */

#include <set>

namespace nta
{
  class Network;

  class NuPIC 
  {
  public:
    static void init();
    static void shutdown();
    static bool isInitialized();
  private:
    /**
     * As a safety measure, don't allow NuPIC to be shut down 
     * if there are any networks still around. Networks 
     * register/unregister themselves at creation and 
     * destruction time.
     * 
     * TBD: license checking will be done in NuPIC::init()
     */
    friend class Network;
    static void registerNetwork(Network* net);
    static void unregisterNetwork(Network* net);
    static std::set<Network*> networks_;
    static bool initialized_;
  };
} // namespace nta

