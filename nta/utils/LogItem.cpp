/**
 * ----------------------------------------------------------------------
 *  Copyright (C) 2006,2007 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 */

/** @file
* LogItem implementation
*/


#include <nta/utils/LogItem.hpp>
#include <nta/types/Exception.hpp>
#include <iostream>  // cout
#include <stdexcept> // runtime_error

using namespace nta;

std::ostream* LogItem::ostream_ = NULL;

void LogItem::setOutputFile(std::ostream& ostream)
{
  ostream_ = &ostream;
}

LogItem::LogItem(const char *filename, int line, LogLevel level)
  : filename_(filename), lineno_(line), level_(level), msg_("") 
{}

LogItem::~LogItem()
{
  std::string slevel;
  switch(level_)
  {
  case debug:
    slevel = "DEBUG:";
    break;
  case warn:
    slevel = "WARN: ";
    break;
  case info:
    slevel = "INFO: ";
    break;
  case error:
    slevel = "ERROR:";
    break;
  default:
    slevel = "Unknown: ";
    break;
  }


  if (ostream_ == NULL)
    ostream_ = &(std::cout);

  (*ostream_) << slevel << "  " << msg_.str();
  if (level_ == error)
    (*ostream_) << " [" << filename_ << " line " << lineno_ << "]";
  (*ostream_) << std::endl;

}

std::ostringstream& LogItem::stream() {
  return msg_;
}


