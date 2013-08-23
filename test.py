#!/usr/bin/env python
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

"""TODO"""

import capnp


_BIT_HISTORY = capnp.load("../../../nta/algorithms/bit_history.capnp")

CHECKPOINT = "/Users/spurdy/tmp.bin"



def create(numBits):
  message = capnp.MallocMessageBuilder()
  l = message.initRoot(_BIT_HISTORY.HistoryList)
  l.initHistories(numBits)

  for bitNum in xrange(numBits):
    bitHistory = l.histories[0]

    # Set the version to the latest version.
    # This is used for serialization/deserialization
    bitHistory.version = 3

    # Form our "id"
    bitHistory.id = "%d[%d]" % (bitNum, nSteps)

    # Dictionary of bucket entries. The key is the bucket index, the
    # value is the dutyCycle, which is the rolling average of the duty cycle
    bitHistory.initStats(100)
    for i in xrange(100):
      bitHistory.stats[i] = 1.0

    # lastUpdate is the iteration number of the last time it was updated.
    bitHistory.lastTotalUpdate = 0

    # The bit's learning iteration. This is updated each time store() gets
    # called on this bit.
    bitHistory.learnIteration = 0

  return message, bitHistory



def read():
  with open(CHECKPOINT) as fin:
    message = capnp.PackedFdMessageReader(fin.fileno())
    l = message.getRoot(_BIT_HISTORY.HistoryList)
  return message, l



def write(message):
  with open(CHECKPOINT, "w") as fout:
    capnp.writePackedMessageToFd(fout.fileno(), message)



if __name__ == '__main__':
  t0 = time.time()
  m, l = create(1000)
  t1 = time.time()
  write(m)
  t2 = time.time()

  for _ in xrange(1000):
    m, l = read()
    for i in xrange(1000):
      bitHistory = l.histories[i]
      for j in xrange(100):
        bitHistory.stats[j] *= 0.999
    write(m)

  t3 = time.time()

  print "Time to create: ", t1 - t0
  print "Time to write: ", t2 - t1
  print "Time for model swapping: ", t3 - t2
