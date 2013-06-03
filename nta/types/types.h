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
 * Basic C type definitions used throughout the app. It is included by 
 * types.hpp - the C++ basic types file
 */

#ifndef NTA_TYPES_H
#define NTA_TYPES_H

#include <stddef.h>

/*---------------------------------------------------------------------- */
 
/* Basic types enumeration */
typedef enum NTA_BasicType
  {
    NTA_BasicType_Byte,
    NTA_BasicType_Int16,
    NTA_BasicType_UInt16,
    NTA_BasicType_Int32,
    NTA_BasicType_UInt32,
    NTA_BasicType_Int64,
    NTA_BasicType_UInt64,
    NTA_BasicType_Real32,
    NTA_BasicType_Real64,
    NTA_BasicType_Handle, /* Opaque handles or pointers (same as void *) */
    
    /* this is not an actual type just a marker for validation purposes */
    NTA_BasicType_Last,

#ifdef NTA_DOUBLE_PRECISION 
    NTA_BasicType_Real = NTA_BasicType_Real64,
#else 
    NTA_BasicType_Real = NTA_BasicType_Real32,
#endif

  } NTA_BasicType;

/* Basic types */

typedef char           NTA_Byte;

typedef size_t         NTA_Size;

typedef short           NTA_Int16;
typedef unsigned short  NTA_UInt16;
  
typedef float          NTA_Real32;
typedef double         NTA_Real64;
typedef void *         NTA_Handle;

#if defined(NTA_PLATFORM_darwin86)
typedef  int                  NTA_Int32;
typedef  unsigned int         NTA_UInt32;
typedef  long long            NTA_Int64;
typedef  unsigned long long   NTA_UInt64;

#elif defined(NTA_PLATFORM_darwin64)
typedef  int                  NTA_Int32;
typedef  unsigned int         NTA_UInt32;
typedef  long                 NTA_Int64;
typedef  unsigned long        NTA_UInt64;

#elif defined(NTA_PLATFORM_linux32)
typedef  int                  NTA_Int32;
typedef  unsigned int         NTA_UInt32;
typedef  long long            NTA_Int64;
typedef  unsigned long long   NTA_UInt64;

#elif defined(NTA_PLATFORM_win32)
typedef  long                NTA_Int32;
typedef  unsigned long       NTA_UInt32;
typedef  long long           NTA_Int64;
typedef  unsigned long long  NTA_UInt64;

#elif defined(NTA_PLATFORM_linux64)
typedef  int                 NTA_Int32;
typedef  unsigned int        NTA_UInt32;
typedef  long                NTA_Int64;
typedef  unsigned long       NTA_UInt64;
#else
#error "Unknown platform"
#endif

#ifdef NTA_DOUBLE_PRECISION 
  typedef NTA_Real64 NTA_Real;
  #define NTA_REAL_TYPE_STRING "NTA_Real64"
#else
  typedef NTA_Real32 NTA_Real;
  #define NTA_REAL_TYPE_STRING "NTA_Real32"
#endif
  
#ifdef NTA_BIG_INTEGER
  typedef  NTA_Int64  NTA_Int;
  typedef  NTA_UInt64 NTA_UInt;
#else
  typedef  NTA_Int32  NTA_Int;
  typedef  NTA_UInt32 NTA_UInt;
#endif

#ifndef SWIG
#ifdef WIN32
#define NTA_EXPORT __declspec(dllexport)
#define NTA_HIDDEN
#else
#define NTA_EXPORT __attribute__ ((visibility ("default")))
#define NTA_HIDDEN __attribute__ ((visibility ("hidden")))
#endif


#else
#define NTA_HIDDEN
#define NTA_EXPORT
#endif

/* This enum represents the documented logging level
 * of the debug logger. Use LDEBUG(NTA_LogLevelXXX)
 */
typedef enum NTA_LogLevel
  {
    NTA_LogLevel_None,
    NTA_LogLevel_Minimal,
    NTA_LogLevel_Normal,
    NTA_LogLevel_Verbose,
  } NTA_LogLevel;

#endif /* NTA_TYPES_H */
