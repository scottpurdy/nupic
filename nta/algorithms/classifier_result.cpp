/**
 * ---------------------------------------------------------------------
 * Copyright (C) 2012 Numenta Inc. All rights reserved.
 *
 * The information and source code contained herein is the
 * exclusive property of Numenta Inc. No part of this software
 * may be used, reproduced, stored or distributed in any form,
 * without explicit written authorization from Numenta Inc.
 * ---------------------------------------------------------------------
 */

#include <map>
#include <vector>

#include <nta/algorithms/classifier_result.hpp>
#include <nta/types/types.hpp>

using namespace std;

namespace nta
{
  namespace algorithms
  {
    namespace cla_classifier
    {

      ClassifierResult::~ClassifierResult()
      {
        for (map<UInt, vector<Real64>*>::const_iterator it = result_.begin();
             it != result_.end(); ++it)
        {
          delete it->second;
        }
      }

      vector<Real64>* ClassifierResult::createVector(UInt step, UInt size,
                                                Real64 value)
      {
        vector<Real64>* v;
        map<UInt, vector<Real64>*>::const_iterator it = result_.find(step);
        if (it != result_.end())
        {
          v = it->second;
        } else {
          v = new vector<Real64>(size, value);
          result_.insert(pair<UInt, vector<Real64>*>(step, v));
        }
        return v;
      }

    } // end namespace cla_classifier
  } // end namespace algorithms
} // end namespace nta
