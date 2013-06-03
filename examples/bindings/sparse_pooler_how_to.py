#!/usr/bin/env python

# ----------------------------------------------------------------------
#  Copyright (C) 2006,2007 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

from nupic.bindings.math import *
from nupic.bindings.algorithms import *

import numpy
import cPickle

#--------------------------------------------------------------------------------
# SparsePooler learning and inference
#--------------------------------------------------------------------------------
def sparse_pooler_use_case():

    segment_size = 4
    norm = 2
    kWinners = 0
    threshold = .25
    sparsification_mode = 2
    inference_mode = 0
    min_accept_distance = 1e-5
    min_accept_norm = .5
    min_proto_sum = 3
    sigma = .1

    # Create a SparsePooler
    sp = SparsePooler(SparsePoolerInputMasks(segment_size, [[(0,8)]]),
                      1, norm,
                      sparsification_mode,
                      inference_mode,
                      kWinners,
                      threshold,
                      min_accept_distance,
                      min_accept_norm,
                      min_proto_sum,
                      sigma)

    # Change its parameters
    sp.setSparsificationMode(1)
    sp.setDoNormalization(1)
    sp.setNorm(1.5)
    sp.setKWinners(2)
    sp.setMinAcceptDistance(.001)
    sp.setMinAcceptNorm(.001)
    sp.setSigma(.414)

    # Learn
    for i in range(0, 10):
        x = numpy.random.random((8))
        sp.learn(x)

    # Infer
    for i in range(0, 10):
        x = numpy.random.random((8))
        sp.infer(x)

    # Access the stored prototypes
    print '\nNumber of prototypes\n', sp.getNPrototypes(0)
    print '\nPrototypes\n', sp.prototypes(0)

    # Persist the SparsePooler
    cPickle.dump(sp, open('test.txt', 'w'))
    sp2 = cPickle.load(open('test.txt', 'r'))

#--------------------------------------------------------------------------------
sparse_pooler_use_case()
