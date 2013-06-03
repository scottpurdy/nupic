# ----------------------------------------------------------------------
#  Copyright (C) 2011 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

""" Script to upload build to S3
 
Usage:
  python upload_build.py [--bucketname=bucketname] --filename=filename
"""


from optparse import OptionParser
import getpass
import boto
import sys
import time
from boto.s3.key import Key


def uploadFile(conn, filename, bucketname):
  print "Getting all buckets ..."
  buckets = conn.get_all_buckets()
  bucket = boto.s3.bucket.Bucket()
  for b in buckets:
    if b.name == bucketname:
      print "Found the bucket ..."
      bucket = b
  k = Key(bucket)
  k.key = filename
  print "Filename %s" %filename
  print "Key %s" %k.key
  print "Uploading file ..."
  k.set_contents_from_filename(filename)
  print "Upload file done."
   

#############################################################################
if __name__ == "__main__":

  username = getpass.getuser()
  defaultBucketName = "numenta.builds"

  parser = OptionParser()
  parser.add_option("--bucketname", help="Name of bucket (default: %default)",
                    dest="bucketname", default=defaultBucketName)

  parser.add_option("--filename", help="Name of file",
                    dest="filename", default=None)

  options, args = parser.parse_args(sys.argv[1:])

  if len(args) > 0:
    print "Unknown arguments: %s" % (str(args))
    sys.exit(1)

  conn = boto.connect_s3()
  uploadFile(conn, options.filename, options.bucketname)

