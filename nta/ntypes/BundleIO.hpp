/*
 * ----------------------------------------------------------------------
 *  Copyright (C) 2010 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
 */

#ifndef NTA_BUNDLEIO_HPP
#define NTA_BUNDLEIO_HPP

#include <nta/os/Path.hpp>
#include <nta/os/FStream.hpp>

namespace nta
{
  class BundleIO
  {
  public:
    BundleIO(const std::string& bundlePath, const std::string& label, 
             const std::string& regionName, bool isInput);

    ~BundleIO();

    // These are {o,i}fstream instead of {o,i}stream so that
    // the node can explicitly close() them. 
    std::ofstream& getOutputStream(const std::string& name) const;

    std::ifstream& getInputStream(const std::string& name) const;

    std::string getPath(const std::string& name) const;

  private:

    // Before a request for a new stream, 
    // there should be no open streams. 
    void checkStreams_() const;

    // Should never read and write at the same time -- this helps
    // to enforce.
    bool isInput_;

    // We only need the file prefix, but store the bundle path
    // for error messages
    std::string bundlePath_;

    // Store the whole prefix instead of just the label
    std::string filePrefix_;

    // Store the region name for debugging
    std::string regionName_; 

    // We own the streams -- helps with finding errors
    // and with enforcing one-stream-at-a-time
    // These are mutable because the bundle doesn't conceptually
    // change when you serialize/deserialize. 
    mutable std::ofstream *ostream_;
    mutable std::ifstream *istream_;

  }; // class BundleIO
} // namespace nta

#endif // NTA_BUNDLEIO_HPP
