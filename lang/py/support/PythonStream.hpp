#ifndef NTA_PYTHON_STREAM_HPP
#define NTA_PYTHON_STREAM_HPP

#ifdef NTA_PYTHON_SUPPORT

/**
 * -----------------------------------------------------------------
 *  Copyright (C) 2009 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * -----------------------------------------------------------------
 */

#include <lang/py/support/PyHelpers.hpp>
#include <iosfwd>
#include <boost/shared_ptr.hpp>

struct SharedPythonOStreamInternals;

/**
 * Data structure for sharing an ostream with a Python string.
 */
class SharedPythonOStream
{
public:
  SharedPythonOStream(size_t maxSize);
  std::ostream &getStream() const;
  PyObject *close();

private:
  boost::shared_ptr<SharedPythonOStreamInternals> p_;
};

//------------------------------------------------------------------

#endif // NTA_PYTHON_SUPPORT

#endif // NTA_PYTHON_STREAM_HPP





