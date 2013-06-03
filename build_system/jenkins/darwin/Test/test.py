#!/usr/bin/env python
# ----------------------------------------------------------------------
#  Copyright (C) 2006-2011 Numenta Inc. All rights reserved.
#
#  The information and src code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

import sys
import pybuild.test_release as test
import logging

if __name__ == '__main__':
  build = sys.argv[1]
  workspace = sys.argv[2]
  outfile = sys.argv[3]

  # Enable full logging right away, so that we see error messages
  log = logging.getLogger("auto") 
  initialhandler = logging.StreamHandler(sys.stdout)
  formatter = logging.Formatter("%(asctime)s %(name)-7s %(levelname)-7s %(message)s", "%y-%m-%d %H:%M:%S")
  initialhandler.setFormatter(formatter)
  initialhandler.setLevel(logging.NOTSET)

  rootlogger = logging.getLogger('')
  rootlogger.setLevel(logging.NOTSET)
  rootlogger.addHandler(initialhandler)

  # Turn down manifest file logging level
  logging.getLogger('autotest').setLevel(logging.INFO)
  # Setup very short log
  veryshortlog = 'veryshortlog.out'
  veryshortlogger = logging.FileHandler(veryshortlog, "w")
  formatter = logging.Formatter("%(asctime)s %(levelname)-7s %(message)s", "%H:%M:%S")
  veryshortlogger.setFormatter(formatter)
  veryshortlogger.addFilter(logging.Filter("auto"))
  veryshortlogger.setLevel(logging.NOTSET)
  rootlogger = logging.getLogger('')
  rootlogger.setLevel(logging.NOTSET)
  rootlogger.addHandler(veryshortlogger)

  longlog = outfile
  shortlog = 'shortlog.out'

  # long log contains all messages
  longlogger = logging.FileHandler(longlog, "w")
  formatter = logging.Formatter("%(asctime)s %(name)-7s %(levelname)-7s %(message)s", "%y-%m-%d %H:%M:%S")
  longlogger.setFormatter(formatter)
  longlogger.setLevel(logging.NOTSET)

  # short log contains only autobuild messages of INFO or higher
  shortlogger = logging.FileHandler(shortlog, "w")
  formatter = logging.Formatter("%(asctime)s %(levelname)-7s %(message)s", "%H:%M:%S")
  shortlogger.setFormatter(formatter)
  shortlogger.addFilter(logging.Filter("auto"))
  shortlogger.setLevel(logging.INFO)

  rootlogger = logging.getLogger('')
  rootlogger.setLevel(logging.NOTSET)
  veryshortlogger.setLevel(logging.CRITICAL)
  rootlogger.addHandler(shortlogger)
  rootlogger.addHandler(longlogger)


  (passed, failed, disabled) = test.runTests(build, workspace)
  test.logTestResults((passed, failed, disabled),
                        (False, True, True),
                        "Primary Tests", log)
  longlogger.flush()
  shortlogger.flush()
  if len(failed) > 0:
    print "The following tests failed: %s" %failed
