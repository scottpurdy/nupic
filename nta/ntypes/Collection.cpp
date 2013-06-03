/**
 * ----------------------------------------------------------------------
 *  Copyright (C) 2010 Numenta Inc. All rights reserved.
 *
 *  The information and source code contained herein is the
 *  exclusive property of Numenta Inc. No part of this software
 *  may be used, reproduced, stored or distributed in any form,
 *  without explicit written authorization from Numenta Inc.
 * ----------------------------------------------------------------------
 */

#include <nta/ntypes/Collection.hpp>
#include <nta/utils/Log.hpp>
#include <string>
#include <vector>

namespace nta
{

/*
 * Implementation of the templated Collection class. 
 * This code is used to create explicit instantiations
 * of the Collection class. 
 * It is not compiled into the types library because
 * we instantiate for classes outside of the types library. 
 * For example, Collection<OutputSpec> is built in the 
 * net library where OutputSpec is defined. 
 * See nta/engine/Collections.cpp, which is where the 
 * Collection classes are instantiated.
 */

template <typename T> 
Collection<T>::Collection()
{
}
    
template <typename T> 
Collection<T>::~Collection()
{
}
    
template <typename T> 
size_t Collection<T>::getCount() const
{
  return vec_.size();
}

template <typename T> const
std::pair<std::string, T>& Collection<T>::getByIndex(size_t index) const
{
  NTA_CHECK(index < vec_.size());
  return vec_[index];
}

template <typename T> 
std::pair<std::string, T>& Collection<T>::getByIndex(size_t index)
{
  NTA_CHECK(index < vec_.size());
  return vec_[index];
}

template <typename T> 
bool Collection<T>::contains(const std::string & name) const
{
  typename CollectionStorage::const_iterator i;
  for (i = vec_.begin(); i != vec_.end(); i++)
  {
    if (i->first == name)
      return true;
  }
  return false;
}

template <typename T>
T Collection<T>::getByName(const std::string & name) const
{
  typename CollectionStorage::const_iterator i;
  for (i = vec_.begin(); i != vec_.end(); i++)
  {
    if (i->first == name)
      return i->second;
  }  
  NTA_THROW << "No item named: " << name;
}

template <typename T>
void Collection<T>::add(const std::string & name, const T & item)
{
  // make sure we don't already have something with this name
  typename CollectionStorage::const_iterator i;
  for (i = vec_.begin(); i != vec_.end(); i++)
  {
    if (i->first == name)
    {
      NTA_THROW << "Unable to add item '" << name << "' to collection "
                << "because it already exists";
    }
  }

  // Add the new item to the vector
  vec_.push_back(std::make_pair(name, item));
}


template <typename T>
void Collection<T>::remove(const std::string & name)
{
  typename CollectionStorage::iterator i;
  for (i = vec_.begin(); i != vec_.end(); i++)
  {
    if (i->first == name)
      break;
  }
  if (i == vec_.end())
    NTA_THROW << "No item named '" << name << "' in collection";

  vec_.erase(i);
}

}

