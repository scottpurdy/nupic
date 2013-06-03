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

/**
 * @file
 */


#include "OSTest.hpp"
#include <nta/os/Env.hpp>
#include <nta/os/Path.hpp>
#include <nta/os/Directory.hpp>

using namespace nta;

OSTest::OSTest() {};

OSTest::~OSTest() {};


void OSTest::RunTests()
{
#ifdef WIN32

#else
  // save the parts of the environment we'll be changing
  std::string savedHOME;
  bool isHomeSet = Env::get("HOME", savedHOME);
  
  Env::set("HOME", "/home1/myhome");
  Env::set("USER", "user1");
  Env::set("LOGNAME", "logname1");
  
  TESTEQUAL2("OS::getHomeDir", "/home1/myhome", OS::getHomeDir());
  bool caughtException = false;
  Env::unset("HOME");
  std::string dummy;
  try {
    dummy = OS::getHomeDir();
  } catch (...) {
    caughtException = true;
  }
  TEST2("getHomeDir -- HOME not set", caughtException == true);
  // restore HOME
  if (isHomeSet) {
    Env::set("HOME", savedHOME);
  }


#endif

  // Test getUserName()
  {
#ifdef WIN32
    Env::set("USERNAME", "123");
    TEST(OS::getUserName() == "123");    
#else
    // case 1 - USER defined
    Env::set("USER", "123");
    TEST(OS::getUserName() == "123");

    // case 2 - USER not defined, LOGNAME defined
    Env::unset("USER");
    Env::set("LOGNAME", "456");
    TEST(OS::getUserName() == "456");

    // case 3 - USER and LOGNAME not defined
    Env::unset("LOGNAME");
    
    std::stringstream ss("");
    ss << getuid();
    TEST(OS::getUserName() == ss.str());
#endif
  }
  

  // Test getStackTrace()
  {
#ifdef WIN32
//    std::string stackTrace = OS::getStackTrace();
//    TEST(!stackTrace.empty());  
//
//    stackTrace = OS::getStackTrace();
//    TEST(!stackTrace.empty());
#endif  
  }
}

