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
 * Timer interface
 */

#ifndef NTA_TIMER2_HPP
#define NTA_TIMER2_HPP

#include <string>
#include <nta/types/types.hpp>

namespace nta 
{

  /**
   * @Responsibility
   * Simple stopwatch services
   * 
   * @Description
   * A timer object is a stopwatch. You can start it, stop it, read the
   * elapsed time, and reset it. It is very convenient for performance
   * measurements. 
   * 
   * Uses the most precise and lowest overhead timer available on a given system.
   *
   */
  class Timer 
  {
  public:

    /**
     * Create a stopwatch
     * 
     * @param startme  If true, the timer is started when created
     */
    Timer(bool startme = false);


    /**
     * Start the stopwatch
     */
    void
    start();


    /**
     * Stop the stopwatch. When restarted, time will accumulate
     */
    void
    stop();


    /**
     * If stopped, return total elapsed time. 
     * If started, return current elapsed time but don't stop the clock
     * return the value in seconds;
     */
    Real64
    getElapsed() const;

    /**
     * Reset the stopwatch, setting accumulated time to zero. 
     */
    void
    reset();

    /**Train
     * Return the number of time the stopwatch has been started.
     */
    UInt64
    getStartCount() const;

    /**
     * Returns true is the stopwatch is currently running
     */
    bool
    isStarted() const;
    
    std::string
    toString() const;

  private:
    // internally times are stored as ticks
    UInt64 prevElapsed_;   // total time as of last stop() (in ticks)
    UInt64 start_;         // time that start() was called (in ticks)
    UInt64 nstarts_;       // number of times start() was called
    bool started_;         // true if was started

  }; // class Timer  
  
} // namespace nta

#endif // NTA_TIMER2_HPP

