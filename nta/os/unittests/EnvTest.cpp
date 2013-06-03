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


#include "EnvTest.hpp"

using namespace nta;

EnvTest::EnvTest() {};

EnvTest::~EnvTest() {};


void EnvTest::RunTests()
{
  std::string name;
  std::string value;
  bool result;
  
  // get value that is not set
  value = "DONTCHANGEME";
  result = Env::get("NOTDEFINED", value);
  TESTEQUAL2("get not set result", false, result);
  TESTEQUAL2("get not set value", "DONTCHANGEME", value.c_str());
  
  // get value that should be set
  value = "";
  result = Env::get("PATH", value);
  TESTEQUAL2("get PATH result", true, result);
  TEST2("get path value", value.length() > 0);
  
  // set a value
  name = "myname";
  value = "myvalue";
  Env::set(name, value);
  
  // retrieve it
  value = "";
  result = Env::get(name, value);
  TESTEQUAL2("get value just set -- result", true, result);
  TESTEQUAL2("get value just set -- value", "myvalue", value.c_str());
  
  // set it to something different
  value = "mynewvalue";
  Env::set(name, value);
  
  // retrieve the new value
  result = Env::get(name, value);
  TESTEQUAL2("get second value just set -- result", true, result);
  TESTEQUAL2("get second value just set -- value", "mynewvalue", value.c_str());
  
  // delete the value
  value = "DONTCHANGEME";
  Env::unset(name);
  result = Env::get(name, value);
  TESTEQUAL2("get after delete -- result", false, result);
  TESTEQUAL2("get after delete -- value", "DONTCHANGEME", value.c_str());
  
  // delete a value that is not set
  // APR response is not documented. Will see a warning if 
  // APR reports an error. 
  // Is there any way to do an actual test here? 
  Env::unset(name);
}

