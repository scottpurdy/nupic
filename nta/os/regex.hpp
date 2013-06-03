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

/** @file */


#ifndef NTA_REGEX_HPP
#define NTA_REGEX_HPP

//----------------------------------------------------------------------

#include <string>

//----------------------------------------------------------------------

namespace nta 
{
  namespace regex
  {
    bool match(const std::string & re, const std::string & text);
  }
}

#endif // NTA_REGEX_HPP


