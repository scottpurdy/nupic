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
 * Win32 Implementations for the OS class
 */

#ifdef WIN32
#include <windows.h>
#include <shlobj.h>

#include <nta/os/OS.hpp>
#include <nta/os/Directory.hpp>
#include <nta/os/Path.hpp>
#include <nta/os/Directory.hpp>
#include <nta/os/Env.hpp>
#include <nta/utils/Log.hpp>
#include <nta/os/DynamicLibrary.hpp>
#include <boost/shared_ptr.hpp>


using namespace nta;

std::string OS::getHomeDir()
{
  std::string homeDrive;
  std::string homePath;
  bool found = Env::get("HOMEDRIVE", homeDrive);
  NTA_CHECK(found) << "'HOMEDRIVE' environment variable is not defined";
  found = Env::get("HOMEPATH", homePath);
  NTA_CHECK(found) << "'HOMEPATH' environment variable is not defined";
  return homeDrive + homePath;
}

std::string OS::getUserName()
{
  std::string username;
  bool found = Env::get("USERNAME", username);
  NTA_CHECK(found) << "Environment variable USERNAME is not defined";

  return username;
}

int OS::getLastErrorCode()
{
  return ::GetLastError();
}

std::string OS::getErrorMessageFromErrorCode(int errorCode)
{ 
  // Retrieve the system error message for the last-error code
  LPVOID lpMsgBuf;

  DWORD msgLen = ::FormatMessageA(
      FORMAT_MESSAGE_ALLOCATE_BUFFER | 
      FORMAT_MESSAGE_FROM_SYSTEM |
      FORMAT_MESSAGE_IGNORE_INSERTS,
      NULL,
      errorCode,
      MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),
      (LPSTR) &lpMsgBuf,
      0, NULL
    );

  std::ostringstream errMessage;
  if(msgLen > 0) {
    errMessage.write((LPSTR) lpMsgBuf, msgLen);
  }
  else {
    errMessage << "Error code: " << errorCode;
  }

  LocalFree(lpMsgBuf);

  return errMessage.str();
}

std::string OS::getErrorMessage()
{
  return getErrorMessageFromErrorCode (getLastErrorCode());
}


#endif //#ifdef WIN32

