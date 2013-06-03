# ----------------------------------------------------------------------
#  Copyright (C) 2009, Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""This file defines the ConsolePrinterMixin class and the Tee class.

The ConsolePrinterMixin is used by objects that need to print to the screen
under the control of a verbosity level.

The Tee class is used to redirect standard output to a file in addition to
sending it to the console.
"""

import sys

class ConsolePrinterMixin(object):
  """Mixin class for printing to the console with different verbosity levels.


  """

  def __init__(self, verbosity=1):
    """Initialize console printer functionality.

    verbosity (int)
        0: don't print anything to stdout
        1: normal (production-level) printing
        2: extra debug information
        3: lost of debug information
        values higher than 3 are possible, but shouldn't normally be used
    """

    # The internal attribute is consolePrinterVerbosity to make it
    # more clear where it comes from (without having to trace back
    # through the class hierarchy). This attribute is normally
    # not accessed directly, but it is fine to read or write it
    # directly if you know what you're doing.
    self.consolePrinterVerbosity = verbosity

  def cPrint(self, level, message, *args, **kw):
    """Print a message to the console.

    Prints only if level <= self.consolePrinterVerbosity
    Printing with level 0 is equivalent to using a print statement,
    and should normally be avoided.

    level is an integer indicating the urgency of the message with
    lower values meaning more urgent (messages at level 0  are the
    most urgent and are always printed)

    message is a string, possibly with format specifiers

    args speficies the values for any format specifiers in message

    newline is the only keyword argument. True (default) if a newline should
    be printed
    """

    if level > self.consolePrinterVerbosity:
      return

    if len(kw) > 1:
      raise KeyError("Invalid keywords for cPrint: %s" % str(kw.keys()))

    newline = kw.get("newline", True)
    if len(kw) == 1 and 'newline' not in kw:
      raise KeyError("Invalid keyword for cPrint: %s" % kw.keys()[0])

    if len(args) == 0:
      if newline:
        print message
      else:
        print message,
    else:
      if newline:
        print message % args
      else:
        print message % args,

class Tee(object):
  """This class captures standard output and writes it to a file
  in addition to sending it to the console
  """
  def __init__(self, outputFile):
    self.outputFile = open(outputFile, 'w', buffering=False)
    self.stdout = sys.stdout
    sys.stdout = self

  def write(self, s):
    self.outputFile.write(s)
    self.stdout.write(s)

  def flush(self):
    self.stdout.flush()
    self.outputFile.flush()

  def fileno(self):
    return self.outputFile.fileno()

  def close(self):
    self.outputFile.close()
    sys.stdout = self.stdout

  def __enter__(self):
    pass

  def __exit__(self, exc_type, exc_value, traceback):
    self.close()