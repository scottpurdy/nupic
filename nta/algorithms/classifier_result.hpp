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

#ifndef NTA_classifier_result_HPP
#define NTA_classifier_result_HPP

#include <map>
#include <vector>

#include <nta/types/types.hpp>

using namespace std;

namespace nta
{
  namespace algorithms
  {
    namespace cla_classifier
    {

      /** CLA classifier result class.
       *
       * @b Responsibility
       * The ClassifierResult is responsible for storing result data and
       * cleaning up the data when deleted.
       *
       */
      class ClassifierResult
      {
        public:

          /**
           * Constructor.
           */
          ClassifierResult() {}

          /**
           * Destructor - frees memory allocated during lifespan.
           */
          virtual ~ClassifierResult();

          /**
           * Creates and returns a vector for a given step.
           *
           * The vectors created are stored and can be accessed with the
           * iterator methods. The vectors are owned by this class and are
           * deleted in the destructor.
           *
           * @param step The prediction step to create a vector for. If 0, then
           *             a vector for the actual values to use for each bucket
           *             is returned.
           * @param size The size of the desired vector.
           * @param value The value to populate the vector with.
           *
           * @returns The specified vector.
           */
          virtual vector<Real64>* createVector(UInt step, UInt size, Real64 value);

          /**
           * Iterator method begin.
           */
          virtual map<UInt, vector<Real64>*>::const_iterator begin()
          {
            return result_.begin();
          }

          /**
           * Iterator method end.
           */
          virtual map<UInt, vector<Real64>*>::const_iterator end()
          {
            return result_.end();
          }

        private:

          map<UInt, vector<Real64>*> result_;

      }; // end class ClassifierResult

    } // end namespace cla_classifier
  } // end namespace algorithms
} // end namespace nta

#endif // NTA_classifier_result_HPP
