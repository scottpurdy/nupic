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

/**
 * @file
 * Definition of C++ macros for logging. 
 */

#ifndef NTA_LOG2_HPP
#define NTA_LOG2_HPP

#ifndef NUPIC2
#error "NUPIC2 is not defined when compiling nta/utils/Log.hpp -- this indicates an include error somewhre"
#endif


#ifdef NTA_LOG_HPP
#error "The NuPIC 1 and NuPIC 2 versions of the logging macros are both defined!"
#endif

#include <nta/utils/LoggingException.hpp>
#include <nta/utils/LogItem.hpp>


#define NTA_DEBUG nta::LogItem(__FILE__, __LINE__, nta::LogItem::debug).stream()

// Can be used in Loggable classes
#define NTA_LDEBUG(level) if (logLevel_ < (level)) {}        \
  else nta::LogItem(__FILE__, __LINE__, nta::LogItem::debug).stream()

// For informational messages that report status but do not indicate that anything is wrong
#define NTA_INFO nta::LogItem(__FILE__, __LINE__, nta::LogItem::info).stream()

// For messages that indicate a recoverable error or something else that it may be 
// important for the end user to know about. 
#define NTA_WARN nta::LogItem(__FILE__, __LINE__, nta::LogItem::warn).stream()

// To throw an exception and make sure the exception message is logged appropriately 
#define NTA_THROW throw nta::LoggingException(__FILE__, __LINE__)

// The difference between CHECK and ASSERT is that ASSERT is for
// performance critical code and can be disabled in a release
// build. Both throw an exception on error. 

#define NTA_CHECK(condition) if (condition)  {} \
else NTA_THROW << "CHECK FAILED: \"" << #condition << "\" "

#ifdef NTA_ASSERTIONS_ON

#define NTA_ASSERT(condition) if (condition)  {} \
else NTA_THROW << "ASSERTION FAILED: \"" << #condition << "\" "

#else

// NTA_ASSERT macro does nothing. 
// The second line should never be executed, or even compiled, but we 
// need something that is syntactically compatible with NTA_ASSERT
#define NTA_ASSERT(condition) if (1) {} \
  else nta::LogItem(__FILE__, __LINE__, nta::LogItem::debug).stream()

#endif  // NTA_ASSERTIONS_ON


#endif // NTA_LOG2_HPP
