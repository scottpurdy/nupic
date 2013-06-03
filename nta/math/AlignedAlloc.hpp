/*
 * ----------------------------------------------------------------------
 *  Copyright (C) 2009 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
 */

/**
 * Aligned memory allocation, needed when working with SSE.
 */

#ifndef NTA_ALIGNED_ALLOC_HPP
#define NTA_ALIGNED_ALLOC_HPP

#ifdef NUPIC2
#error "AlignedAlloc.hpp is not used and should not be part of NuPIC 2"
#endif

#ifdef NTA_PLATFORM_win32
#include <malloc.h> // for _aligned_malloc and _aligned_free
#endif

#include <stdlib.h>

//--------------------------------------------------------------------------------
/**
 * Provides aligned memory allocation and deallocation in a cross-platform fashion.
 * Working with aligned memory is more efficient when working with SSE instructions
 * because there are specialized, fast instructions to load aligned memory into the 
 * XMM registers.
 *
 * On darwin86, malloc is guaranteed to return an aligned pointer:
 * "The malloc(), calloc(), valloc(), realloc(), and reallocf() functions allo-
 *  cate memory.  The allocated memory is aligned such that it can be used for
 *  any data type, including AltiVec- and SSE-related types.  The free() func-
 *  tion frees allocations that were created via the preceding allocation func-
 *  tions."
 *
 * However on Windows, special functions need to be used to achieve alignment.
 *
 * Note that there needs to be exactly as many calls to AlignedFree as there
 * are calls to AlignedMalloc.
 */
namespace nta {
  
  //--------------------------------------------------------------------------------
  /**
   * Aligned memory allocation. Call AlignedFree to deallocate.
   * 
   * Parameters:
   * ==========
   * - size: size of the requested memory allocation, in bytes
   */
  inline void* AlignedMalloc(size_t size)
  {
#ifdef NTA_PLATFORM_win32
    // 16 is the alignment value we need for SSE
    return _aligned_malloc(size, 16);
#else
    return malloc(size);
#endif
  }

  //--------------------------------------------------------------------------------
  /**
   * Aligned memory deallocation. Call AlignedMalloc to allocate.
   *
   * Parameters:
   * ==========
   * - ptr: pointer to the memory to deallocate
   */
  inline void AlignedFree(void* ptr)
  {
#ifdef NTA_PLATFORM_win32
    _aligned_free(ptr);
#else
    free(ptr);
#endif
  }
  
}; // end namespace nta

//--------------------------------------------------------------------------------
#endif //NTA_ALIGNED_ALLOC_HPP
