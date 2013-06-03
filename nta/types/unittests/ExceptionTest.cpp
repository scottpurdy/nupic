/**
 * ----------------------------------------------------------------------
 *  Copyright (C) 2010 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
 */

/** @file
 * Implementation of Fraction test
 */

#include "ExceptionTest.hpp"
#include <nta/types/Exception.hpp>

using namespace nta;

void ExceptionTest::RunTests()
{
  try
  {
    throw nta::Exception("FFF", 123, "MMM");
  }
  catch (const Exception & e)
  {
    TEST(std::string(e.getFilename()) == std::string("FFF"));
    TEST(e.getLineNumber() == 123);
    TEST(std::string(e.getMessage()) == std::string("MMM"));
    TEST(std::string(e.getStackTrace()) == std::string(""));
  }

  try
  {
    throw nta::Exception("FFF", 123, "MMM", "TB");
  }
  catch (const Exception & e)
  {
    TEST(std::string(e.getFilename()) == std::string("FFF"));
    TEST(e.getLineNumber() == 123);
    TEST(std::string(e.getMessage()) == std::string("MMM"));
    TEST(std::string(e.getStackTrace()) == std::string("TB"));
  }  
}

