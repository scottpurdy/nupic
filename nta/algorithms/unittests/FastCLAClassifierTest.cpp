/**
 * ----------------------------------------------------------------------
 * Copyright (C) 2012 Numenta Inc. All rights reserved.
 *
 * The information and source code contained herein is the
 * exclusive property of Numenta Inc. No part of this software
 * may be used, reproduced, stored or distributed in any form,
 * without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
*/

/** @file
 * Implementation of unit tests for NearestNeighbor
 */

#include <iostream>

#include <nta/algorithms/classifier_result.hpp>
#include <nta/algorithms/fast_cla_classifier.hpp>
#include <nta/math/stl_io.hpp>
#include <nta/types/types.hpp>
#include <nta/utils/Log.hpp>
#include "FastCLAClassifierTest.hpp"

using namespace std;
using namespace nta::algorithms::cla_classifier;

namespace nta {

  void FastCLAClassifierTest::RunTests()
  {
    testBasic();
  }

  void FastCLAClassifierTest::testBasic()
  {
    vector<UInt> steps;
    steps.push_back(1);
    FastCLAClassifier* c = new FastCLAClassifier(steps, 0.1, 0.1, 0);

    vector<UInt> input1;
    input1.push_back(1);
    input1.push_back(5);
    input1.push_back(9);
    ClassifierResult result1;
    c->fastCompute(0, input1, 4, 34.7, false, true, true, &result1);

    vector<UInt> input2;
    input2.push_back(1);
    input2.push_back(5);
    input2.push_back(9);
    ClassifierResult result2;
    c->fastCompute(1, input2, 4, 34.7, false, true, true, &result2);

    bool found0 = false;
    bool found1 = false;
    for (map<UInt, vector<Real64>*>::const_iterator it = result2.begin();
         it != result2.end(); ++it)
    {
      if (it->first == 0)
      {
        NTA_CHECK(found0 == false);
        found0 = true;
        NTA_CHECK(it->second->size() == 5);
        NTA_CHECK(fabs(it->second->at(4) - 34.7) < 0.000001);
      } else if (it->first == 1) {
        NTA_CHECK(found1 == false);
        found1 = true;
        NTA_CHECK(it->second->size() == 5);
      }
    }

    delete c;
  }

} // end namespace nta
