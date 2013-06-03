/*
 * ----------------------------------------------------------------------
 *  Copyright (C) 2006,2007 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 *----------------------------------------------------------------------
 */


/** @file 
 * Unix Implementations for the OS class
 */

#ifndef WIN32

#include <nta/os/OS.hpp>
#include <nta/os/Path.hpp>
#include <nta/os/Directory.hpp>
#include <nta/os/Env.hpp>
#include <nta/utils/Log.hpp>
#include <fstream>
#include <cstdlib>
#include <unistd.h>   // getuid()
#include <sys/types.h>
#include <apr-1/apr_errno.h>
#include <apr-1/apr_time.h>
#include <apr-1/apr_network_io.h>


using namespace nta;

std::string OS::getErrorMessage()
{
  char buff[1024];
  apr_status_t st = apr_get_os_error();
  ::apr_strerror(st , buff, 1024);
  return std::string(buff);
}



std::string OS::getHomeDir()
{
  std::string home;
  bool found = Env::get("HOME", home);
  if (!found)
    NTA_THROW << "'HOME' environment variable is not defined";
  return home;
}

std::string OS::getUserName()
{
  std::string username;
  bool found = Env::get("USER", username);

  // USER isn't always set inside a cron job
  if (!found)
    found = Env::get("LOGNAME", username);

  if (!found) 
  {
    NTA_WARN << "OS::getUserName -- USER and LOGNAME environment variables are not set. Using userid = " << getuid();
    std::stringstream ss("");
    ss << getuid();
    username = ss.str(); 
  } 

  return username;
}


 


int OS::getLastErrorCode() { return errno; }

std::string OS::getErrorMessageFromErrorCode(int errorCode)
{
  std::stringstream errorMessage;
  char errorBuffer[1024];
  errorBuffer[0] = '\0';
#ifdef __APPLE__
  int result = ::strerror_r(errorCode, errorBuffer, 1024);
  if(result == 0) errorMessage << errorBuffer;
#else
  char *result = ::strerror_r(errorCode, errorBuffer, 1024);
  if(result != 0) errorMessage << errorBuffer;
#endif
  else errorMessage << "Error code " << errorCode;
  return errorMessage.str();
}

#endif // #ifndef WIN32


