#!/usr/bin/env python
# ----------------------------------------------------------------------
#  Copyright (C) 2006-2010 Numenta Inc. All rights reserved.
#
#  The information and src code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------
import os
import sys
import time
import logging
import getopt
import socket
import shutil
import platform
import math
import getpass
import boto
from datetime import datetime
import pybuild.utils as utils
import pybuild.test_release as test
from pybuild.orderedDict import orderedDict
from pybuild.arch import getArch
import pybuild.make_release as release
import pybuild.mail as mail
from optparse import OptionParser
from boto.s3.key import Key

pythonVersion = sys.version[:3]
myDir = os.path.dirname(os.path.abspath(__file__))
log = logging.getLogger("auto")

class JenkinsBuilds:
  def isEmpty(self, filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    if len(lines) == 0:
      return True
    else:
      return False

  def isNotEmpty(self, filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    if len(lines) > 0:
      return True
    else:
      return False

  def isTagInList(self, tag, filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    if tag in lines:
      return True
    else:
      return False

  def removeTagFromFile(self, tag, filename, tmpfilename):
    file = open(filename)
    tmpfile = open(tmpfilename, 'w')
    lines = file.readlines()
    for line in lines:
      if tag not in line:
        print >> tmpfile, line
    file.close()
    tmpfile.close()
    os.system('cp %s %s' %(tmpfilename, filename))

  def addTagToFile(self, tag, filename):
    file = open(filename, 'a')
    print >> file, tag
    file.close()

  def getLatestBuild(self, filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    lastLine = lines[len(lines)-1]
    return lastLine

  def getBuildsInOrder(self, filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    buildsList = []
    listLen = len(lines)
    while (listLen > 0):
      buildsList.append(lines[listLen-1])
      listLen = listLen - 1
    return buildsList

  def getLatestUntestedBuild(self, tempStatusFile, testedBuilds):
    latestUntestedBuild = ""
    toTest = self.getBuildsInOrder(tempStatusFile)
    tested = self.getBuildsInOrder(testedBuilds)
    for x in toTest:
      print x
      if x not in tested and x != '\n':
        return x
    return latestUntestedBuild


def downloadFile(conn, filename, bucketname, localpath):
  print "Getting all buckets ..."
  buckets = conn.get_all_buckets()
  bucket = boto.s3.bucket.Bucket()
  for b in buckets:
    if b.name == bucketname:
      print "Found the bucket ..."
      bucket = b
  k = Key(bucket)
  k.key = filename
  print "Checking if file exists locally ..."
  if filename == "":
    print "No filename specified. Quitting ..."
    return 1
  print "Downloading file ..."
  k.get_contents_to_filename(os.path.join(localpath, filename))
  print "Download file done."

def saveFile(conn, dirname, filename, bucketname):
  print "Getting all buckets ..."
  buckets = conn.get_all_buckets()
  bucket = boto.s3.bucket.Bucket()
  os.chdir(dirname)
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


if __name__ == '__main__':

  # Get builds_to_test and builds_tested from S3
  # Check if test is in progress - quit
  # If not, get build number to test
  # Check if test done for this build
  # If done, remove from builds_to_test and Try next build until list is empty
  # If not, update to that build
  # Begin test
  # Copy log file to S3
  # Change builds_to_test and builds_tested and put in S3
  rootdir = os.path.join('../workspace')
  conn = boto.connect_s3()
  builds = JenkinsBuilds()
  jenkinsBuilds = []
  testedBuilds = []
  verifiedBuilds = []

  # Get builds_to_test and builds_tested from S3
  downloadFile(conn, 'builds_tested', 'numenta.builds', rootdir)

  doneTestsFile = os.path.join(rootdir, 'builds_tested')
  verifiedTestsFile = os.path.join(rootdir, 'awstest_done')
  latestFile = os.path.join(rootdir, 'latest')
  testedBuilds = builds.getBuildsInOrder(doneTestsFile)
  verifiedBuilds = builds.getBuildsInOrder(verifiedTestsFile)

  # Get build to test
  latestBuild = builds.getLatestBuild(doneTestsFile)
  latestBuildToTest = latestBuild.rstrip()
  if latestBuild in verifiedBuilds or latestBuildToTest == "":
    latestBuildToTest = (builds.getLatestUntestedBuild(doneTestsFile, verifiedTestsFile)).rstrip()

  # If all builds have been tested
  if latestBuildToTest == "":
    print "No builds to test. Exiting."
    sys.exit(0)
 
  print "Build to test - %s" %latestBuildToTest

  # Get that log
  downloadFile(conn, '%s.out' %latestBuildToTest, 'numenta.clustertestresults', rootdir)

  # Add to in progress file
  f = open(latestFile, 'w')
  print >> f, latestBuildToTest
  f.close()

