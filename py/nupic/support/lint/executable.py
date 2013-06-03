# ----------------------------------------------------------------------
# Copyright (C) 2012, Numenta Inc. All rights reserved.
#
# The information and source code contained herein is the
# exclusive property of Numenta Inc.  No part of this software
# may be used, reproduced, stored or distributed in any form,
# without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""Pylint checker for executable scripts."""

import os

from pylint.checkers import BaseChecker
from pylint.interfaces import IRawChecker


MSGS = {
    'W9820': ('Non-executable script', 'non-executable',
              'Used when a script has a shebang line or __main__ check but '
              'is not executable.'),
    'W9821': ('Unprotected executable code', 'executable-no-main',
              'Used when a script has a shebang line or has executable '
              'permissions but does not have a __main__ check.'),
    'W9822': ('Missing shebang', 'executable-no-shebang',
              'Used when a script has executable permissions or has a __main__ '
              'check but is missing a shebang line.'),
    }


class ExecutableChecker(BaseChecker):
  """Checks for executable scripts."""

  __implements__ = IRawChecker

  name = 'executable_raw'
  msgs = MSGS
  options = ()

  def process_module(self, node):
    """Process a module.

    The module's content is accessible via the node.file_stream object.
    """
    isExecutable = os.access(node.path, os.X_OK)
    hasShebang = False
    hasMainProtection = False
    for lineno, line in enumerate(node.file_stream):
      lineno += 1
      line = line.strip()
      if lineno == 1 and (line == '#!/usr/bin/env python' or
                          line == '#! /usr/bin/env python'):
        hasShebang = True
      # Keep the checks on separate lines so this file doesn't appear as an
      # executable script.
      if ('__name__' in line and
          '__main__' in line):
        hasMainProtection = True
        break

    if (hasShebang or hasMainProtection) and not isExecutable:
      self.add_message('W9820')
    if (isExecutable or hasShebang) and not hasMainProtection:
      self.add_message('W9821')
    if (isExecutable or hasMainProtection) and not hasShebang:
      self.add_message('W9822', line=1)


def register(linter):
  """Register the checker with the linter."""
  linter.register_checker(ExecutableChecker(linter))
