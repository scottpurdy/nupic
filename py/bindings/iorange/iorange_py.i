%module(package="nupic.bindings") iorange

%include <lang/py/bindings/exception.i>

%pythoncode %{
# ----------------------------------------------------------------------
#  Copyright (C) 2006,2010 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------
%}

///////////////////////////////////////////////////////////////////
/// Includes necessary to compile the C wrappers
///////////////////////////////////////////////////////////////////

%{

/**
 * ----------------------------------------------------------------------
 *  Copyright (C) 2006,2010 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
*/

#include <numpy/arrayobject.h>
#include <lang/py/support/NumpyVector.hpp>
#include <py/bindings/iorange/WrappedVector.hpp>
#include <nta/ntypes/ArrayBase.hpp>

%}

%naturalvar;

%include <lang/py/bindings/exception.i>
%include <lang/py/bindings/numpy.i>
%include <py/bindings/types.i>
%include <py/bindings/reals.i>

// An easy-to-wrap vector class that is designed to 
// look like a Python container.

%ignore nta::WrappedVectorIter::operator[];
%ignore nta::WrappedVectorIter::operator++;
%ignore nta::WrappedVectorIter::operator--;
%ignore nta::WrappedVector::operator=;

%include <lang/py/support/NumpyVector.hpp>
%include <py/bindings/iorange/WrappedVector.hpp>
%template(WrappedVectorList) std::vector<nta::WrappedVector>;

%extend nta::WrappedVector {

  // Used by NuPIC 2 to directly wrap an array object
  void setFromArray(PyObject* parray)
  {
    if (!PyCObject_Check(parray))
    {
      throw std::invalid_argument("setFromArray -- object is not a CObject");
    }
    nta::ArrayBase* array = (nta::ArrayBase*)PyCObject_AsVoidPtr(parray);
    if (array->getType() != NTA_BasicType_Real32)
    {
      throw std::invalid_argument("setFromArray -- array datatype is not Real32");
    }
    self->setPointer(array->getCount(), (nta::Real*)array->getBuffer());
  }


void copyFromPointer(size_t n, PyObject * obj) {
  nta::Real * p = (nta::Real *) PyCObject_AsVoidPtr(obj);
  if (n != self->__len__())
    throw std::invalid_argument("Sizes must match.");
  self->copyFromT(n, 1, p);
}

void copyFromArray(PyObject *obj) {
  nta::NumpyVector v(obj);
  nta::Size n = v.size();
  if(!(n == self->__len__())) throw std::invalid_argument("Sizes must match.");
  self->copyFromT(n, v.incr(), v.addressOf(0));
}

nta::WrappedVector __getslice__(long long i, long long j) const {
  self->adjust(i);
  self->adjust(j);
  return self->slice(i, j);
}

void __setslice__(long long i, long long j, PyObject *obj) {
  self->adjust(i);
  self->adjust(j);
  nta::NumpyVector v(obj);
  nta::Size n = v.size();
  nta::WrappedVector toSet = self->slice(i, j);
  if(!(n == toSet.__len__())) {
    char errBuffer[256];
    snprintf(errBuffer, 256-1, 
        "Expected to set slice of size %d but received %d inputs.",
        (int) toSet.__len__(), (int) n);
    throw std::invalid_argument(errBuffer);
  }
  toSet.copyFromT(n, v.incr(), v.addressOf(0));
}

PyObject *array() const {
  int n = self->__len__();
  nta::NumpyVector v(n);
  self->copyIntoT(n, v.incr(), v.addressOf(0));
  return v.forPython();
}

}

