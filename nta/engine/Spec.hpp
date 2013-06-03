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

/** @file 
Definition of Spec data structures
*/

#ifndef NTA_SPEC_HPP
#define NTA_SPEC_HPP

#include <nta/types/types.hpp>
#include <nta/ntypes/Collection.hpp>
#include <string>
#include <map>

namespace nta
{
  class InputSpec
  {
  public:  
    InputSpec() {}
    InputSpec(
      const std::string & description, 
      NTA_BasicType dataType, 
      UInt32 count, 
      bool required, 
      bool regionLevel, 
      bool isDefaultInput, 
      bool requireSplitterMap = true);

    std::string description;
    NTA_BasicType dataType;
    // TBD: Omit? isn't it always of unknown size?
    // 1 = scalar; > 1 = array of fixed sized; 0 = array of unknown size 
    UInt32 count; 
    // TBD. Omit? what is "required"? Is it ok to be zero length?
    bool required;
    bool regionLevel;
    bool isDefaultInput;
    bool requireSplitterMap; // 
  };

  class OutputSpec
  {
  public:
    OutputSpec() {}
    OutputSpec(const std::string& description, const 
               NTA_BasicType dataType, size_t count, bool regionLevel, bool isDefaultOutput);

    std::string description;
    NTA_BasicType dataType;
    // Size, in number of elements. If size is fixed, specify it here. 
    // Value of 0 means it is determined dynamically
    size_t count; 
    bool regionLevel;
    bool isDefaultOutput;
  };

  class CommandSpec
  {
  public:
    CommandSpec() {}
    CommandSpec(const std::string& description);

    std::string description;

  };

  class ParameterSpec
  {
  public:
    typedef enum { CreateAccess, ReadOnlyAccess, ReadWriteAccess } AccessMode;

    ParameterSpec() {}
    /**
     * @param defaultValue -- a JSON-encoded value
     */
    ParameterSpec(const std::string& description, 
                  NTA_BasicType dataType, size_t count, 
                  const std::string& constraints, const std::string& defaultValue, 
                  AccessMode accessMode);


    std::string description;

    // [open: current basic types are bytes/{u}int16/32/64, real32/64, BytePtr. Is this 
    // the right list? Should we have std::string, jsonstd::string?]
    NTA_BasicType    dataType;
    // 1 = scalar; > 1 = array o fixed sized; 0 = array of unknown size 
    // TODO: should be size_t? Serialization issues?
    size_t      count; 
    std::string constraints;
    std::string defaultValue; // JSON representation; empty std::string means parameter is required
    AccessMode  accessMode;

  };


  struct Spec
  {
    // Return a printable string with Spec information
    // TODO: should this be in the base API or layered? In the API right
    // now since we do not build layered libraries. 
    std::string toString() const;

    // Some RegionImpls support only a single node in a region. 
    // Such regions always have dimension [1]
    bool singleNodeOnly;

    // Description of the node as a whole
    std::string description;

    Collection<InputSpec> inputs;
    Collection<OutputSpec> outputs;
    Collection<CommandSpec> commands;
    Collection<ParameterSpec> parameters;

#ifdef NTA_INTERNAL

    Spec();

    // TODO: decide whether/how to wrap these
    std::string getDefaultOutputName() const;
    std::string getDefaultInputName() const;

    // TODO: need Spec validation, to make sure 
    // that default input/output are defined
    // Currently this is checked in getDefault*, above

#endif // NTA_INTERNAL

  };

} // namespace nta

#endif // NTA_SPEC_HPP
