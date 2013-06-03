/**
 * ----------------------------------------------------------------------
 *  Copyright (C) 2006-2010 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 */

/** @file
* LogItem interface
*/

#ifndef NTA_LOG_ITEM_HPP
#define NTA_LOG_ITEM_HPP

#include <sstream>
#include <iostream>

namespace nta {

  /**
   * @b Description
   * A LogItem represents a single log entry. It contains a stream that accumulates
   * a log message, and its destructor calls the logger. 
   * 
   * A LogItem contains an internal stream
   * which is used for building up an application message using
   * << operators. 
   * 
   */


  class LogItem {
  public:

    typedef enum {debug, info, warn, error} LogLevel;
    /**
     * Record information to be logged
     */
    LogItem(const char *filename, int line, LogLevel level);

    /**
     * Destructor performs the logging
     */
    virtual ~LogItem();

    /*
     * Return the underlying stream object. Caller will use it to construct the log message. 
     */
    std::ostringstream& stream();

    static void setOutputFile(std::ostream& ostream);


  protected:
    const char *filename_;     // name of file
    int  lineno_;              // line number in file
    LogLevel level_;
    std::ostringstream  msg_; 

  private:
    static std::ostream* ostream_;

  };


}


#endif // NTA_LOG_ITEM_HPP
