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
 * Interface for the OS class
 */

#ifndef NTA_OS_HPP
#define NTA_OS_HPP

#include <string>
#include <vector>
#include <nta/types/types.hpp>

#ifdef _MSC_VER
  #pragma warning (disable: 4996)  
  // The POSIX name for this item is deprecated. Instead, use the ISO C++ 
  // conformant name: _getpid.
#endif

namespace nta  
{
  /* 
   * removed for NuPIC 2:
   * getHostname
   * getUserNTADir
   * setUserNTADir
   * getProcessID
   * getTempDir
   * makeTempFilename
   * sleep
   * executeCommand
   * genCryptoString
   * verifyHostname
   * isProcessAliveWin32
   * killWin32
   * getStackTrace
   */


  /**
   * @b Responsibility
   * Operating system functionality.
   * 
   * @b Description
   * OS is a set of static methods that provide access to operating system functionality
   * for Numenta apps. 
   */

  class OS  
  {
  public:
    /**
     * Get the last error string
     *
     * @retval Returns character string containing the last error message.
     */    
    static std::string getErrorMessage();

    /**
     * 
     * 
     * @return An OS/system library error code.
     */
    static int getLastErrorCode();

    /**
     * Get an OS-level error message associated with an error code.
     *
     * If no error code is specified, gets the error message associated 
     * with the last error code.
     * 
     * @param An error code, usually reported by getLastErrorCode().
     * 
     * @return An error message string.
     */
    static std::string getErrorMessageFromErrorCode(
      int errorCode=getLastErrorCode());

    /**
     * Get the user's home directory
     *
     * The home directory is determined by common environment variables 
     * on different platforms.
     *
     * @retval Returns character string containing the user's home directory.
     */    
    static std::string getHomeDir();


    /**
     * Get the user name
     *
     * A user name is disovered on unix by checking a few environment variables
     * (USER, LOGNAME) and if not found defaulting to the user id. On Windows the 
     * USERNAME environment variable is set by the OS.
     * 
     * @retval Returns character string containing the user name.
     */ 
    static std::string getUserName();

    /**
     * Get process memory usage
     * 
     * Real and Virtual memory usage are returned in bytes
     */
    static void getProcessMemoryUsage(size_t& realMem, size_t& virtualMem);

  };
}

#endif // NTA_OS_HPP
