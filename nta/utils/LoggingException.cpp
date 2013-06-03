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

#include "LoggingException.hpp"
#include "LogItem.hpp"
#include <iostream>
using namespace nta;

LoggingException::~LoggingException() throw()
{
  if (!alreadyLogged_) {
    // Let LogItem do the work for us. This code is a bit complex
    // because LogItem was designed to be used from a logging macro
    LogItem *li = new LogItem(filename_.c_str(), lineno_, LogItem::error);
    li->stream() << getMessage();
    delete li;
    alreadyLogged_ = true;
  }
}

