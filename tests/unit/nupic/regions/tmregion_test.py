# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2017, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

"""Unit tests for TMRegion."""

import json
import pkg_resources
import sys
import tempfile
import unittest

import capnp
import numpy

from nupic.data.file_record_stream import FileRecordStream
from nupic.encoders import MultiEncoder, ScalarEncoder
from nupic.engine import Network
from nupic.regions import tm_region_proto_capnp

_INPUT_FILE_PATH = pkg_resources.resource_filename(
  "nupic.datafiles", "extra/hotgym/rec-center-hourly.csv"
)

TM_PARAMS = {
    "temporalImp": "tm_py",
    "verbosity": 0,
    "columnCount": 20,
    "cellsPerColumn": 3,
    "inputWidth": 20,
    "seed": 1987,
    "newSynapseCount": 3,
    "maxSynapsesPerSegment": 5,
    "maxSegmentsPerCell": 1,
    "initialPerm": 0.21,
    "permanenceInc": 0.1,
    "permanenceDec": 0.1,
    "globalDecay": 0.0,
    "maxAge": 0,
    "minThreshold": 2,
    "activationThreshold": 3,
    "outputType": "normal",
    "pamLength": 3,
}



def createEncoder():
  """Create the encoder instance for our test and return it."""
  consumption_encoder = ScalarEncoder(5, 0.0, 100.0, n=20, name="consumption",
      clipInput=True, forced=True)

  encoder = MultiEncoder()
  encoder.addEncoder("consumption", consumption_encoder)

  return encoder



class TMRegionTest(unittest.TestCase):


  def testSerialization(self):
    net1 = Network()

    net1.addRegion("sensor", "py.RecordSensor",
                      json.dumps({"verbosity": 0}))
    dataSource = FileRecordStream(streamID=_INPUT_FILE_PATH)
    sensor = net1.regions["sensor"].getSelf()
    # The RecordSensor needs to know how to encode the input values
    sensor.encoder = createEncoder()
    # Specify the dataSource as a file record stream instance
    sensor.dataSource = dataSource

    net1.addRegion("temporalPoolerRegion", "py.TMRegion",
                      json.dumps(TM_PARAMS))

    net1.link("sensor", "temporalPoolerRegion", "UniformLink", "")

    net1.initialize()
    net1.run(5)

    print dir(tm_region_proto_capnp)
    message1 = tm_region_proto_capnp.TMRegionProto.new_message()
    net1.write(message1)

    f = tempfile.TemporaryFile()
    try:
      message1.write(f)
      f.seek(0)
      message2 = tm_region_proto_capnp.TMRegionProto.read(f)
    finally:
      f.close()

    net2 = Network.read(message2)

    net1.run(5)
    net2.run(5)
    #self.assertTrue(numpy.array_equal(net1.




if __name__ == "__main__":
  unittest.main()
