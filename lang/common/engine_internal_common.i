
%{
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

#define SWIG_FILE_WITH_INIT


#include <nta/types/types.hpp>
#include <nta/types/types.h>
#include <nta/types/BasicType.hpp>
#include <nta/types/Exception.hpp>
#include <nta/ntypes/Dimensions.hpp>
#include <nta/ntypes/Array.hpp>
#include <nta/ntypes/ArrayRef.hpp>
#include <nta/ntypes/Collection.hpp>

#include <nta/utils/Log.hpp>
#include <nta/utils/LogItem.hpp>
#include <nta/utils/LoggingException.hpp>



#include <lang/py/support/PyArray.hpp>

#include <nta/engine/NuPIC.hpp>
#include <nta/engine/Network.hpp>

#include <nta/engine/Spec.hpp>
#include <nta/utils/Watcher.hpp>
#include <nta/engine/Region.hpp>
#include <nta/os/Timer.hpp>
%}

%include "std_pair.i"
%include "std_string.i"
%include "std_vector.i"
%include "std_map.i"
%include "std_set.i" 
%template(StringVec) std::vector<std::string>;


%include <nta/types/types.h>
%include <nta/types/types.hpp>
%include <nta/types/BasicType.hpp>
%include <nta/types/Exception.hpp>

// For Network::get/setPhases()
%template(UInt32Set) std::set<nta::UInt32>;


%template(Dimset) std::vector<size_t>;
%include <nta/ntypes/Dimensions.hpp>
%include <nta/ntypes/Array.hpp>
%include <nta/ntypes/ArrayRef.hpp>

%include <nta/ntypes/Collection.hpp>
%template(InputCollection) nta::Collection<nta::InputSpec>;
%template(OutputCollection) nta::Collection<nta::OutputSpec>;
%template(ParameterCollection) nta::Collection<nta::ParameterSpec>;
%template(CommandCollection) nta::Collection<nta::CommandSpec>;
%template(RegionCollection) nta::Collection<nta::Region *>;

%include <nta/engine/NuPIC.hpp>
%include <nta/engine/Network.hpp>
%ignore nta::Region::getInputData;
%ignore nta::Region::getOutputData;
%include <nta/engine/Region.hpp>
%include <nta/utils/Watcher.hpp>
%include <nta/engine/Spec.hpp>

%template(InputPair) std::pair<std::string, nta::InputSpec>;
%template(OutputPair) std::pair<std::string, nta::OutputSpec>;
%template(ParameterPair) std::pair<std::string, nta::ParameterSpec>;
%template(CommandPair) std::pair<std::string, nta::CommandSpec>;
%template(RegionPair) std::pair<std::string, nta::Region *>;

%include <nta/os/Timer.hpp>

  
