/*
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
 * Utility functions
 */

#ifndef NTA_UTILS_HPP
#define NTA_UTILS_HPP

#include <nta/types/types.hpp>

namespace utils 
{
  inline bool isSystemLittleEndian()
  {
    static const char test[2] = { 1, 0 };
    return (*(short *) test) == 1;
  }

  template<typename T>
  inline void swapBytesInPlace(T *pxIn, nta::Size n)
  {
    union SwapType { T x; unsigned char b[sizeof(T)]; };
    SwapType *px = reinterpret_cast<SwapType *>(pxIn);
    SwapType *pxend = px + n;
    const int stop = sizeof(T) / 2;
    for(; px!=pxend; ++px)
    {
      for(int j=0; j<stop; ++j) std::swap(px->b[j], px->b[sizeof(T)-j-1]);
    }
  }
  
  template<typename T>
  inline void swapBytes(T *pxOut, nta::Size n, const T *pxIn)
  {
    NTA_ASSERT(pxOut != pxIn) << "Use swapBytesInPlace() instead.";
    NTA_ASSERT(!(((pxOut > pxIn) && (pxOut < (pxIn+n))) ||
      ((pxIn > pxOut) && (pxIn < (pxOut+n))))) << "Overlapping ranges not supported.";
    
    union SwapType { T x; unsigned char b[sizeof(T)]; };
    const SwapType *px0 = reinterpret_cast<SwapType *>(pxIn);
    const SwapType *pxend = px0 + n;
    SwapType *px1 = reinterpret_cast<SwapType *>(pxOut);
    for(; px0!=pxend; ++px0, ++px1) {
      for(int j=0; j<sizeof(T); ++j) px1->b[j] = px0->b[sizeof(T)-j-1];
    }
  }
  
} // end of namespace nta

#endif

