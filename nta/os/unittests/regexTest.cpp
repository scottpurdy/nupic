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

/** @file
 * Implementation for Directory test
 */


#include <nta/os/regex.hpp>
#include "regexTest.hpp"

using namespace std;
using namespace nta;


void regexTest::RunTests()
{
  
  TEST(regex::match(".*", ""));
  TEST(regex::match(".*", "dddddfsdsgregegr"));
  TEST(regex::match("d.*", "d"));  
  TEST(regex::match("^d.*", "ddsfffdg"));
  TEST(!regex::match("d.*", ""));
  TEST(!regex::match("d.*", "a"));
  TEST(!regex::match("^d.*", "ad"));
  TEST(!regex::match("Sensor", "CategorySensor"));
  
  
  TEST(regex::match("\\\\", "\\"));  
                
//  TEST(regex::match("\\w", "a"));  
//  TEST(regex::match("\\d", "3"));    
//  TEST(regex::match("\\w{3}", "abc"));
//  TEST(regex::match("^\\w{3}$", "abc"));  
//  TEST(regex::match("[\\w]{3}", "abc"));  
  
  TEST(regex::match("[A-Za-z0-9_]{3}", "abc"));
  
  // Invalid expression tests (should throw)
  try
  {
    TEST(regex::match("", ""));
    TEST(false);
  }
  catch (...)
  {
  }
   
  try
  {
    TEST(regex::match("xyz[", ""));
    TEST(false);
  }
  catch (...)
  {
  }
}

