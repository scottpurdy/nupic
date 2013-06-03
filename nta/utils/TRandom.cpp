/*
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
    Random Number Generator implementation
*/

#include <nta/utils/TRandom.hpp>
#include <nta/utils/Log.hpp>
#include <nta/utils/StringUtils.hpp>
#include <nta/os/Env.hpp>
#include <cstdlib>
#include <ctime>

using namespace nta;

TRandom::TRandom(std::string name)
{

  UInt64 seed = 0;

  std::string optionName = "set_random";
  if (name != "")
  {
    optionName += "_" + name;
  }

  bool seed_from_environment = false;
  if (Env::isOptionSet(optionName))
  {
    seed_from_environment = true;
    std::string val = Env::getOption(optionName);
    try 
    {
      seed = StringUtils::toUInt64(val, true);
    }
    catch (...)       
    {  
      NTA_WARN << "Invalid value \"" << val << "\" for NTA_SET_RANDOM. Using 1";
      seed = 1;
    }
  }
  else
  {
    // Seed the global rng from time(). 
    // Don't seed subsequent ones from time() because several random 
    // number generators may be initialized within the same second. 
    // Instead, use the global rng.  
    if (theInstanceP_ == NULL) {
      seed = (UInt64)time(NULL);
    } else {
      seed = (*Random::getSeeder())();
    }

  } 

  if (Env::isOptionSet("random_debug"))
  {
    if (seed_from_environment) {
        NTA_INFO << "TRandom(" << name << ") -- initializing with seed " << seed << " from environment";
    } else {
        NTA_INFO << "TRandom(" << name << ") -- initializing with seed " << seed;
    }
  }

  // Create the actual RNG
  // @todo to add different algorithm support, this is where we will
  // instantiate different implementations depending on the requested
  // algorithm 
  reseed(seed);
}
