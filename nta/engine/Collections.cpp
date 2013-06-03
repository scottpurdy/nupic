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


#include <nta/engine/Spec.hpp>

/*
 * We need to import the code from Collection.cpp 
 * in order to instantiate all the methods in the classes
 * instantiated below. 
 */
#include <nta/ntypes/Collection.hpp>
#include <nta/ntypes/Collection.cpp>
#include <nta/engine/Region.hpp>
#include <nta/engine/Network.hpp>

using namespace nta;


// Explicit instantiations of the collection classes used by Spec
template class nta::Collection<OutputSpec>;
template class nta::Collection<InputSpec>;
template class nta::Collection<ParameterSpec>;
template class nta::Collection<CommandSpec>;
template class nta::Collection<Region*>;
template class nta::Collection<Network::callbackItem>;

