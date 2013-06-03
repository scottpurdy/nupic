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
 * Declarations for VectorFileEffector class
 */

//----------------------------------------------------------------------

#ifndef NTA_VECTOR_FILE_EFFECTOR_HPP
#define NTA_VECTOR_FILE_EFFECTOR_HPP

//----------------------------------------------------------------------

#include <nta/types/types.h>
#include <nta/os/FStream.hpp>
#include <nta/engine/RegionImpl.hpp>
#include <nta/ntypes/Array.hpp>
#include <nta/ntypes/ArrayRef.hpp>

namespace nta
{

  class ValueMap;

  /**
   *  VectorFileEffector is a node that takes its input vectors and
   *  writes them sequentially to a file.
   *  
   *  The current input vector is written (but not flushed) to the file
   *  each time the effector's compute() method is called.
   *
   *  The file format for the file is a space-separated list of numbers, with
   *  one vector per line:
   *
   *        e11 e12 e13 ... e1N
   *        e21 e22 e23 ... e2N
   *           :
   *        eM1 eM2 eM3 ... eMN
   *
   *  VectorFileEffector implements the execute() commands as defined in the
   *  nodeSpec.
   *
   */
  class VectorFileEffector : public RegionImpl
  {
  public:
    
    static Spec* createSpec();
    size_t getNodeOutputElementCount(const std::string& outputName);
    void getParameterFromBuffer(const std::string& name, Int64 index, IWriteBuffer& value);

    void setParameterFromBuffer(const std::string& name, Int64 index, IReadBuffer& value);

    void setParameterString(const std::string& name, Int64 index, const std::string& s);
    std::string getParameterString(const std::string& name, Int64 index);

    void initialize();
  
    VectorFileEffector(const ValueMap& params, Region *region);
  
    VectorFileEffector(BundleIO& bundle, Region* region);

    virtual ~VectorFileEffector();
  

    // ---
    /// Serialize state to bundle
    // ---
    virtual void serialize(BundleIO& bundle);

    // ---
    /// De-serialize state from bundle
    // ---
    virtual void deserialize(BundleIO& bundle);

    void compute();

    virtual std::string executeCommand(const std::vector<std::string>& args, Int64 index);

    
    
  private:
    
    void closeFile();
    void openFile(const std::string& filename);

    ArrayRef dataIn_;
    std::string filename_;          // Name of the output file
    nta::OFStream *outFile_;        // Handle to current file
    
    /// Disable unsupported default constructors
    VectorFileEffector(const VectorFileEffector&);
    VectorFileEffector& operator=(const VectorFileEffector&);
    
  }; // end class VectorFileEffector
  
  //----------------------------------------------------------------------
  

#endif // NTA_VECTOR_FILE_EFFECTOR_HPP



} // namespace nta

