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

/** @file
 * Basic C++ type definitions used throughout the app and rely on types.h
 */

#ifndef NTA_TYPES_HPP
#define NTA_TYPES_HPP

#include <nta/types/types.h>

//----------------------------------------------------------------------

namespace nta 
{
  // Basic types
  typedef NTA_Byte            Byte;
  typedef NTA_Int16           Int16;
  typedef NTA_UInt16          UInt16;
  typedef NTA_Int32           Int32;
  typedef NTA_UInt32          UInt32;
  typedef NTA_Int64           Int64;
  typedef NTA_UInt64          UInt64;
  typedef NTA_Real32          Real32;
  typedef NTA_Real64          Real64;
  typedef NTA_Handle          Handle;
  // Flexible types (depending on NTA_DOUBLE_PROCESION and NTA_BIG_INTEGER)
  typedef NTA_Real Real;
  typedef NTA_Int  Int;
  typedef NTA_UInt UInt;

  typedef NTA_Size            Size;

  // enums
  enum LogLevel
  {
    LogLevel_None = NTA_LogLevel_None,
    LogLevel_Minimal,
    LogLevel_Normal,
    LogLevel_Verbose,
  };

} // end namespace nta

#ifdef SWIG
#undef NTA_INTERNAL
#endif // SWIG

#endif // NTA_TYPES_HPP



