/**
 * ----------------------------------------------------------------------
 *  Copyright (C) 2006,2007,2010 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
 */

/** @file
 * Notes
 */ 

#include "MemParserTest.hpp"
#include <nta/ntypes/MemParser.hpp>

#include <stdexcept>
#include <string>
#include <iostream>

namespace nta {

void MemParserTest::RunTests() 
{
  // -------------------------------------------------------
  // Test using get methods
  // -------------------------------------------------------
  {
    std::stringstream ss; 
    
    // Write one of each type to the stream
    unsigned long a = 10;
    long b = -20;
    double c = 1.5;
    float d = 1.6f;
    std::string e = "hello";
    
    ss << a << " " 
       << b << " "
       << c << " "
       << d << " "
       << e << " ";
    
    // Read back 
    MemParser in(ss, (UInt32)ss.str().size());
    
    unsigned long test_a = 0;
    in.get(test_a);
    TESTEQUAL2("get ulong", a, test_a);
    
    long test_b = 0;
    in.get(test_b);
    TESTEQUAL2("get long", b, test_b);
    
    double test_c = 0;
    in.get(test_c);
    TESTEQUAL2("get double", c, test_c);
    
    float test_d = 0;
    in.get(test_d);
    TESTEQUAL2("get float", d, test_d);
    
    std::string test_e = "";
    in.get(test_e);
    TESTEQUAL2("get string", e, test_e);
    

    // Test EOF
    SHOULDFAIL(in.get(test_e));
  }

 
  // -------------------------------------------------------
  // Test passing in -1 for the size to read in entire stream
  // -------------------------------------------------------
  {
    std::stringstream ss; 
    
    // Write one of each type to the stream
    unsigned long a = 10;
    long b = -20;
    double c = 1.5;
    float d = 1.6f;
    std::string e = "hello";
    
    ss << a << " " 
       << b << " "
       << c << " "
       << d << " "
       << e << " ";
    
    // Read back 
    MemParser in(ss);
    
    unsigned long test_a = 0;
    in.get(test_a);
    TESTEQUAL2("get ulong b", a, test_a);
    
    long test_b = 0;
    in.get(test_b);
    TESTEQUAL2("get long b", b, test_b);
    
    double test_c = 0;
    in.get(test_c);
    TESTEQUAL2("get double b", c, test_c);
    
    float test_d = 0;
    in.get(test_d);
    TESTEQUAL2("get float b", d, test_d);
    
    std::string test_e = "";
    in.get(test_e);
    TESTEQUAL2("get string b", e, test_e);
    

    // Test EOF
    SHOULDFAIL(in.get(test_e));
  }

 
  // -------------------------------------------------------
  // Test using >> operator
  // -------------------------------------------------------
  {
    std::stringstream ss; 
    
    // Write one of each type to the stream
    unsigned long a = 10;
    long b = -20;
    double c = 1.5;
    float d = 1.6f;
    std::string e = "hello";
    
    ss << a << " " 
       << b << " "
       << c << " "
       << d << " "
       << e << " ";
    
    // Read back 
    MemParser in(ss, (UInt32)ss.str().size());
    
    unsigned long test_a = 0;
    long test_b = 0;
    double test_c = 0;
    float test_d = 0;
    std::string test_e = "";
    in >> test_a >> test_b >> test_c >> test_d >> test_e;
    TESTEQUAL2(">> ulong", a, test_a);
    TESTEQUAL2(">> long", b, test_b);
    TESTEQUAL2(">> double", c, test_c);
    TESTEQUAL2(">> float", d, test_d);
    TESTEQUAL2(">> string", e, test_e);
    

    // Test EOF
    SHOULDFAIL(in >> test_e);
  }

 
  // -------------------------------------------------------
  // Test reading trying to read an int when we have a string
  // -------------------------------------------------------
  {
    std::stringstream ss; 
    ss << "hello";
        
    // Read back 
    MemParser in(ss, (UInt32)ss.str().size());
    
    // Test EOF
    long  v;
    SHOULDFAIL(in.get(v));
  } 
}






} // namespace nta
