%module net_internal

# Exception classhes with System.Exception
%rename (BaseException) Exception;

%include "exception.i"
//%include "../common/net_internal_common.i"



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

#include <nta2/types2/types.hpp>
#include <nta2/types2/types.h>
#include <nta2/types2/BasicType.hpp>
#include <nta2/types2/Exception.hpp>
#include <nta2/ntypes/Dimensions.hpp>
#include <nta2/ntypes/Array.hpp>
#include <nta2/ntypes/Collection.hpp>

#include <nta2/utils2/Log.hpp>
#include <nta2/utils2/LogItem.hpp>
#include <nta2/utils2/LoggingException.hpp>

#include <lang/py/support/PyArray.hpp>

#include <nta2/net/NuPIC.hpp>
#include <nta2/net/Network.hpp>

#include <nta2/net/Node.hpp>
#include <nta2/net/Spec.hpp>
#include <nta2/utils2/Watcher.hpp>
#include <nta2/net/Region.hpp>
#include <nta2/os2/Timer.hpp>
%}



//include "std/std_pair.i"

%include "std/std_string.i"

/* 
//%include "std/std_vector.i"
//%include "std/std_map.i"
//%include "std/std_set.i" 
//%template(StringVec) std::vector<std::string>;

//%include <nta2/types2/types.h>
//%include <nta2/types2/types.hpp>
//%include <nta2/types2/BasicType.hpp>
//%include <nta2/types2/Exception.hpp>

// For Network::get/setPhases()
%template(UInt32Set) std::set<nta::UInt32>;


%template(Dimset) std::vector<size_t>;
%include <nta2/ntypes/Dimensions.hpp>
%include <nta2/ntypes/Array.hpp>

%include <nta2/ntypes/Collection.hpp>
%template(InputCollection) nta::Collection<nta::InputSpec>;
%template(OutputCollection) nta::Collection<nta::OutputSpec>;
%template(ParameterCollection) nta::Collection<nta::ParameterSpec>;
%template(CommandCollection) nta::Collection<nta::CommandSpec>;
%template(RegionCollection) nta::Collection<nta::Region *>;

%include <nta2/net/NuPIC.hpp>
%include <nta2/net/Network.hpp>
%include <nta2/net/Node.hpp>
%include <nta2/net/Region.hpp>
%include <nta2/utils2/Watcher.hpp>
%include <nta2/net/Spec.hpp>

%template(InputPair) std::pair<std::string, nta::InputSpec>;
%template(OutputPair) std::pair<std::string, nta::OutputSpec>;
%template(ParameterPair) std::pair<std::string, nta::ParameterSpec>;
%template(CommandPair) std::pair<std::string, nta::CommandSpec>;
%template(RegionPair) std::pair<std::string, nta::Region *>;

%include <nta2/os2/Timer.hpp>

*/