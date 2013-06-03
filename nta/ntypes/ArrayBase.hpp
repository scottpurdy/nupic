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
 * Definitions for the ArrayBase class
  * 
  * An ArrayBase object contains a memory buffer that is used for 
  * implementing zero-copy and one-copy operations in NuPIC. 
  * An ArrayBase contains:
  * - a pointer to a buffer
  * - a length
  * - a type
  * - a flag indicating whether or not the object owns the buffer. 
  */

#ifndef NTA_ARRAY_BASE_HPP
#define NTA_ARRAY_BASE_HPP

#include <nta/types/types.h>
#include <string>

namespace nta
{
  /**
   * An ArrayBase is used for passing arrays of data back and forth between 
   * a client application and NuPIC, minimizing copying. It facilitates
   * both zero-copy and one-copy operations.
   */
  class ArrayBase 
  {
  public:
    /**
     * Caller provides a buffer to use. 
     * NuPIC always copies data into this buffer
     * Caller frees buffer when no longer needed. 
     */
    ArrayBase(NTA_BasicType type, void* buffer, size_t count);

    /**
     * Caller does not provide a buffer --
     * Nupic will either provide a buffer via setBuffer or 
     * ask the ArrayBase to allocate a buffer via allocateBuffer.
     */
    explicit ArrayBase(NTA_BasicType type);

    /**
     * The destructor ensures the array doesn't leak its buffer (if
     * it owns it).
     */
    virtual ~ArrayBase();


    /**
     * Ask ArrayBase to allocate its buffer
     */
    void 
    allocateBuffer(size_t count);
  
    void 
    setBuffer(void *buffer, size_t count);

    void 
    releaseBuffer();

    void* 
    getBuffer() const;

    // number of elements of given type in the buffer
    size_t
    getCount() const;
    
    NTA_BasicType 
    getType() const;

  protected:
    // buffer_ is typed so that we can use new/delete
    // cast to/from void* as necessary
    char* buffer_;
    size_t count_;
    NTA_BasicType type_;
    bool own_;
  };
}

#endif

