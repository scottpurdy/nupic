#ifdef NTA_PYTHON_SUPPORT

/**
 * ----------------------------------------------------------------------
 *  Copyright (C) 2009 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
 */

#include <lang/py/support/PythonStream.hpp>
#include <nta/utils/Log.hpp>
#include <strstream>

/**
 * Bumps up size to a nicely aligned larger size.
 * Taken for NuPIC2 from PythonUtils.hpp
 */
static size_t NextPythonSize(size_t n)
{
  n += 1;
  n += 8 - (n % 8);
  return n;
}

// -------------------------------------------------------------
struct SharedPythonOStreamInternals
{
  SharedPythonOStreamInternals(PyObject * pys, char * buffer, size_t maxSize) :
    pys(pys), 
    s(buffer, maxSize)
  {
  }
  
  nta::py::Ptr pys;
  std::strstream s;
};

// -------------------------------------------------------------
SharedPythonOStream::SharedPythonOStream(size_t maxSize)
{
  // Use Python to allocate the memory.
  Py_ssize_t bufferSize = NextPythonSize(maxSize);

  PyObject * pys = PyString_FromStringAndSize(0, bufferSize);

  // Access the pointers.
  char *buffer=0;
  Py_ssize_t n=0;
  PyString_AsStringAndSize(pys, &buffer, &n);
  
  // Hang on to everything
  p_ = boost::shared_ptr<SharedPythonOStreamInternals>(
    new SharedPythonOStreamInternals(pys, buffer, maxSize));                                       
}


// -------------------------------------------------------------
std::ostream &SharedPythonOStream::getStream() const
{
  if(!p_) throw std::runtime_error("Stream is closed.");
  return p_->s;
}

// -------------------------------------------------------------
PyObject * SharedPythonOStream::close()
{
  if (!p_)
    throw std::runtime_error("Stream is closed.");
  p_->s.flush();
  p_->s.freeze();
  size_t n = p_->s.pcount();
  size_t size = PyString_Size(p_->pys);
  if (size <= n) 
    throw std::runtime_error("Stream output larger than allocated buffer.");

  // Create a new Python string with the correct size
  nta::py::String ss(p_->pys.release());
  nta::py::String result((const char *)ss, n);
  return result.release();
}

#endif // NTA_PYTHON_SUPPORT


