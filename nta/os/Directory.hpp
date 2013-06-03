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


#ifndef NTA_DIRECTORY_HPP
#define NTA_DIRECTORY_HPP

//----------------------------------------------------------------------

#include <apr-1/apr.h>
#include <apr-1/apr_file_info.h>
#include <string>

//----------------------------------------------------------------------

namespace nta 
{
  class Path;
  
  namespace Directory
  {
    // check if a directory exists
    bool exists(const std::string & path);

    bool empty(const std::string & path);
    
    // get current working directory
    std::string getCWD();
		
    // set current working directories
    void setCWD(const std::string & path);

    // Copy directory tree rooted in 'source' to 'destination'
    void copyTree(const std::string & source, const std::string & destination);
    		
    // Remove directory tree rooted in 'path'
    bool removeTree(const std::string & path, bool noThrow=false);
		
    // Create directory 'path' including all parent directories if missing
    // returns the first directory that was actually created.
    //
    // For example if path is /A/B/C/D 
    //    if /A/B/C/D exists it returns ""
    //    if /A/B exists it returns /A/B/C
    //    if /A doesn't exist it returns /A/B/C/D
    // 
    // Failures will throw an exception
    void create(const std::string & path, bool otherAccess=false, bool recursive=false);

    std::string createTemporary(const std::string &templatePath);

    struct Entry : public apr_finfo_t
    {
      enum Type { FILE, DIRECTORY, LINK };
			
      Type type;
      std::string path;
    };

    class Iterator
    {
    public:

      Iterator(const Path & path);		
      Iterator(const std::string & path);
      ~Iterator();
		
      // Resets directory to start. Subsequent call to next() 
      // will retrieve the first entry
      void reset();
      // get next directory entry
      Entry * next(Entry & e);
		
    private:
      Iterator();
      Iterator(const Iterator &);
		
      void init(const std::string & path);
    private:
      std::string path_;
      apr_dir_t * handle_;
      apr_pool_t * pool_;
    };
  }
}

#endif // NTA_DIRECTORY_HPP


