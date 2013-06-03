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

//----------------------------------------------------------------------

#ifndef NTA_LOGGING_EXCEPTION_HPP
#define NTA_LOGGING_EXCEPTION_HPP

#include <nta/types/Exception.hpp>
#include <sstream>

namespace nta
{
  class LoggingException : public Exception
  {
  public:
    LoggingException(const std::string& filename, UInt32 lineno) :
      Exception(filename, lineno, std::string()), ss_(std::string()),
      lmessageValid_(false), alreadyLogged_(false)
    {
    }

    virtual ~LoggingException() throw();

    virtual const char * getMessage() const
    {
      // Make sure we use a persistent string. Otherwise the pointer may
      // become invalid. 
      // If the underlying stringstream object hasn't changed, don't regenerate lmessage_.
      // This is important because if we catch this exception a second call to exception.what() 
      // will trash the buffer returned by a first call to exception.what()
      if (! lmessageValid_) {
        lmessage_ = ss_.str();
        lmessageValid_ = true;
      }
      return lmessage_.c_str();
    }

    template <typename T> LoggingException& operator<<(const T& obj)
    {
      // underlying stringstream changes, so let getMessage() know 
      // to regenerate lmessage_
      lmessageValid_ = false;
      ss_ << obj;
      return *this;
    }

    LoggingException(const LoggingException& l) : Exception(l), 
                                                  ss_(l.ss_.str()), 
                                                  lmessage_(""), 
                                                  lmessageValid_(false),
                                                  alreadyLogged_(true) // copied exception does not log

    {
      // make sure message string is up to date for debuggers. 
      getMessage();
    }

  private:
    std::stringstream ss_;
    mutable std::string lmessage_;  // mutable because getMesssage() modifies it
    mutable bool lmessageValid_;
    bool alreadyLogged_;
  }; // class LoggingException

}

#endif // NTA_LOGGING_EXCEPTION_HPP
