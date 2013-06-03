/**
 * ----------------------------------------------------------------------
 *  Copyright (C) 2006-2010 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
 */

/** @file */

#ifndef NTA_MEM_PARSER2_HPP
#define NTA_MEM_PARSER2_HPP

#include <vector>
#include <sstream>

#include "nta/types/types.hpp"


namespace nta {
  
////////////////////////////////////////////////////////////////////////////
/// Class for parsing numbers and strings out of a memory buffer. 
///
/// This provides a significant performance advantage over using the standard
/// C++ stream input operators operating on a stringstream in memory. 
///
/// @b Responsibility
///  - provide high level parsing functions for extracing numbers and strings
///     from a memory buffer
///
/// @b Resources/Ownerships:
///  - Owns a memory buffer that it allocates in it's constructor. 
///
/// @b Notes:
///  To use this class, you pass in an input stream and a total # of bytes to the
///  constructor. The constructor will then read that number of bytes from the stream
///  into an internal buffer maintained by the MemParser object. Subsequent calls to 
///  MemParser::get() will extract numbers/strings from the internal buffer. 
///
//////////////////////////////////////////////////////////////////////////////
class MemParser
{
public:

  /////////////////////////////////////////////////////////////////////////////////////
  /// Constructor
  ///
  /// @param in     The input stream to get characters from.
  /// @param bytes  The number of bytes to extract from the stream for parsing. 
  ///               0 means extract all bytes 
  ///////////////////////////////////////////////////////////////////////////////////
  MemParser(std::istream& in, UInt32 bytes=0);

  /////////////////////////////////////////////////////////////////////////////////////
  /// Destructor
  ///
  /// Free the MemParser object
  ///////////////////////////////////////////////////////////////////////////////////
  virtual ~MemParser();
  
  /////////////////////////////////////////////////////////////////////////////////////
  /// Read an unsigned integer out of the stream
  ///
  ///////////////////////////////////////////////////////////////////////////////////
  void get(unsigned long& val);

  /////////////////////////////////////////////////////////////////////////////////////
  /// Read an unsigned long long out of the stream
  ///
  ///////////////////////////////////////////////////////////////////////////////////
  void get(unsigned long long& val);
  
  /////////////////////////////////////////////////////////////////////////////////////
  /// Read an signed integer out of the stream
  ///
  ///////////////////////////////////////////////////////////////////////////////////
  void get(long& val);
  
  /////////////////////////////////////////////////////////////////////////////////////
  /// Read a double precision floating point number out of the stream
  ///
  ///////////////////////////////////////////////////////////////////////////////////
  void get(double& val);
  
  /////////////////////////////////////////////////////////////////////////////////////
  /// Read a double precision floating point number out of the stream
  ///
  ///////////////////////////////////////////////////////////////////////////////////
  void get(float& val);

#ifdef NTA_QUAD_PRECISION
  /////////////////////////////////////////////////////////////////////////////////////
  /// Read a triple precision floating point number out of the stream
  ///
  ///////////////////////////////////////////////////////////////////////////////////
  void get(long double& val);
#endif
  
  /////////////////////////////////////////////////////////////////////////////////////
  /// Read a string out of the stream
  ///
  ///////////////////////////////////////////////////////////////////////////////////
  void get(std::string& val);
  
  
  /////////////////////////////////////////////////////////////////////////////////////
  /// >> operator's
  ///////////////////////////////////////////////////////////////////////////////////
  friend MemParser& operator>>(MemParser& in, unsigned long& val)
  {  
    in.get(val);
    return in;
  }

  friend MemParser& operator>>(MemParser& in, unsigned long long& val)
  {  
    in.get(val);
    return in;
  }

  friend MemParser& operator>>(MemParser& in, long& val)
  {  
    in.get(val);
    return in;
  }

  friend MemParser& operator>>(MemParser& in, unsigned int& val)
  {  
    unsigned long lval;
    in.get(lval);
    val = lval;
    return in;
  }

  friend MemParser& operator>>(MemParser& in, int& val)
  {  
    long lval;
    in.get(lval);
    val = lval;
    return in;
  }

  friend MemParser& operator>>(MemParser& in, double& val)
  {  
    in.get(val);
    return in;
  }

  friend MemParser& operator>>(MemParser& in, float& val)
  {  
    in.get(val);
    return in;
  }

#ifdef NTA_QUAD_PRECISION
  friend MemParser& operator>>(MemParser& in, long double& val)
  {  
    in.get(val);
    return in;
  }
#endif

  friend MemParser& operator>>(MemParser& in, std::string& val)
  {  
    in.get(val);
    return in;
  }


private:
  std::string     str_;
  const char*     bufP_;
  UInt32          bytes_;
  
  const char*     startP_;
  const char*     endP_;

};



} // namespace nta

#endif // NTA_MEM_PARSER2_HPP
