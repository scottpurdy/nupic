/**
 * ----------------------------------------------------------------------
 *  Copyright (C) 2006,2007 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
*/


%include <nta/types/types.h>
%include <nta/types/types.hpp>

///////////////////////////////////////////////////////////////////
///  Bring in SWIG typemaps for base types and stl.
///////////////////////////////////////////////////////////////////
%include <typemaps.i>
%include <stl.i>
%include <std_list.i>
%include <std_set.i>

///////////////////////////////////////////////////////////////////
///  Instantiate templates that we will use.
///////////////////////////////////////////////////////////////////

%template(VectorOfInt32) std::vector<NTA_Int32>;
%template(VectorOfInt64) std::vector<NTA_Int64>;
%template(VectorOfUInt32) std::vector<NTA_UInt32>;
%template(VectorOfUInt64) std::vector<NTA_UInt64>;

%template(FloatVector) std::vector<NTA_Real32>;
%template(DoubleVector) std::vector<NTA_Real64>;

%template(StringVector) std::vector<std::string>;
%template(StringList) std::list<std::string>;
%template(StringSet) std::set<std::string>;
%template(StringMap) std::map<std::string, std::string>;

%template(StringStringPair) std::pair<std::string, std::string>;
%template(StringStringList) std::vector< std::pair<std::string, std::string> >;
%template(StringMapList) std::vector< std::map<std::string, std::string> >;
%template(StringIntPair) std::pair<std::string, NTA_Int32>;

%template(PairOfUInt32) std::pair<nta::UInt32, nta::UInt32>;
%template(VectorOfPairsOfUInt32) std::vector<std::pair<nta::UInt32,nta::UInt32> >;
%template(VectorOfVectorsOfPairsOfUInt32) std::vector<std::vector<std::pair<nta::UInt32,nta::UInt32> > >;

%template(PairUInt32Real32) std::pair<nta::UInt32,nta::Real32>;
%template(PairUInt32Real64) std::pair<nta::UInt32,nta::Real64>;
%template(VectorOfPairsUInt32Real32) std::vector<std::pair<nta::UInt32,nta::Real32> >;
%template(VectorOfPairsUInt32Real64) std::vector<std::pair<nta::UInt32,nta::Real64> >;
#ifdef NTA_QUAD_PRECISION
%template(PairUInt32Real128) std::pair<nta::UInt32,nta::Real128>;
%template(SizeTReal128Vector) std::vector<std::pair<nta::UInt32,nta::Real128> >;
#endif




