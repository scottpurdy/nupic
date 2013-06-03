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

/** @file */

//----------------------------------------------------------------------

#include <nta/os/DynamicLibrary.hpp>
#include <nta/os/Path.hpp>
#include <sstream>
#include <iostream>

//----------------------------------------------------------------------

namespace nta 
{

  DynamicLibrary::DynamicLibrary(void * handle) : handle_(handle)
  {
  }

  DynamicLibrary::~DynamicLibrary()
  {
    #ifndef WIN32
      ::dlclose(handle_);
    #else
      ::FreeLibrary((HMODULE)handle_);
    #endif
  }

  DynamicLibrary * DynamicLibrary::load(const std::string & name, std::string &errorString)
  {
    #ifdef WIN32
      return load(name, 0, errorString);
    #else
      // LOCAL/NOW make more sense. In NuPIC 2 we currently need GLOBAL/LAZY
      // See comments in RegionImplFactory.cpp
      // return load(name, LOCAL | NOW, errorString);
      return load(name, GLOBAL | LAZY, errorString);
    #endif
  }

  DynamicLibrary * DynamicLibrary::load(const std::string & name, UInt32 mode, std::string & errorString)
  {
    if (name.empty()) 
    {
      errorString = "Empty path.";
      return NULL;
    }

    //if (!Path::exists(name))
    //{
    //  errorString = "Dynamic library doesn't exist.";
    //  return NULL;
    //}
    
    void * handle = NULL;
  
    #ifdef WIN32
      mode; // ignore on Windows
      handle = ::LoadLibraryA(name.c_str());
      if (handle == NULL)
      {
        DWORD errorCode = ::GetLastError();
        std::stringstream ss;
        ss << std::string("LoadLibrary(") << name 
           << std::string(") Failed. errorCode: ") 
           << errorCode; 
        errorString = ss.str();
        return NULL;
      }
    #else
      handle = ::dlopen(name.c_str(), mode);
      if (!handle) 
      {
        std::string dlErrorString;
        const char *zErrorString = ::dlerror();
        if (zErrorString)
          dlErrorString = zErrorString;
        errorString += "Failed to load \"" + name + '"';
        if(dlErrorString.size())
          errorString += ": " + dlErrorString;
        return NULL;
      }

    #endif
    return new DynamicLibrary(handle);

  }

  void * DynamicLibrary::getSymbol(const std::string & symbol)
  {    
    #ifdef WIN32
      return ::GetProcAddress((HMODULE)handle_, symbol.c_str());
    #else
      return ::dlsym(handle_, symbol.c_str());
    #endif
  }
}
