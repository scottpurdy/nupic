%module engine_internal

%pythoncode %{
# ----------------------------------------------------------------------
#  Copyright (C) 2010 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------
%}


%include <lang/py/bindings/exception.i>

%include "../../../common/engine_internal_common.i"

%include "../numpy.i"
 
%init %{
 import_array();
%}


%include <lang/py/support/PyArray.hpp>
%template(ByteArray) nta::PyArray<nta::Byte>;
%template(Int16Array) nta::PyArray<nta::Int16>;
%template(UInt16Array) nta::PyArray<nta::UInt16>;
%template(Int32Array) nta::PyArray<nta::Int32>;
%template(UInt32Array) nta::PyArray<nta::UInt32>;
%template(Int64Array) nta::PyArray<nta::Int64>;
%template(UInt64Array) nta::PyArray<nta::UInt64>;
%template(Real32Array) nta::PyArray<nta::Real32>;
%template(Real64Array) nta::PyArray<nta::Real64>;

%template(ByteArrayRef) nta::PyArrayRef<nta::Byte>;
%template(Int16ArrayRef) nta::PyArrayRef<nta::Int16>;
%template(UInt16ArrayRef) nta::PyArrayRef<nta::UInt16>;
%template(Int32ArrayRef) nta::PyArrayRef<nta::Int32>;
%template(UInt32ArrayRef) nta::PyArrayRef<nta::UInt32>;
%template(Int64ArrayRef) nta::PyArrayRef<nta::Int64>;
%template(UInt64ArrayRef) nta::PyArrayRef<nta::UInt64>;
%template(Real32ArrayRef) nta::PyArrayRef<nta::Real32>;
%template(Real64ArrayRef) nta::PyArrayRef<nta::Real64>;


%extend nta::Timer
{
  // Extend here (engine_internal) rather than nupic.engine because
  // in order to have properties, we would have to define a wrapper
  // class, and explicitly forward all methods to the contained class
  %pythoncode %{
    def __str__(self):
      return self.toString()

    elapsed = property(getElapsed)
    startCount = property(getStartCount)
  %}
}

%extend nta::Region
{
  PyObject * getSelf()
  {
    nta::Handle h = self->getParameterHandle("self");
    PyObject * p = (PyObject *)h;
    return p;
  }
  
  PyObject * getInputArray(std::string name)
  {
    return nta::PyArrayRef<nta::Byte>(self->getInputData(name)).asNumpyArray();
  }

  PyObject * getOutputArray(std::string name)
  {
    return nta::PyArrayRef<nta::Byte>(self->getOutputData(name)).asNumpyArray();
  }
}


%{
#include <nta/os/OS.hpp>
%}

// magic swig incantation
// provides: (real, virtual) = OS.getProcessMemoryUsage()
%include <typemaps.i>
class nta::OS
{
public:
  static void OS::getProcessMemoryUsage(size_t& OUTPUT, size_t& OUTPUT);
};


