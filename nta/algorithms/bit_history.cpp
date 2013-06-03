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
#include <math.h>
#include <sstream>
#include <string>
#include <vector>

#include <nta/algorithms/bit_history.hpp>
#include <nta/types/types.hpp>
#include <nta/utils/Log.hpp>

namespace nta
{
  namespace algorithms
  {
    namespace cla_classifier
    {

      const Real64 DUTY_CYCLE_UPDATE_INTERVAL = pow(3.2, 32);

      BitHistory::BitHistory(UInt bitNum, int nSteps, Real64 alpha,
                             UInt verbosity) :
          lastTotalUpdate_(-1), learnIteration_(0), alpha_(alpha),
          verbosity_(verbosity)
      {
        stringstream ss;
        ss << bitNum << "[" << nSteps << "]";
        id_ = ss.str();
      }

      void BitHistory::store(int iteration, int bucketIdx)
      {
        if (lastTotalUpdate_ == -1)
        {
          lastTotalUpdate_ = iteration;
        }

        // Get the previous duty cycle, or 0.0 for new buckets.
        map<int, Real64>::const_iterator it = stats_.find(bucketIdx);
        Real64 dc = 0.0;
        if (it != stats_.end())
        {
          dc = it->second;
        }

        // Compute the new duty cycle, dcNew, at the iteration that the duty
        // cycles are currently at.
        Real64 denom = pow(1.0 - alpha_, iteration - lastTotalUpdate_);
        Real64 dcNew = -1.0;
        if (denom > 0.0)
        {
          dcNew = dc + (alpha_ / denom);
        }

        if (denom  < 0.00001 or dcNew > DUTY_CYCLE_UPDATE_INTERVAL)
        {
          // Update all duty cycles to the current iteration.
          Real64 exp = pow(1.0 - alpha_, iteration - lastTotalUpdate_);
          for (map<int, Real64>::const_iterator i = stats_.begin();
               i != stats_.end(); ++i)
          {
            stats_[i->first] = i->second * exp;
          }

          lastTotalUpdate_ = iteration;

          dc = stats_[bucketIdx] + alpha_;
        } else {
          dc = dcNew;
        }

        // Set the new duty cycle for the specified bucket.
        stats_[bucketIdx] = dc;
      }

      void BitHistory::infer(int iteration, vector<Real64>* votes)
      {
        Real64 total = 0.0;
        // Set the vote for each bucket to the duty cycle value.
        for (map<int, Real64>::const_iterator it = stats_.begin();
             it != stats_.end(); ++it)
        {
          if (it->second > 0.0)
          {
            (*votes)[it->first] = it->second;
            total += it->second;
          }
        }

        // Normalize the duty cycles.
        if (total > 0.0)
        {
          for (UInt i = 0; i < votes->size(); ++i)
          {
            (*votes)[i] = (*votes)[i] / total;
          }
        }
      }

      void BitHistory::save(ostream& outStream) const
      {
        // Write out a starting marker.
        outStream << "BitHistory" << endl;

        // Save the simple variables.
        outStream << id_ << " "
                  << lastTotalUpdate_ << " "
                  << learnIteration_ << " "
                  << alpha_ << " "
                  << verbosity_ << " "
                  << endl;

        // Save the bucket duty cycles.
        outStream << stats_.size() << " ";
        for (map<int, Real64>::const_iterator it = stats_.begin();
             it != stats_.end(); ++it)
        {
          outStream << it->first << " " << it->second << " ";
        }
        outStream << endl;

        // Write out a termination marker.
        outStream << "~BitHistory" << endl;
      }

      void BitHistory::load(istream& inStream)
      {
        // Check the starting marker.
        string marker;
        inStream >> marker;
        NTA_CHECK(marker == "BitHistory");

        // Load the simple variables.
        inStream >> id_
                 >> lastTotalUpdate_
                 >> learnIteration_
                 >> alpha_
                 >> verbosity_;

        // Load the bucket duty cycles.
        UInt numBuckets;
        int bucketIdx;
        Real64 dutyCycle;
        inStream >> numBuckets;
        for (UInt i = 0; i < numBuckets; ++i)
        {
          inStream >> bucketIdx >> dutyCycle;
          stats_.insert(pair<int, Real64>(bucketIdx, dutyCycle));
        }

        // Check the termination marker.
        inStream >> marker;
        NTA_CHECK(marker == "~BitHistory");
      }

    } // end namespace cla_classifier
  } // end namespace algorithms
} // end namespace nta
