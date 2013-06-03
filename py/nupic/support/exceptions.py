# ----------------------------------------------------------------------
#  Copyright (C) 2012 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

import sys
import traceback


###############################################################################
class TimeoutError(Exception):
  """ The requested operation timed out """
  pass


###############################################################################
class StreamDisappearedError(Exception):
  """ Signals that a data stream became suddenly unavailable """
  pass


###############################################################################
class GrokJobFailException(Exception):
  """ This exception signals that the Grok job (e.g., Hypersearch, Production,
  etc.) should be aborted due to the given error.
  """

  def __init__(self, errorCode, msg):
    """
    Parameters:
    ---------------------------------------------------------------------
    errorCode:      An error code from the support.errorcodes.ErrorCodes
                    enumeration
    msg:            Error message string
    """

    self.__errorCode = errorCode
    self.__msg = msg

    super(JobFatalException, self).__init__(errorCode, msg)

    return


  def getWorkerCompletionMessage(self):
    """ Generates a worker completion message that is suitable for the
    worker_completion_message field in jobs table

    Parameters:
    ---------------------------------------------------------------------
    retval:         The worker completion message appropriate for the
                    "worker_completion_message" field in jobs table
    """

    msg = "%s: %s\n%s" % (self.__errorCode, self.__msg, traceback.format_exc())

    return msg


  @classmethod
  def mapCurrentException(cls, e, errorCode, msg):
    """ Raises GrokJobFailException by mapping from another exception that
    is being handled in the caller's scope and preserves the current exception's
    traceback.

    Parameters:
    ---------------------------------------------------------------------
    e:              The source exception
    errorCode:      An error code from the support.errorcodes.ErrorCodes
                    enumeration
    msg:            Error message string
    """

    traceback = sys.exc_info()[2]
    assert traceback is not None

    newMsg = "%s: %r" % (msg, e)

    e = GrokJobFailException(errorCode=errorCode, msg=newMsg)

    raise e, None, traceback