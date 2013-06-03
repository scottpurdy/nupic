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

// ---
//
// Definitions for the Array class
//  
// It is a sub-class of ArrayBase that owns its buffer
//
// ---

#ifndef NTA_ARRAY_HPP
#define NTA_ARRAY_HPP

#include <nta/ntypes/ArrayBase.hpp>
#include <nta/utils/Log.hpp>

namespace nta
{
  class Array : public ArrayBase 
  {
  public:
    Array(NTA_BasicType type, void * buffer, size_t count) :
      ArrayBase(type, buffer, count)
    {
    }
    
    explicit Array(NTA_BasicType type) : ArrayBase(type)
    {
    }

    //Array(const Array & other) : ArrayBase(other)
    //{
    //}

    void invariant()
    {
      if (!own_)
        NTA_THROW << "Array must own its buffer";
    }
  private:
    // Hide base class method (invalid for Array)
    void setBuffer(void * buffer, size_t count);
  };
}

#endif

