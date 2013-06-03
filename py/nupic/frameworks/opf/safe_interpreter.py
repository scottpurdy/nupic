# ----------------------------------------------------------------------
# Copyright (C) 2013 Numenta Inc. All rights reserved.
#
# The information and source code contained herein is the
# exclusive property of Numenta Inc. No part of this software
# may be used, reproduced, stored or distributed in any form,
# without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""Safe Python interpreter for user-submitted code."""

import asteval



class SafeInterpreter(asteval.Interpreter):


  blacklisted_nodes = set(('while', 'for', ))


  def __init__(self, *args, **kwargs):
    """Initialize interpreter with blacklisted nodes removed from supported
    nodes.
    """
    self.supported_nodes = tuple(set(self.supported_nodes) -
                                 self.blacklisted_nodes)
    asteval.Interpreter.__init__(self, *args, **kwargs)
