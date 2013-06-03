# ----------------------------------------------------------------------
#  Copyright (C) 2011 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------



class ErrorCodes(object):
  streamReading         = "E10001"
  tooManyModelErrs      = "E10002"
  hypersearchLogicErr   = "E10003"
  productionModelErr    = "E10004"      # General PM error
  modelCommandFormatErr = "E10005"      # Invalid model command request object
  tooManyFailedWorkers  = "E10006"
  unspecifiedErr        = "E10007"
  modelInputLostErr     = "E10008"      # Input stream was garbage-collected
  requestOutOfRange     = "E10009"      # If a request range is invalid
  invalidType           = "E10010"      # Invalid 