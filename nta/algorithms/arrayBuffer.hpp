/**
* ----------------------------------------------------------------------
 *  Copyright (C) 2008 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
 */

/** @file 
 *  This header file defines the data structures used for
 *  facilitating the passing of numpy arrays from python
 *  code to C code.
 */ 

#ifndef NTA_ARRAY_BUFFER_HPP
#define NTA_ARRAY_BUFFER_HPP

#ifdef __cplusplus
extern "C" {
#endif  // __cplusplus


// Structure that wraps the essential elements of 
// a numpy array object.
typedef struct _NUMPY_ARRAY {
  int nNumDims;
  const int * pnDimensions;
  const int * pnStrides;
  const char * pData;
} NUMPY_ARRAY; 

// Bounding box
typedef struct _BBOX {
  int   nLeft;
  int   nRight;
  int   nTop;
  int   nBottom;
} BBOX;

// Macros for clipping boxes
#ifndef MIN
#define MIN(x, y)    ((x) <= (y) ? (x) : (y))
#endif // MIN
#ifndef MAX
#define MAX(x, y)    ((x) <= (y) ? (y) : (x))
#endif // MAX

#ifdef __cplusplus
}
#endif  // __cplusplus

#endif // NTA_ARRAY_BUFFER_HPP
