# ----------------------------------------------------------------------
# Copyright (C) 2012, Numenta Inc. All rights reserved.
#
# The information and source code contained herein is the
# exclusive property of Numenta Inc.  No part of this software
# may be used, reproduced, stored or distributed in any form,
# without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""Pylint checker for trailing whitespace."""

from logilab import astng
from pylint.checkers import BaseChecker
from pylint.interfaces import IRawChecker


MSGS = {
    'W9810': ('Trailing whitespace', 'trailing-whitespace',
              'Used when there is trailing whitespace on a line.'),
    }


class TrailingWhitespaceChecker(BaseChecker):
  """Checks for trailing whitespace on every line of the file."""

  __implements__ = IRawChecker

  name = 'trailing_whitespace_raw'
  msgs = MSGS
  options = ()

  def process_module(self, node):
    """Process a module.

    The module's content is accessible via the node.file_stream object.
    """
    for lineno, line in enumerate(node.file_stream):
      lineno += 1
      if line.rstrip() != line.rstrip('\n') and len(line.strip()) > 0:
        self.add_message('W9810', line=lineno)


def register(linter):
  """Register the checker with the linter."""
  linter.register_checker(TrailingWhitespaceChecker(linter))
