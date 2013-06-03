#!/usr/bin/env python
# ----------------------------------------------------------------------
#  Copyright (C) 2010 Numenta Inc. All rights reserved.
#
#  The information and source code contained herein is the
#  exclusive property of Numenta Inc. No part of this software
#  may be used, reproduced, stored or distributed in any form,
#  without explicit written authorization from Numenta Inc.
# ----------------------------------------------------------------------

"""
This file implements the CLA Classifier region. See the comments in the class
definition of CLAClassifierRegion for a description.
"""

import numpy
from PyRegion import PyRegion
from nupic.algorithms.cla_classifier_factory import CLAClassifierFactory

###############################################################################
class CLAClassifierRegion(PyRegion):
  """
  CLAClassifierRegion implements a CLA specific classifier that accepts a binary
  input from the level below (the "activationPattern") and information from the
  sensor and encoders (the "classification") describing the input to the system
  at that time step.

  When learning, for every bit in activation pattern, it records a history of the
  classification each time that bit was active. The history is bounded by a
  maximum allowed age so that old entries are thrown away.

  For inference, it takes an ensemble approach. For every active bit in the
  activationPattern, it looks up the most likely classification(s) from the
  history stored for that bit and then votes across these to get the resulting
  classification(s).

  The caller can choose to tell the region that the classifications for
  iteration N+K should be aligned with the activationPattern for iteration N.
  This results in the classifier producing predictions for K steps in advance.
  Any number of different K's can be specified, allowing the classifier to learn
  and infer multi-step predictions for a number of steps in advance.
  """
  
###############################################################################
  @classmethod
  def getSpec(cls):
    ns = dict(
        description=CLAClassifierRegion.__doc__,
        singleNodeOnly=True,

        # The inputs and outputs are not used in this region because they are
        #  either sparse vectors or dictionaries and hence don't fit the "vector
        #  of real" input/output pattern.
        # There is a custom compute() function provided that accepts the
        #  inputs and outputs.
        inputs=dict(
          categoryIn=dict(
            description='Category of the input sample',
            dataType='Real32',
            count=1,
            required=True,
            regionLevel=True,
            isDefaultInput=False,
            requireSplitterMap=False),

          bottomUpIn=dict(
            description='Belief values over children\'s groups',
            dataType='Real32',
            count=0,
            required=True,
            regionLevel=False,
            isDefaultInput=True,
            requireSplitterMap=False),
        ),

        outputs=dict(),

        parameters=dict(
          learningMode=dict(
            description='Boolean (0/1) indicating whether or not a region '
                        'is in learning mode.',
            dataType='UInt32',
            count=1,
            constraints='bool',
            defaultValue=1,
            accessMode='ReadWrite'),

          inferenceMode=dict(
            description='Boolean (0/1) indicating whether or not a region '
                        'is in inference mode.',
            dataType='UInt32',
            count=1,
            constraints='bool',
            defaultValue=0,
            accessMode='ReadWrite'),

          steps=dict(
            description='Comma separated list of the desired steps of '
                        'prediction that the classifier should learn',
            dataType="Byte",
            count=0,
            constraints='',
            defaultValue='1',
            accessMode='Create'),

          alpha=dict(
            description='The alpha used to compute running averages of the '
               'bucket duty cycles for each activation pattern bit. A lower '
               'alpha results in longer term memory',
            dataType="Real32",
            count=1,
            constraints='',
            defaultValue=0.001,
            accessMode='Create'),

          implementation=dict(
            description='The classifier implementation to use.',
            accessMode='ReadWrite',
            dataType='Byte',
            count=0,
            constraints='enum: py, cpp'),

           clVerbosity=dict(
            description='An integer that controls the verbosity level, '
                        '0 means no verbose output, increasing integers '
                        'provide more verbosity.',
            dataType='UInt32',
            count=1,
            constraints='',
            defaultValue=0 ,
            accessMode='ReadWrite'),

     ),
      commands=dict()
    )

    return ns

  ###############################################################################
  def __init__(self,
               steps='1',
               alpha=0.001,
               clVerbosity=0,
               implementation=None,
               ):

    # Convert the steps designation to a list
    self.steps = steps
    self.stepsList = eval("[%s]" % (steps))
    self.alpha = alpha
    self.verbosity = clVerbosity

    # Initialize internal structures
    self._claClassifier = CLAClassifierFactory.create(
        steps=self.stepsList,
        alpha=self.alpha,
        verbosity=self.verbosity,
        implementation=implementation,
        )
    self.learningMode = True
    self.inferenceMode = False

    self._initEphemerals()


  ###############################################################################
  def _initEphemerals(self):
    pass


   ###############################################################################
  def initialize(self, dims, splitterMaps):
    pass

  ###############################################################################
  def clear(self):
    self._claClassifier.clear()


  ###############################################################################
  def getParameter(self, name, index=-1):
    """
    Get the value of the parameter.

    @param name -- the name of the parameter to retrieve, as defined
            by the Node Spec.
    """
    # If any spec parameter name is the same as an attribute, this call
    # will get it automatically, e.g. self.learningMode
    return PyRegion.getParameter(self, name, index)


  ###############################################################################
  def setParameter(self, name, index, value):
    """
    Set the value of the parameter.

    @param name -- the name of the parameter to update, as defined
            by the Node Spec.
    @param value -- the value to which the parameter is to be set.
    """
    if name == "learningMode":
      self.learningMode = bool(int(value))
    elif name == "inferenceMode":
      self.inferenceMode = bool(int(value))
    else:
      return PyRegion.setParameter(self, name, index, value)


  ###############################################################################
  def reset(self):
    pass


  ###############################################################################
  def compute(self, inputs, outputs):
    """
    Process one input sample.
    This method is called by the runtime engine.

    We don't use this method in this region because the inputs and outputs don't
    fit the standard "vector of reals" used by the engine. Instead, call
    the customCompute() method directly
    """

    pass

  ###############################################################################
  def customCompute(self, recordNum, patternNZ, classification):
    """
    Process one input sample.
    This method is called by outer loop code outside the nupic-engine. We
    use this instead of the nupic engine compute() because our inputs and
    outputs aren't fixed size vectors of reals.

    Parameters:
    --------------------------------------------------------------------
    patternNZ:      list of the active indices from the output below
    classification: dict of the classification information:
                      bucketIdx: index of the encoder bucket
                      actValue:  actual value going into the encoder

    retval:     dict containing inference results, one entry for each step in
                self.steps. The key is the number of steps, the value is an
                array containing the relative likelihood for each bucketIdx
                starting from bucketIdx 0.

                for example:
                  {1 : [0.1, 0.3, 0.2, 0.7]
                   4 : [0.2, 0.4, 0.3, 0.5]}
    """

    return self._claClassifier.compute( recordNum=recordNum,
                                        patternNZ=patternNZ,
                                        classification=classification,
                                        learn = self.learningMode,
                                        infer = self.inferenceMode)



###############################################################################
if __name__=='__main__':
  from nupic.engine import Network
  n = Network()
  classifier = n.addRegion(
    'classifier',
    'py.CLAClassifierRegion',
    '{ steps: "1,2", maxAge: 1000}'
  )
