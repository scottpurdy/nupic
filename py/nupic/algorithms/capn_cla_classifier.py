# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013, Numenta, Inc.  Unless you have purchased from
# Numenta, Inc. a separate commercial license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

"""This module contains the CLA classifier implementation using Cap'n Proto."""

import capnp


_BIT_HISTORY = capnp.load("../../../nta/algorithms/bit_history.capnp")



class BitHistory(object):
  """Class to store an activationPattern  bit history."""


  __VERSION__ = 2
  __slots__ = ("_proto", "_classifier")


  def __init__(self, classifier, bitNum, nSteps):
    """Constructor for bit history.

    Parameters:
    ---------------------------------------------------------------------
    classifier:    instance of the CLAClassifier that owns us
    bitNum:        activation pattern bit number this history is for,
                        used only for debug messages
    nSteps:        number of steps of predition this history is for, used
                        only for debug messages
    """
    # Store reference to the classifier
    self._classifier = classifier

    self._proto = _BIT_HISTORY

    # Form our "id"
    self._id = "%d[%d]" % (bitNum, nSteps)

    # Dictionary of bucket entries. The key is the bucket index, the
    # value is the dutyCycle, which is the rolling average of the duty cycle
    self._stats = array.array('f')

    # lastUpdate is the iteration number of the last time it was updated.
    self._lastTotalUpdate = None

    # The bit's learning iteration. This is updated each time store() gets
    # called on this bit.
    self._learnIteration = 0

    # Set the version to the latest version.
    # This is used for serialization/deserialization
    self._version = BitHistory.__VERSION__


  def store(self, iteration, bucketIdx):
    """Store a new item in our history.

    This gets called for a bit whenever it is active and learning is enabled

    Parameters:
    --------------------------------------------------------------------
    iteration:  the learning iteration number, which is only incremented
                  when learning is enabled
    bucketIdx:  the bucket index to store

    Save duty cycle by normalizing it to the same iteration as
    the rest of the duty cycles which is lastTotalUpdate.

    This is done to speed up computation in inference since all of the duty
    cycles can now be scaled by a single number.

    The duty cycle is brought up to the current iteration only at inference and
    only when one of the duty cycles gets too large (to avoid overflow to
    larger data type) since the ratios between the duty cycles are what is
    important. As long as all of the duty cycles are at the same iteration
    their ratio is the same as it would be for any other iteration, because the
    update is simply a multiplication by a scalar that depends on the number of
    steps between the last update of the duty cycle and the current iteration.
    """

    # If lastTotalUpdate has not been set, set it to the current iteration.
    if self._lastTotalUpdate == None:
      self._lastTotalUpdate = iteration
    # Get the duty cycle stored for this bucket.
    statsLen = len(self._stats) - 1
    if bucketIdx > statsLen:
      self._stats.extend(itertools.repeat(0.0, bucketIdx - statsLen))

    # Update it now.
    # duty cycle n steps ago is dc{-n}
    # duty cycle for current iteration is (1-alpha)*dc{-n}*(1-alpha)**(n)+alpha
    dc = self._stats[bucketIdx]

    # To get the duty cycle from n iterations ago that when updated to the
    # current iteration would equal the dc of the current iteration we simply
    # divide the duty cycle by (1-alpha)**(n). This results in the formula
    # dc'{-n} = dc{-n} + alpha/(1-alpha)**n where the apostrophe symbol is used
    # to denote that this is the new duty cycle at that iteration. This is
    # equivalent to the duty cycle dc{-n}
    denom = ((1.0 - self._classifier.alpha) **
                                  (iteration - self._lastTotalUpdate))
    if denom > 0:
      dcNew = dc + (self._classifier.alpha / denom)

    # This is to prevent errors associated with inf rescale if too large
    if denom == 0 or dcNew > DUTY_CYCLE_UPDATE_INTERVAL:
      exp =  (1.0 - self._classifier.alpha) ** (iteration-self._lastTotalUpdate)
      for (bucketIdxT, dcT) in enumerate(self._stats):
        dcT *= exp
        self._stats[bucketIdxT] = dcT

      # Reset time since last update
      self._lastTotalUpdate = iteration

      # Add alpha since now exponent is 0
      dc = self._stats[bucketIdx] + self._classifier.alpha
    else:
      dc = dcNew

    self._stats[bucketIdx] = dc
    if self._classifier.verbosity >= 2:
      print "updated DC for %s, bucket %d to %f" % (self._id, bucketIdx, dc)


  def infer(self, iteration, votes):
    """Look up and return the votes for each bucketIdx for this bit.

    Parameters:
    --------------------------------------------------------------------
    iteration:  the learning iteration number, which is only incremented
                  when learning is enabled
    votes:      a numpy array, initialized to all 0's, that should be filled
                  in with the votes for each bucket. The vote for bucket index N
                  should go into votes[N].
    """
    # Place the duty cycle into the votes and update the running total for
    # normalization
    total = 0
    for (bucketIdx, dc) in enumerate(self._stats):
    # Not updating to current iteration since we are normalizing anyway
      if dc > 0.0:
        votes[bucketIdx] = dc
        total += dc

    # Experiment... try normalizing the votes from each bit
    if total > 0:
      votes /= total
    if self._classifier.verbosity >= 2:
      print "bucket votes for %s:" % (self._id), _pFormatArray(votes)


  def __getstate__(self):
    return dict((elem, getattr(self, elem)) for elem in self.__slots__)


  def __setstate__(self, state):
    version = 0
    if "_version" in state:
      version = state["_version"]

    # Migrate from version 0 to version 1
    if version == 0:
      stats = state.pop("_stats")
      assert isinstance(stats, dict)
      maxBucket = max(stats.iterkeys())
      self._stats = array.array('f', itertools.repeat(0.0, maxBucket+1))
      for index, value in stats.iteritems():
        self._stats[index] = value
    elif version == 1:
      state.pop('_updateDutyCycles', None)
    elif version == 2:
      pass
    else:
      raise Exception("Error while deserializing %s: Invalid version %s"
                      %(self.__class__, version))
    
    for attr, value in state.iteritems():
      setattr(self, attr, value)

    self._version = BitHistory.__VERSION__



class CapnCLAClassifier(object):
