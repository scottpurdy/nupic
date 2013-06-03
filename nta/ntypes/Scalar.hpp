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

/** @file 
 * Definitions for the Scalar class
 * 
 * A Scalar object is an instance of an NTA_BasicType -- essentially a union
 * It is used internally in the conversion of YAML strings to C++ objects. 
 */

#ifndef NTA_SCALAR_HPP
#define NTA_SCALAR_HPP

#include <nta/types/types.h>
#include <nta/utils/Log.hpp> // temporary, while implementation is in hpp
#include <string>

namespace nta
{
  class Scalar
  {
  public:
    Scalar(NTA_BasicType theTypeParam);

    NTA_BasicType getType();

    template <typename T> T getValue() const;


    union {
      NTA_Handle handle;
      NTA_Byte byte;
      NTA_Int16 int16; 
      NTA_UInt16 uint16;
      NTA_Int32 int32;
      NTA_UInt32 uint32;
      NTA_Int64 int64;
      NTA_UInt64 uint64;
      NTA_Real32 real32;
      NTA_Real64 real64;
    } value;


  private:
    NTA_BasicType theType_;

  };

}

#endif // NTA_SCALAR_HPP



