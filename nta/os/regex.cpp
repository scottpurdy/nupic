/*
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
*/

#include <nta/os/regex.hpp>
#include <nta/utils/Log.hpp>
#ifdef WIN32
  #include <pcre/pcreposix.h>
#else
  #include <regex.h>
#endif

namespace nta
{
  namespace regex
  {
    bool match(const std::string & re, const std::string & text)
    {        
      NTA_CHECK(!re.empty()) << "Empty regular expressions is invalid";
      
      // Make sure the regex will perform an exact match
      std::string exactRegExp;
      if (re[0] != '^')
        exactRegExp += '^';
      exactRegExp += re;
      if (re[re.length()-1] != '$') 
        exactRegExp += '$';
      
      regex_t r;
      int res = ::regcomp(&r, exactRegExp.c_str(), REG_EXTENDED|REG_NOSUB);
      NTA_CHECK(res == 0) 
        << "regcomp() failed to compile the regular expression: "
        << re << " . The error code is: " << res;
        
      res = regexec(&r, text.c_str(), (size_t) 0, NULL, 0);
      ::regfree(&r);
      return res == 0; 
    }
  }
}
